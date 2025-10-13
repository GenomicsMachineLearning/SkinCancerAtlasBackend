from inspect import Parameter

import fastapi as fastapi
import typing as typing
import numpy as numpy
import anndata as anndata
import pandas as pandas

from app.plotting import generate_spatial_plot, generate_sample_cell_type_plot, \
    generate_cell_type_plot, generate_umap
from app.expression_measure import ExpressionMeasure
from app.services.sample_service import get_sample_data, get_all_samples
from app.core.config import Settings
from app.core.dependencies import get_settings
from app.models import SampleResponse, ScRnaSeqResponse, ScRnaSeq
from app.services.scrnaseq_service import get_all_scrnaseq, get_scrnaseq_data

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

@router.get("/samples/{sample_id}/{condition}/h_and_e")
async def get_h_and_e_image(
    sample_id: str,
    condition: str,
    settings: Settings = fastapi.Depends(get_settings),
):
    sample = get_sample_data(sample_id, condition)
    if sample is not None:
        file_path = settings.DATA_STORAGE_PATH / f"{sample.h_and_e_image}"
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


@router.get("/samples/{sample_id}/{condition}/{platform}/cell_type")
async def get_cell_types(
    sample_id: str,
    condition: str,
    platform: str,
    cmap: str = 'inferno',
    alpha: float = 0.5,
    spot_size: float = 20,
    library_id: str | None = None,
    legend_spot_size: float = 1,
    dpi: int = 120,
    flip_x: bool = False,
    flip_y: bool = False,
    settings: Settings = fastapi.Depends(get_settings), ):
    sample = get_sample_data(sample_id, condition, platform)
    if sample is not None:
        file_path = settings.DATA_STORAGE_PATH / f"{sample.data}"
        adata = anndata.read_h5ad(file_path)
        image_buffer = generate_sample_cell_type_plot(sample, adata, cmap, alpha,
                                               spot_size, library_id, legend_spot_size,
                                               dpi, flip_x, flip_y)
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

@router.get("/samples/{sample_id}/{condition}/{platform}/genes")
async def get_all_genes(
    sample_id: str,
    condition: str,
    platform: str,
    measure: ExpressionMeasure = "mean",
    limit: int = 100,
    settings: Settings = fastapi.Depends(get_settings), ):
    if limit > 500:
        limit = 500

    sample = get_sample_data(sample_id, condition, platform)
    if sample is not None:
        file_path = settings.DATA_STORAGE_PATH / f"{sample.data}"
        adata = anndata.read_h5ad(file_path)
        ordered_genes = ExpressionMeasure.apply_measure_adata(adata, measure,
                                                              adata.var.index, limit)
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

@router.get("/samples/{sample_id}/{condition}/{platform}/lrs")
async def get_all_genes(
    sample_id: str,
    condition: str,
    platform: str,
    measure: ExpressionMeasure = "total",
    limit: int = 100,
    settings: Settings = fastapi.Depends(get_settings), ):
    if limit > 500:
        limit = 500

    sample = get_sample_data(sample_id, condition, platform)
    if sample is not None:
        file_path = settings.DATA_STORAGE_PATH / f"{sample.lr}"
        p = pandas.read_hdf(file_path)
        ordered_lrs = ExpressionMeasure.apply_measure(p.to_numpy(), measure, p.columns, limit)
        return fastapi.responses.JSONResponse(
            ordered_lrs,
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

@router.get("/samples/{sample_id}/{condition}/{platform}/genes/{gene}")
async def get_gene_expression(
    sample_id: str,
    condition: str,
    platform: str,
    gene: str,
    cmap: str = 'inferno',
    alpha: float = 0.5,
    spot_size: float = 20,
    library_id: str | None = None,
    legend_spot_size: float = 1,
    dpi: int = 120,
    flip_x: bool = False,
    flip_y: bool = False,
    settings: Settings = fastapi.Depends(get_settings), ):
    sample = get_sample_data(sample_id, condition, platform)
    if sample is not None:
        file_path = settings.DATA_STORAGE_PATH / f"{sample.data}"
        adata = anndata.read_h5ad(file_path)

        image_buffer = generate_spatial_plot(adata, gene, cmap, alpha,
                                             library_id, spot_size, legend_spot_size,
                                             dpi, flip_x, flip_y)
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

@router.get("/samples/{sample_id}/{condition}/{platform}/lrs/{lr}")
async def get_all_genes(
    sample_id: str,
    condition: str,
    platform: str,
    lr: str,
    cmap: str = 'inferno',
    alpha: float = 0.5,
    spot_size: float = 20,
    library_id: str | None = None,
    legend_spot_size: float = 1,
    dpi: int = 120,
    flip_x: bool = False,
    flip_y: bool = False,
    settings: Settings = fastapi.Depends(get_settings), ):
    sample = get_sample_data(sample_id, condition, platform)
    if sample is not None:
        lr_file_path = settings.DATA_STORAGE_PATH / f"{sample.lr}"
        gene_file_path = settings.DATA_STORAGE_PATH / f"{sample.data}"
        p = pandas.read_hdf(lr_file_path)
        adata = anndata.read_h5ad(gene_file_path)
        adata.obs[lr] = p[lr].values

        image_buffer = generate_spatial_plot(adata, lr, cmap, alpha,
                                             library_id, spot_size, legend_spot_size,
                                             dpi, flip_x, flip_y)
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
