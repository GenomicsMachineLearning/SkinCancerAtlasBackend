from typing import Dict

from app.models import SampleResponse, Sample


SAMPLES = {
    "6767": [
        {
            "condition": "melanoma",
            "platform": "visium",
            "data": "6767_Mel_stlearn.h5ad",
            "lr": "6767_Mel_lr_scores.h5ad",
            "render_params": {
                "spot_size": "125",
                "flip_y": "true",
            },
        }
    ],
    "66487": [
        {
            "condition": "melanoma",
            "platform": "visium",
            "data": "66487_Mel_stlearn.h5ad",
            "lr": "66487_Mel_lr_scores.h5ad",
            "render_params": {
                "spot_size": "125",
                "flip_y": "true"
            },
        },
        {
            "condition": "melanoma",
            "platform": "cosmx",
            "data": "66487-1A_cutoff50_cosmx_clean.h5ad",
            "lr": "66487-1A_cutoff50_cosmx_lr_scores.h5ad",
            "render_params": {
                "spot_size": 50,
                "dpi": 150,
            }
        }
    ],
    "21031": [
        {
            "condition": "melanoma",
            "platform": "visium",
            "data": "21031_Mel_stlearn.h5ad",
            "lr": "21031_Mel_lr_scores.h5ad",
            "render_params": {
                "spot_size": "125",
            },
        }
    ],
    "48974": [
        {
            "condition": "melanoma",
            "platform": "visium",
            "data": "48974_Mel_stlearn.h5ad",
            "lr": "48974_Mel_lr_scores.had",
            "render_params": {
                "spot_size": "125",
            },
        }
    ],
    "B18": [
        {
            "condition": "scc",
            "platform": "visium",
            "data": "B18_SCC_stlearn.h5ad",
            "lr": "B18_SCC_lr_scores.h5ad",
            "render_params": {
                "spot_size": "20",
            },
        },
        {
            "condition": "bcc",
            "platform": "visium",
            "data": "B18_BCC_stlearn.h5ad",
            "lr": "B18_BCC_lr_scores.h5ad",
            "render_params": {
                "spot_size": "75",
            },
        },
        {
            "condition": "scc",
            "platform": "cosmx",
            "data": "B18_SCC_cutoff50_cosmx_clean.h5ad",
            "lr": "B18_SCC_cutoff50_cosmx_lr_scores.h5ad",
            "render_params": {
                "spot_size": 50,
                "dpi": 150,
            }
        },
        {
            "condition": "bcc",
            "platform": "cosmx",
            "data": "B18_BCC_cutoff50_cosmx_clean.h5ad",
            "lr": "B18_BCC_cutoff50_cosmx_lr_scores.h5ad",
            "render_params": {
                "spot_size": 50,
                "dpi": 150,
            }
        }
    ],
    "E15": [
        {
            "condition": "bcc",
            "platform": "visium",
            "data": "E15_BCC_stlearn.h5ad",
            "lr": "E15_BCC_lr_scores.h5ad",
        },
        {
            "condition": "scc",
            "platform": "visium",
            "data": "E15_SCC_stlearn.h5ad",
            "lr": "E15_SCC_lr_scores.h5ad",
        }
    ],
    "F21": [
        {
            "condition": "bcc",
            "platform": "visium",
            "data": "F21_BCC_stlearn.h5ad",
            "lr": "F21_BCC_lr_scores.h5ad",
        },
        {
            "condition": "scc",
            "platform": "visium",
            "data": "F21_SCC_stlearn.h5ad",
            "lr": "F21_SCC_lr_scores.h5ad",
        },
    ],
    "6475-07FC": [
        {
            "condition": "melanoma",
            "platform": "xenium",
            "data": "6475-07FC_labeled_xenium.h5ad",
            "lr": "6475-07FC_labeled_xenium_lr_scores.h5ad",
            "render_params": {
                "spot_size": 50,
                "dpi": 150,
            }
        }
    ],
    "9474-06BR": [
        {
            "condition": "melanoma",
            "platform": "xenium",
            "data": "9474-06BR_labeled_xenium.h5ad",
            "lr": "9474-06BR_labeled_xenium_lr_scores.h5ad",
            "render_params": {
                "flip_y": "true",
                "spot_size": 50,
                "dpi": 150,
            },
        }
    ],
    "23346-10SP": [
        {
            "condition": "melanoma",
            "platform": "xenium",
            "data": "23346-10SP_labeled_xenium.h5ad",
            "lr": "23346-10SP_labeled_xenium_lr_scores.h5ad",
            "render_params": {
                "flip_y": "true",
                "spot_size": 50,
                "dpi": 150,
            },
        }
    ],
    "30037-07BR": [
        {
            "condition": "melanoma",
            "platform": "xenium",
            "data": "30037-07BR_labeled_xenium.h5ad",
            "lr": "30037-07BR_labeled_xenium_lr_scores.h5ad",
            "render_params": {
                "flip_y": "true",
                "spot_size": 50,
                "dpi": 150,
            },
        },
    ],
    "98594-09PY": [
        {
            "condition": "melanoma",
            "platform": "xenium",
            "data": "98594-09PY_labeled_xenium.h5ad",
            "lr": "98594-09PY_labeled_xenium_lr_scores.h5ad",
            "render_params": {
                "flip_y": "true",
                "spot_size": 50,
                "dpi": 150,
            },
        }
    ],
    "48974-2B": [
        {
            "condition": "melanoma",
            "platform": "cosmx",
            "data": "48974-2B_cutoff50_cosmx_clean.h5ad",
            "lr": "48974-2B_cutoff50_cosmx_lr_scores.h5ad",
            "render_params": {
                "spot_size": 50,
                "dpi": 150,
            }
        }
    ],
    "6747": [
        {
            "condition": "melanoma",
            "platform": "cosmx",
            "data": "6747-085P_cutoff50_cosmx_clean.h5ad",
            "lr": "6747-085P_cutoff50_cosmx_lr_scores.h5ad",
            "render_params": {
                "spot_size": 50,
                "dpi": 150,
            }
        }
    ],
    "P13": [
        {
            "condition": "scc",
            "platform": "cosmx",
            "data": "P13_cutoff50_cosmx_clean.h5ad",
            "lr": "P13_cutoff50_cosmx_lr_scores.h5ad",
            "render_params": {
                "spot_size": 50,
                "dpi": 150,
            }
        }
    ],
    "P30": [
        {
            "condition": "scc",
            "platform": "cosmx",
            "data": "P30_cutoff50_cosmx_clean.h5ad",
            "lr": "P30_cutoff50_cosmx_lr_scores.h5ad",
            "render_params": {
                "spot_size": 50,
                "dpi": 150,
            }
        }
    ],
}

def get_sample_data(sample_id: str, condition: str, platform: str) -> Sample | None:
    if sample_id in SAMPLES:
        items_from_sample = SAMPLES[sample_id]
        sample_file_names = [item for item in items_from_sample if
                             item["condition"] == condition and item["platform"] == platform]
        if sample_file_names:
            sample_dict = sample_file_names[0]
            return Sample(id=sample_id, **sample_dict)
    else:
        return None


def get_all_samples() -> Dict:
    return SAMPLES
