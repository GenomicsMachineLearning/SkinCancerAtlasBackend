from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

from app.platform import Platform


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str

_CONDITION = Literal["melanoma", "bcc", "scc"]

class SampleResponse(BaseModel):
    id: str
    condition: _CONDITION
    platform: Platform
    cell_types_image: Optional[str] = None
    h_and_e_image: Optional[str] = None
    data: str
    links: Optional[dict] = None

    def add_links(self, base_url: str):
        self.links = {
            "self": f"{base_url}samples/{self.id}",
            "cell_type": f"{base_url}samples/{self.id}/{self.condition}/cell_type",
            "h_and_e": f"{base_url}samples/{self.id}/{self.condition}/h_and_e",
            "gene_expression": f"{base_url}samples/{self.id}/{self.condition}/genes",
        }