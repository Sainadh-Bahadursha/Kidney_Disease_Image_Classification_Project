import setuptools

# Reads the content of the README.md file for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Defines version and project details
__version__ = "0.0.0"

REPO_NAME = "Kidney_Disease_Image_Classification_Project"
AUTHOR_USER_NAME = "Sainadh-Bahadursha"
SRC_REPO = "kidney_disease_image_classification"
AUTHOR_EMAIL = "sainadhbahadursha@gmail.com"

# Configures the package setup using setuptools
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",  # A brief description of the project
    long_description=long_description,  # Long description from README file
    long_description_content="text/markdown",  # Specifies the format of the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={  # Provides additional project links
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Specifies the source directory
    packages=setuptools.find_packages(where="src")  # Finds and includes packages within the src folder
)
