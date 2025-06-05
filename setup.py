import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "end_to_end_mlproject"
SRC_REPO = "mlProject"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/kiranupreti/end_to_end_mlproject",
    project_urls={
        "Bug Tracker": f"https://github.com/kiranupreti/end_to_end_mlproject/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)