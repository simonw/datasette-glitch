from setuptools import setup
import os

VERSION = "0.1a"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-glitch",
    description="Utilities to help run Datasette on Glitch",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-glitch",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-glitch/issues",
        "CI": "https://github.com/simonw/datasette-glitch/actions",
        "Changelog": "https://github.com/simonw/datasette-glitch/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_glitch"],
    entry_points={"datasette": ["glitch = datasette_glitch"]},
    install_requires=["datasette==0.45a3"],
    extras_require={"test": ["pytest", "pytest-asyncio", "httpx"]},
    tests_require=["datasette-glitch[test]"],
)
