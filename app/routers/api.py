import fastapi as fastapi
from typing import List

from app.models import SampleResponse

router = fastapi.APIRouter()

samples = {
    "21031": [
        {
            "condition": "Melanoma",
            "platform": "Visium",
            "cell_types_image": "Vis_21031_Mel_stlearn.png",
            "h_and_e_image": "Vis_21031_Mel_stlearn.png",
            "data": "21031_Mel_stlearn.h5ad",
        }
    ],
    "B18": [
        {
            "condition": "SCC",
            "platform": "Visium",
            "cell_types_image": "Vis_B18_SCC_stlearn.png",
            "h_and_e_image": "Vis_B18_SCC_stlearn.png",
            "data": "B18_BCC_stlearn.h5ad",
        },
    ],
    "F21": [
        {
            "condition": "BCC",
            "platform": "Visium",
            "cell_types_image": "Vis_B18_SCC_stlearn.png",
            "h_and_e_image": "Vis_B18_SCC_stlearn.png",
            "data": "B18_BCC_stlearn.h5ad",
        }
    ],
    "E15": [
        {
            "condition": "BCC",
            "platform": "Visium",
            "cell_types_image": "Vis_E15_BCC_stlearn.png",
            "h_and_e_image": "Vis_E15_BCC_stlearn.png",
            "data": "E15_BCC_stlearn.h5ad",
        },
        {
            "condition": "SCC",
            "platform": "Visium",
            "cell_types_image": "Vis_E15_SCC_stlearn.png",
            "h_and_e_image": "Vis_E15_SCC_stlearn.png",
            "data": "E15_SCC_stlearn.h5ad",
        }
    ]
}


@router.get("/samples", response_model=List[SampleResponse])
async def get_samples(request: fastapi.Request):
    api_samples = [
        SampleResponse(id = sample_id, **sample_data)
        for sample_id, sample_data_list in samples.items()
        for sample_data in sample_data_list
    ]
    for sample in api_samples:
        sample.add_links(str(request.base_url))
    return api_samples
