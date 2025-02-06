from pydantic import BaseModel


class QuadraCreate(BaseModel):
    nome: str
    localizacao: str
    tipo: str 

    class Config:
        from_attributes = True
