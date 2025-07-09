from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    LIST_OF_REQUIREMENTS = f.read().splitlines()

## edit below variables as per your requirements -
REPO_NAME = "Books Recommender System"
AUTHOR_USER_NAME = "SAYEED HASSAN"
SRC_REPO = "books_recommender_system"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="SAYEED HASSAN",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sayeedhassan329/Books_Recommender_system",
    author_email="sayeedhassan329@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.11",
    install_requires=LIST_OF_REQUIREMENTS
)
