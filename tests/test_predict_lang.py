# coding=utf-8
from __future__ import division, unicode_literals
from whatlangid.predict_lang import WhatLangId
from os import path
import unittest


class WhatLangIdTest(unittest.TestCase):

    def setUp(self):
        self.wtl = WhatLangId()

    def test_model_present(self):
        self.assertEqual(path.isfile(self.wtl.model_file), True)

    def test_english(self):
        pred = self.wtl.predict_lang("This is an English sentence")
        self.assertEqual(pred, 'en')

    def test_english_pro(self):
        pred = self.wtl.predict_pro("This is an English sentence")
        self.assertEqual(pred, [('en', 0.9606998562812805)])

    def test_batch(self):
        pred = self.wtl.predict_lang(["English sentence", "അമ്മ"])
        self.assertEqual(pred, ['en', 'ml'])

    def test_batch_pro(self):
        pred = self.wtl.predict_pro(["English sentence", "അമ്മ"])
        self.assertListEqual(pred, [('en', 0.8848170638084412), ('ml', 0.9535570740699768)])

    def test_num_langs(self):
        self.assertEqual(len(self.wtl.get_langs()), 176)

    def test_emoji(self):
        pred = self.wtl.predict_lang("👿👿👿👿👿")
        self.assertEqual(pred, "en")

    # def test_huoxingwen(self):
    #     pred = self.wtl.predict_lang("焱暒妏")
    #     self.assertEqual(pred, "zh")

    # def test_orz(self):
    #     pred = self.wtl.predict_lang("Orz")
    #     self.assertEqual(pred, "en")

    #
    # def test_unknown(self):
    #     pred = self.wtl.predict_lang("asdfs")
    #     self.assertEqual(pred, None)

    # def test_batch_with_unknown(self):
    #     pred = self.wtl.predict_lang(["English sentence", "അമ്മ", "asdfs"])
    #     self.assertEqual(pred, ['en', 'ml', None])

    def test_unicode_input(self):
        pred = self.wtl.predict_lang(u"nike running shoes")
        self.assertEqual(pred, 'en')

    def test_chinese(self):
        pred = self.wtl.predict_lang(["权威数据：大纪元新唐人成海外中文媒体巨人"])
        self.assertEqual(pred, ["zh"])


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(WhatLangIdTest))
    return suite


if __name__ == '__main__':
    unittest.main()
