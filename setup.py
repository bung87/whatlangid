from setuptools import setup
import io

setup(
    name='whatlangid',
    version='1.0.3',
    description='Lightning Fast Language Prediction powered by FastText and langid.',
    long_description=io.open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
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
