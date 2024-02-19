from pydantic import BaseModel


class DataParsOrbiter(BaseModel):
    total: int = 0


class OrbiterPars(BaseModel):
    data: DataParsOrbiter


class AltLayerPars(BaseModel):
    address: str
    amount: str


class ZetaPars(BaseModel):
    totalXp: int = None
