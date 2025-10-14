from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

from app.platform import Platform


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str


_CONDITION = Literal["melanoma", "bcc", "scc"]


class Sample(BaseModel):
    id: str
    condition: _CONDITION
    platform: Platform
    data: str
    lr: Optional[str] = None
    cell_types_image: Optional[str] = None
    h_and_e_image: Optional[str] = None
    render_params: dict = None
    links: Optional[dict] = None


class SampleResponse(BaseModel):
    id: str
    condition: _CONDITION
    platform: Platform
    render_params: dict = None
    lr: Optional[str] = None
    links: Optional[dict] = None

    def add_links(self, base_url: str):
        self.links = {
            "self": f"{base_url}samples/{self.id}",
            "cell_type": f"{base_url}samples/{self.id}/{self.condition}/{self.platform}/cell_type",
            "h_and_e": f"{base_url}samples/{self.id}/{self.condition}/h_and_e",
            "gene_expression": f"{base_url}samples/{self.id}/{self.condition}/{self.platform}/genes",
        }
        if self.lr is not None:
            self.links[
                'lrs'] = f"{base_url}samples/{self.id}/{self.condition}/{self.platform}/lrs"
        del self.lr


class ScRnaSeq(BaseModel):
    id: str
    condition: str
    data: str
    links: Optional[dict] = None

    def add_links(self, base_url: str):
        self.links = {
            "cell_type": f"{base_url}scrnaseq/{self.id}/cell_type",
            "list_cell_types": f"{base_url}scrnaseq/{self.id}/cell_types",
        }


class ScRnaSeqResponse(BaseModel):
    id: str
    condition: str
    links: Optional[dict] = None


class ScRnaSeqCellTypesResponse(BaseModel):
    id: str
    cell_type: str
    links: Optional[dict] = None

    def add_links(self, base_url: str):
        self.links = {
            "list_genes": f"{base_url}scrnaseq/{self.id}/{self.cell_type}/genes",
        }
