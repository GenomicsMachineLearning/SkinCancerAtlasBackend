from typing import Dict, List, Optional

from app.models import SampleResponse

SAMPLES = {
    "21031": [
        {
            "condition": "melanoma",
            "platform": "visium",
            "cell_types_image": "Vis_21031_Mel_stlearn.png",
            "h_and_e_image": "Vis_21031_Mel_stlearn.png",
            "data": "21031_Mel_stlearn.h5ad",
        }
    ],
    "48974": [
        {
            "condition": "melanoma",
            "platform": "visium",
            "data": "48974_Mel_stlearn.h5ad",
        }
    ],
    "6767": [
        {
            "condition": "melanoma",
            "platform": "visium",
            "data": "6767_Mel_stlearn.h5ad",
        }
    ],
    "66487": [
        {
            "condition": "melanoma",
            "platform": "visium",
            "data": "66487_Mel_stlearn.h5ad",
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

def get_sample_data(sample_id: str, condition: str) -> SampleResponse | None:
    if sample_id in SAMPLES:
        items_from_sample = SAMPLES[sample_id]
        sample_file_names = [item for item in items_from_sample if
                             item["condition"] == condition]
        if sample_file_names:
            sample_dict = sample_file_names[0]
            return SampleResponse(id=sample_id, **sample_dict)
    else:
        return None

def get_all_samples() -> Dict:
    return SAMPLES