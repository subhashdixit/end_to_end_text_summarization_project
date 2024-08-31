import setuptools  # Import setuptools, a library for building and distributing Python packages.

# Read the content of the README file to use as the long description of the package.
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version of the package.
__version__ = "0.0.0"

# Define project metadata.
REPO_NAME = "end_to_end_text_summarization_project"  # Name of the repository on GitHub.
AUTHOR_USER_NAME = "subhashdixit"  # GitHub username of the author.
SRC_REPO = "textSummarizer"  # The name of the source directory for the package.
AUTHOR_EMAIL = "subhashdixit17@gmail.com"  # Email address of the author.

setuptools.setup(
    name=SRC_REPO,  # The name of the package.
    version=__version__,  # The version of the package.
    author=AUTHOR_USER_NAME,  # The author's GitHub username.
    author_email=AUTHOR_EMAIL,  # The author's email address.
    description="A Text Summarizer Project Using Hugging Face Transformer Model",  # A short description of the package.
    long_description=long_description,  # A long description of the package, typically from the README file.
    long_description_content_type="text/markdown",  # The format of the long description (Markdown).
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # The URL for the project’s homepage.
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # URL for tracking bugs and issues.
    },
    package_dir={"": "src"},  # Specifies that the source code is in the "src" directory.
    packages=setuptools.find_packages(where="src")  # Finds all packages under the "src" directory.
)
