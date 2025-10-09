from typing import Dict

from app.models import ScRnaSeq

SCRNA_SEQ = [
    {
        "id": "melanoma",
        "condition": "melanoma",
        "data": "Mel_full_object_final_Nov26_clean.h5ad",
    },
    {
        "id": "scc_bcc",
        "condition": "scc_bcc",
        "data": "SCC_full_object_final_Nov26_clean.h5ad",
    }
]

def get_scrnaseq_data(id: str) -> ScRnaSeq | None:
    all_matches = [d for d in SCRNA_SEQ if d['id'] == id]
    if len(all_matches) > 0:
        return ScRnaSeq(**all_matches[0])
    else:
        return None


def get_all_scrnaseq() -> []:
    return SCRNA_SEQ