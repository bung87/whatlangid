# coding=utf-8
from __future__ import division, unicode_literals

import langid
from whatthelang import WhatTheLang

wtl = WhatTheLang()

def test(s):
    s = s
    print(s)
    assert langid.classify(s)[0] == wtl.predict_lang(s), "langid:%s whatthelang:%s" % (
    langid.classify(s)[0], wtl.predict_lang(s))

kr = "CIDA 장애청년 고용 워크숍"
test(kr)

de = "Das ist ein hässliches Auto."
test(de)

fr = "C'est une voiture terribles."
test(fr)

s = "東協10國＋印度 來台觀光給方便"
test(s)

# s="权威数据：大纪元新唐人成海外中文媒体巨人"
# test(s) # langid:zh whatthelang:ja

s = "日本人僧侶ら、台湾の寺院で昭和天皇ゆかりの文化財拝観  約90年前に結んだ縁で"
test(s)

s = "-VW ‘made several devices’ to cheat tests-"
test(s)

# s = "Toronto, London Among Riskiest Housing Bubble Cities, UBS Says"
# test(s) #langid:it whatthelang:en

# s="Former US first lady Nancy Reagan dies at 94"
# test(s) # langid:id whatthelang:en
