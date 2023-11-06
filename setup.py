#setup tools is used to convert your project into packahe( a package is group of python files which has multiple modules and a module is 
# a functions and classes)
import setuptools

with open("README.md", "r", encoding='utf-8') as f:

    long_description = f.read()


# below is the configuration for my package i am creating

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project" # my git hub repo name
AUTHOR_USER_NAME = "Debojit-0"
SRC_REPO = "TextSumaarizer" # this is my src folder if you see src folder you will see this like this src\TextSumaarizer
AUTHOR_EMAIL = "debojit.mandal@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)
# so find_package in packages=setuptools.find_packages will find the folders containing __init__.py to convert that perticular folder into packages

# now if you recall inside src you have components and inside each components you have __init__.py file now this file is resposnsible
# for saying to our setup file hey this folder needs to be converted to package 
# for eg lets  componets folder dint have __init__.py file then this folder wont be consodered for converting into packages by setup.py file
# so the __init__.py file tells the setup.py file that which folders needs to be converted to packages
   