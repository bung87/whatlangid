from setuptools import setup
import io
try:
    long_description = io.open('README', encoding="utf-8").read()
except Exception:
    long_description = io.open('README.md', encoding="utf-8").read()

setup(
    name='whatlangid',
    version='1.0.6',
    description='Lightning Fast Language Prediction powered by FastText and langid.',
    long_description=long_description,
    author='bung87',
    url='https://github.com/bung87/whatlangid',
    keywords='language detection library',
    packages=['whatlangid'],
    include_package_data=True,
    dependency_links=[
        "git+https://github.com/facebookresearch/fastText.git@master#egg=fasttext-0.8.22",
    ],
    python_requires='>=3',
    install_requires=['fasttext>=0.8.22', 'langid>=1.1.6'],
    test_suite='tests.test_predict_lang.suite',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
