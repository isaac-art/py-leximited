import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leximited",
    version="1.0.4",
    author="Isaac Clarke",
    author_email="isaac@isaacclarke.com",
    description="Lexicographically Delimited Encoding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isaac-art/py-leximited",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)