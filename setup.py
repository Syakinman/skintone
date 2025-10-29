import os
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="skintone",
    version="0.0.3",
    author="sai",
    author_email="d53520@gmail.com",
    description="Kintone REST API helper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/syakinman/skintone",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.0.0",
    ],
    keywords=["python", "kintone"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
