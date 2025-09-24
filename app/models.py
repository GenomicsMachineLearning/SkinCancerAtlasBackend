from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str

_CONDITION = Literal["Melanoma", "BCC", "SCC"]
_PLATFORM = Literal["Visium", "Xenium", "CosMX"]

class SampleResponse(BaseModel):
    id: str
    condition: _CONDITION
    platform: _PLATFORM
    cell_types_image: str
    h_and_e_image: str
    data: str
    links: Optional[dict] = None

    def add_links(self, base_url: str):
        self.links = {
            "self": f"{base_url}samples/{self.id}",
            "cell_type": f"{base_url}samples/{self.id}/cell_type",
            "h_and_e": f"{base_url}samples/{self.id}/h_and_e",
            "gene_expression": f"{base_url}samples/{self.id}?gene=gene_id",
        }