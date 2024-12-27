from typing import Optional
from pydantic import BaseModel

class ArtigoSchemaBase(BaseModel):
    titulo: str
    descricao: str  # Corrected spelling
    url_fonte: str

class ArtigoSchemaCreate(ArtigoSchemaBase):
    pass  # Exclude 'usuario_id' as it's set server-side

class ArtigoSchema(ArtigoSchemaBase):
    id: int
    usuario_id: int

    class Config:
        orm_mode = True