from typing import List
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class OfflineTranslator:
    def __init__(self, tokenizer, model):
        self._tokenizer = tokenizer
        self._model = model

    def translate(self, s: List[str]):
        batch = self._tokenizer(s, return_tensors="pt")
        gen = self._model.generate(**batch)
        r = self._tokenizer.batch_decode(gen, skip_special_tokens=True)
        return r[0].replace("▁", " ")

    def batch_translate(self, s: List[str]):
        batch = self._tokenizer(s, return_tensors="pt", padding=True)
        translated = self._model.generate(**batch)
        return self._tokenizer.batch_decode(translated, skip_special_tokens=True)


tokenizer_en_id = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-id")
model_en_id = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-id")

tokenizer_id_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-id-en")
model_id_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-id-en")

en_id_translator = OfflineTranslator(tokenizer_en_id, model_en_id)
id_en_translator = OfflineTranslator(tokenizer_id_en, model_id_en)
