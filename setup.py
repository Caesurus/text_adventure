import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text_adventure",
    version="0.1.0",
    author="Caesurus",
    author_email="caesurus+textadventure@gmail.com",
    description="A simple text adventure building framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caesurus/text_adventure",
    project_urls={
        "Bug Tracker": "https://github.com/caesurus/text_adventure/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'text_adventure'},
    py_module=['text_adventure'],
    packages=setuptools.find_packages(where="text_adventure"),
    python_requires=">=3.6",
)
