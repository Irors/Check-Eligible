from pydantic import BaseModel


class AltLayerPars(BaseModel):
    address: str
    amount: str

