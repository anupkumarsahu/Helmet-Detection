from setuptools import find_packages, setup

REQUIREMENT_FILE_NAME = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirement_list(requirement_filename=REQUIREMENT_FILE_NAME) -> list:
    try:
        requirement_list = None
        with open(requirement_filename) as requirement_file:
            requirement_list = [requirement.replace("\n", "") for requirement in requirement_file]
            requirement_list.remove(REMOVE_PACKAGE)
        return requirement_list
    except Exception as e:
        raise e
    
    

setup(
    name="helmet",
    license="MIT",
    version="0.0.1",
    author="Anup",
    author_email="anup.sahu@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement_list(),
)
