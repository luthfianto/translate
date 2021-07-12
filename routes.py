from fastapi import FastAPI
from typing import List
from main import en_id_translator, id_en_translator

from pydantic import BaseModel


class Item(BaseModel):
    inputs: List[str]
    langs: List[str] = ["en-id", "id-en"]


app = FastAPI()


@app.post("/batch_translate")
async def batch_translate(item: Item):
    return {
        "en-id": en_id_translator.batch_translate(item.inputs),
        "id-en": id_en_translator.batch_translate(item.inputs),
    }
