from inspect import Parameter

import fastapi as fastapi
import typing as typing
import anndata as anndata
import numpy as numpy
import pandas as pandas

import app as app
import app.plotting as app_plotting
from app.expression_measure import ExpressionMeasure
from app.core.config import Settings
from app.core.dependencies import get_settings
from app.models import ScRnaSeqResponse, ScRnaSeq
from app.services.scrnaseq_service import get_all_scrnaseq, get_scrnaseq_data

router = fastapi.APIRouter()

@router.get("/scrnaseq", response_model=typing.List[ScRnaSeqResponse])
async def get_scrnaseq(request: fastapi.Request):
    api_scrnaseqs = [
        ScRnaSeq(**scrnaseq_data)
        for scrnaseq_data in get_all_scrnaseq()
    ]
    for rnaseq in api_scrnaseqs:
        rnaseq.add_links(str(request.base_url))
    return api_scrnaseqs


@router.get("/scrnaseq/{scrnaseq_id}/cell_type")
async def get_cell_types(
    scrnaseq_id: str,
    cmap: str = 'inferno',
    spot_size: float = 5,
    legend_spot_size: float = 80,
    dpi: int = 100,
    level: str = 'Level1',
    settings: Settings = fastapi.Depends(get_settings), ):
    scrnaseq = get_scrnaseq_data(scrnaseq_id)
    if scrnaseq is not None:
        file_path = settings.DATA_STORAGE_PATH / f"{scrnaseq.data}"
        adata = anndata.read_h5ad(file_path)
        print(f"Read {file_path}")
        image_buffer = app_plotting.generate_umap(adata, cmap, spot_size,
                                                  legend_spot_size, dpi, level)
        image_buffer.seek(0)
        return fastapi.responses.StreamingResponse(
            image_buffer,
            media_type="image/png",
            headers={
                "Cache-Control": "public, max-age=3600",  # Cache for 1 hour
                "X-ScRnaSeq-ID": scrnaseq_id,
            }
        )
    else:
        raise fastapi.HTTPException(
            status_code=404,
            detail=f"ScRnaSeq not found {scrnaseq_id}"
        )


@router.get("/scrnaseq/{scrnaseq_id}/genes")
async def get_all_genes(
    scrnaseq_id: str,
    measure: ExpressionMeasure = "total",
    limit: int = 100,
    settings: Settings = fastapi.Depends(get_settings), ):
    if limit > 500:
        limit = 500

    scrnaseq = get_scrnaseq_data(scrnaseq_id)
    if scrnaseq is not None:
        file_path = settings.DATA_STORAGE_PATH / f"{scrnaseq.data}"
        adata = anndata.read_h5ad(file_path)
        ordered_genes = ExpressionMeasure.apply_measure(adata, measure,
                                                         adata.var_names, limit)
        return fastapi.responses.JSONResponse(
            ordered_genes,
            headers={
                "Content-Type": "application/json",
                "Cache-Control": "public, max-age=3600",  # Cache for 1 hour
                "X-Sample-ID": scrnaseq_id,
            }
        )
    else:
        raise fastapi.HTTPException(
            status_code=404,
            detail=f"ScRnaSeq not found {scrnaseq_id}"
        )

@router.get("/scrnaseq/{scrnaseq_id}/genes/{gene}")
async def get_gene_expression(
    scrnaseq_id: str,
    gene: str,
    cmap: str = 'inferno',
    spot_size: float = 5,
    legend_spot_size: float = 80,
    dpi: int = 100,
    settings: Settings = fastapi.Depends(get_settings), ):

    scrnaseq = get_scrnaseq_data(scrnaseq_id)
    if scrnaseq is not None:
        file_path = settings.DATA_STORAGE_PATH / f"{scrnaseq.data}"
        adata = anndata.read_h5ad(file_path)
        gene_idx = adata.var_names.get_loc(gene)
        expr = adata.X.toarray()[:, gene_idx]

        image_buffer = app_plotting.generate_umap(adata, cmap, spot_size,
                                                  legend_spot_size, dpi, gene, expr)
        image_buffer.seek(0)
        return fastapi.responses.StreamingResponse(
            image_buffer,
            media_type="image/png",
            headers={
                "Cache-Control": "public, max-age=3600",  # Cache for 1 hour
                "X-ScRnaSeq-ID": scrnaseq_id,
            }
        )
    else:
        raise fastapi.HTTPException(
            status_code=404,
            detail=f"ScRnaSeq not found {scrnaseq_id}"
        )
