from typing import Dict

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

def get_all_scrnaseq() -> []:
    return SCRNA_SEQ