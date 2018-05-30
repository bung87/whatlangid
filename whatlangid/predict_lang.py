from __future__ import division, unicode_literals
from fastText import load_model
from os import path
import re
import sys
import collections
import langid
from .exceptions import InsufficientError

if sys.version_info[0] >= 3:
    unicode = str

MODEL_FILE = path.join(path.dirname(__file__), 'model', 'lid.176.ftz')


def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


class WhatLangId(object):
    def __init__(self):
        langid.classify("")  # force initialize
        self.model_file = MODEL_FILE
        self.model = load_model(MODEL_FILE)
        self.unknown = None

    def _clean_up(self, txt):
        txt = re.sub(r"\b\d+\b", "", txt)
        self.txt = txt
        return self.txt

    def _predict_pro(self, x):
        labels, pros = self.model.predict(x)
        labels = flatten(labels)
        pros = flatten(pros)
        x = map(lambda x: x.replace("__label__", ""), labels)
        return list(zip(x, pros))

    def _predict(self, text):
        labels, _ = self.model.predict(text)
        labels = flatten(labels)

        langs_map = map(lambda x: x.replace("__label__", ""), labels)
        if isinstance(text, collections.Iterable) and not isinstance(text, (str, bytes)):
            results = [x if x != "ja" else langid.classify(text[i])[0] for i, x in enumerate(langs_map)]
        else:
            results = [x if x != "ja" else langid.classify(text)[0] for x in langs_map]
        return results

    def get_langs(self):
        return self.model.get_labels()

    def predict_lang(self, inp):
        if isinstance(inp, unicode):
            cleaned_txt = self._clean_up(inp)
            if cleaned_txt == "":
                raise InsufficientError("Not enough text to predict language")
            pred = self._predict(cleaned_txt)
            if len(pred) == 0:
                return self.unknown

            return pred[0]
        else:
            batch = [self._clean_up(i) for i in inp]
            return list(flatten(self._predict(batch)))

    def predict_pro(self, inp):
        if isinstance(inp, unicode):
            inp = self._clean_up(inp)
            return self._predict_pro([inp])
        return self._predict_pro(inp)
