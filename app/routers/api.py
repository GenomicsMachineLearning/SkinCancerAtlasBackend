import fastapi as fastapi
import typing as typing
import anndata as anndata
import numpy as numpy
import pandas as pandas

from app.plotting import generate_spatial_plot
from app.services.sample_service import get_sample_data, get_all_samples
from app.core.config import Settings
from app.core.dependencies import get_settings
from app.models import SampleResponse

router = fastapi.APIRouter()

@router.get("/samples", response_model=typing.List[SampleResponse])
async def get_samples(request: fastapi.Request):
    api_samples = [
        SampleResponse(id=sample_id, **sample_data)
        for sample_id, sample_data_list in get_all_samples().items()
        for sample_data in sample_data_list
    ]
    for sample in api_samples:
        sample.add_links(str(request.base_url))
    return api_samples


@router.get("/samples/{sample_id}/{condition}/cell_type")
async def get_sample_image(
    sample_id: str,
    condition: str,
    settings: Settings = fastapi.Depends(get_settings),
):
    sample_file_name = get_sample_data(sample_id, condition)
    if sample_file_name is not None:
        file_path = settings.IMAGE_STORAGE_PATH / f"{sample_file_name['cell_types_image']}"
        return fastapi.responses.FileResponse(
            path=file_path,
            media_type="image/png",
            headers={
                "Cache-Control": "public, max-age=3600",  # Cache for 1 hour
                "X-Sample-ID": sample_id,
            }
        )
    else:
        raise fastapi.HTTPException(
            status_code=404,
            detail=f"Sample not found {sample_id}, condition {condition}"
        )


@router.get("/samples/{sample_id}/{condition}/genes")
async def get_all_genes(
    sample_id: str,
    condition: str,
    limit: int = 100,
    settings: Settings = fastapi.Depends(get_settings), ):
    if limit > 500:
        limit = 500

    sample_file_name = get_sample_data(sample_id, condition)
    if sample_file_name is not None:
        file_path = settings.IMAGE_STORAGE_PATH / f"{sample_file_name['data']}"
        adata = anndata.read_h5ad(file_path)
        if hasattr(adata.X, 'toarray'):  # Handle sparse matrices
            expression_matrix = adata.X.toarray()
        else:
            expression_matrix = adata.X

        # Calculate mean expression per gene (across all cells/spots)
        mean_expression = numpy.mean(expression_matrix, axis=0)
        gene_expression_df = pandas.DataFrame({
            'gene': adata.var.index,
            'mean_expression': mean_expression
        })

        # Sort by mean expression (descending - highest expression first)
        gene_expression_df = gene_expression_df.sort_values('mean_expression',
                                                            ascending=False)
        ordered_genes = gene_expression_df['gene'][0:limit].tolist()
        return fastapi.responses.JSONResponse(
            ordered_genes,
            headers={
                "Content-Type": "application/json",
                "Cache-Control": "public, max-age=3600",  # Cache for 1 hour
                "X-Sample-ID": sample_id,
            }
        )
    else:
        raise fastapi.HTTPException(
            status_code=404,
            detail=f"Sample not found {sample_id}, condition {condition}"
        )


@router.get("/samples/{sample_id}/{condition}/genes/{gene}")
async def get_gene_expression(
    sample_id: str,
    condition: str,
    gene: str,
    cmap: str = 'inferno',
    alpha: float = 0.5,
    spot_size: float = 1,
    dpi: int = 120,
    settings: Settings = fastapi.Depends(get_settings), ):
    sample_file_name = get_sample_data(sample_id, condition)
    if sample_file_name is not None:
        file_path = settings.IMAGE_STORAGE_PATH / f"{sample_file_name['data']}"
        adata = anndata.read_h5ad(file_path)
        image_buffer = generate_spatial_plot(adata, gene, cmap, alpha, spot_size, dpi)
        image_buffer.seek(0)
        return fastapi.responses.StreamingResponse(
            image_buffer,
            media_type="image/png",
            headers={
                "Cache-Control": "public, max-age=3600",  # Cache for 1 hour
                "X-Sample-ID": sample_id,
            }
        )
    else:
        raise fastapi.HTTPException(
            status_code=404,
            detail=f"Sample not found {sample_id}, condition {condition}"
        )
