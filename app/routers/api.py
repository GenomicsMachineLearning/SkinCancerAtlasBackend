import fastapi as fastapi
import typing as typing
import pathlib as pathlib

from fastapi.responses import FileResponse, Response
from fastapi import Depends, HTTPException

from app.core.config import Settings
from app.core.dependencies import get_settings
from app.models import SampleResponse

router = fastapi.APIRouter()

samples = {
    "21031": [
        {
            "condition": "melanoma",
            "platform": "visium",
            "cell_types_image": "Vis_21031_Mel_stlearn.png",
            "h_and_e_image": "Vis_21031_Mel_stlearn.png",
            "data": "21031_Mel_stlearn.h5ad",
        }
    ],
    "B18": [
        {
            "condition": "scc",
            "platform": "visium",
            "cell_types_image": "Vis_B18_SCC_stlearn.png",
            "h_and_e_image": "Vis_B18_SCC_stlearn.png",
            "data": "B18_BCC_stlearn.h5ad",
        },
    ],
    "F21": [
        {
            "condition": "bcc",
            "platform": "visium",
            "cell_types_image": "Vis_B18_SCC_stlearn.png",
            "h_and_e_image": "Vis_B18_SCC_stlearn.png",
            "data": "B18_BCC_stlearn.h5ad",
        }
    ],
    "E15": [
        {
            "condition": "bcc",
            "platform": "visium",
            "cell_types_image": "Vis_E15_BCC_stlearn.png",
            "h_and_e_image": "Vis_E15_BCC_stlearn.png",
            "data": "E15_BCC_stlearn.h5ad",
        },
        {
            "condition": "scc",
            "platform": "visium",
            "cell_types_image": "Vis_E15_SCC_stlearn.png",
            "h_and_e_image": "Vis_E15_SCC_stlearn.png",
            "data": "E15_SCC_stlearn.h5ad",
        }
    ]
}


@router.get("/samples", response_model=typing.List[SampleResponse])
async def get_samples(request: fastapi.Request):
    api_samples = [
        SampleResponse(id = sample_id, **sample_data)
        for sample_id, sample_data_list in samples.items()
        for sample_data in sample_data_list
    ]
    for sample in api_samples:
        sample.add_links(str(request.base_url))
    return api_samples


@router.get("/samples/{sample_id}/{condition}/cell_type")
async def get_sample_image(
    sample_id: str,
    condition: str,
    settings: Settings = Depends(get_settings),
):
    items_from_sample = samples[sample_id]
    sample_file_names = [item for item in items_from_sample if item["condition"] == condition]
    sample_file_name = sample_file_names[0]
    if sample_file_name is not None:
        file_path = settings.IMAGE_STORAGE_PATH / f"{sample_file_name['cell_types_image']}"
    if file_path is not None and not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"Image not found for sample {sample_id}"
        )

    return FileResponse(
        path=file_path,
        media_type="image/png",
        headers={
            "Cache-Control": "public, max-age=3600",  # Cache for 1 hour
            "X-Sample-ID": sample_id,
        }
    )