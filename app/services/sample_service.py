from typing import Dict, List, Optional

from app.models import SampleResponse

SAMPLES = {
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
        },
        {
            "condition": "melanoma",
            "platform": "cosmx",
            "data": "66487-1A_cutoff50_cosmx_clean.h5ad",
        }
    ],
    "21031": [
        {
            "condition": "melanoma",
            "platform": "visium",
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
    "B18": [
        {
            "condition": "scc",
            "platform": "visium",
            "data": "B18_SCC_stlearn.h5ad",
        },
        {
            "condition": "bcc",
            "platform": "visium",
            "data": "B18_BCC_stlearn.h5ad",
        },
        {
            "condition": "scc",
            "platform": "cosmx",
            "data": "B18_SCC_cutoff50_cosmx_clean.h5ad",
        },
        {
            "condition": "bcc",
            "platform": "cosmx",
            "data": "B18_BCC_cutoff50_cosmx_clean.h5ad",
        }
    ],
    "E15": [
        {
            "condition": "bcc",
            "platform": "visium",
            "data": "E15_BCC_stlearn.h5ad",
        },
        {
            "condition": "scc",
            "platform": "visium",
            "data": "E15_SCC_stlearn.h5ad",
        }
    ],
    "F21": [
        {
            "condition": "bcc",
            "platform": "visium",
            "data": "F21_BCC_stlearn.h5ad",
        },
        {
            "condition": "scc",
            "platform": "visium",
            "data": "F21_SCC_stlearn.h5ad",
        },
    ],
    "6475-07FC": [
        {
            "condition": "melanoma",
            "platform": "xenium",
            "data": "6475-07FC_labeled_xenium.h5ad",
        }
    ],
    "9474-06BR": [
        {
            "condition": "melanoma",
            "platform": "xenium",
            "data": "9474-06BR_labeled_xenium.h5ad",
        }
    ],
    "23346-10SP": [
        {
            "condition": "melanoma",
            "platform": "xenium",
            "data": "23346-10SP_labeled_xenium.h5ad",
        }
    ],
    "30037-07BR": [
        {
            "condition": "melanoma",
            "platform": "xenium",
            "data": "30037-07BR_labeled_xenium.h5ad",
        },
    ],
    "98594-09PY": [
        {
            "condition": "melanoma",
            "platform": "xenium",
            "data": "98594-09PY_labeled_xenium.h5ad",
        }
    ],
    "48974-2B": [
        {
            "condition": "melanoma",
            "platform": "cosmx",
            "data": "48974-2B_cutoff50_cosmx_clean.h5ad",
        }
    ],
    "67667": [
        {
            "condition": "melanoma",
            "platform": "cosmx",
            "data": "6747-085P_cutoff50_cosmx_clean.h5ad",
        }
    ],
    "P13": [
        {
            "condition": "scc",
            "platform": "cosmx",
            "data": "P13_cutoff50_cosmx_clean.h5ad",
        }
    ],
    "P30": [
        {
            "condition": "scc",
            "platform": "cosmx",
            "data": "P30_cutoff50_cosmx_clean.h5ad",
        }
    ],
    "D12": [
        {
            "condition": "bcc",
            "platform": "cosmx",
            "data": "D12_cutoff50_cosmx_stlearn.h5ad",
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
