# whatlangid

[![Build Status](https://travis-ci.org/bung87/whatlangid.svg?branch=master)](https://travis-ci.org/bung87/whatlangid)  [![PyPI](https://img.shields.io/pypi/v/whatlangid.svg)](https://pypi.python.org/pypi/whatlangid)


This project is build on top of [whatthelang](https://github.com/indix/whatthelang) and [langid](https://github.com/saffsd/langid.py)

The dependency([pyfasttext](https://github.com/vrasneur/pyfasttext)) of **whatthelang** is not facebook official release.

This project depends on the official release [https://github.com/facebookresearch/fastText.git](https://github.com/facebookresearch/fastText.git)

The **fastText** for now is not release on pypi,so you need `--process-dependency-links` arg when using pip.

# Why this project exist?

see [issue_lang.py](issue_lang.py)

## Dependencies

The dependencies can be installed using the requirements.txt file:

```bash
$ pip install -r requirements.txt
```

## Install


```bash
$ pip install  --process-dependency-links git+https://github.com/bung87/whatlangid
```


## Basic Usage

Predicting Language using ``whatlangid``

```python
>>> from whatlangid import WhatLangId
>>> wtl = WhatLangId()
>>> wtl.predict_lang("Mother")
'en'
>>> wtl.predict_lang("தாய்")
'ta'
>>> wtl.predict_lang("അമ്മ")
'ml'
>>> wtl.predict_lang("पिता")
'hi'
>>> wtl.predict_pro(["English sentence", "അമ്മ"])
[('en', 0.8848170638084412), ('ml', 0.9535570740699768)]

```

Batch Prediction is also supported

```python
>>>wtl.predict_lang(["അമ്മ","पिता","teacher"])
['ml','hi','en']
```


## Supported Languages

Supports 176 languages . The ISO codes for the corresponding languages are as below.

```
af als am an ar arz as ast av az azb ba bar bcl be bg bh bn bo bpy br bs bxr ca cbk
ce ceb ckb co cs cv cy da de diq dsb dty dv el eml en eo es et eu fa fi fr frr fy ga
gd gl gn gom gu gv he hi hif hr hsb ht hu hy ia id ie ilo io is it ja jbo jv ka kk km
kn ko krc ku kv kw ky la lb lez li lmo lo lrc lt lv mai mg mhr min mk ml mn mr mrj ms
mt mwl my myv mzn nah nap nds ne new nl nn no oc or os pa pam pfl pl pms pnb ps pt qu
rm ro ru rue sa sah sc scn sco sd sh si sk sl so sq sr su sv sw ta te tg th tk tl tr
tt tyv ug uk ur uz vec vep vi vls vo wa war wuu xal xmf yi yo yue zh
```

## Model Training Details

Quantized model built using Fasttext. More details present in the fasttext [blog](https://fasttext.cc/blog/2017/10/02/blog-post.html)

## Reference


``WhatLangId`` is powered by ``FastText`` and `langid`

### Enriching Word Vectors with Subword Information

[1] P. Bojanowski\*, E. Grave\*, A. Joulin, T. Mikolov, [*Enriching Word Vectors with Subword Information*](https://arxiv.org/abs/1607.04606)

```
@article{bojanowski2016enriching,
  title={Enriching Word Vectors with Subword Information},
  author={Bojanowski, Piotr and Grave, Edouard and Joulin, Armand and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.04606},
  year={2016}
}
```

### Bag of Tricks for Efficient Text Classification

[2] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, [*Bag of Tricks for Efficient Text Classification*](https://arxiv.org/abs/1607.01759)

```
@article{joulin2016bag,
  title={Bag of Tricks for Efficient Text Classification},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.01759},
  year={2016}
}
```

### FastText.zip: Compressing text classification models

[3] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, [*FastText.zip: Compressing text classification models*](https://arxiv.org/abs/1612.03651)

```
@article{joulin2016fasttext,
  title={FastText.zip: Compressing text classification models},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Douze, Matthijs and J{\'e}gou, H{\'e}rve and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1612.03651},
  year={2016}
}
```
