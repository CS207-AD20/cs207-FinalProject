import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AD20",
    version="0.0.2",
    author="Lindsey Brown, Xinyue Wang, Kevin Yoon",
    author_email=" ",
    description="Automatic Differentiation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CS207-AD20/cs207-FinalProject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)