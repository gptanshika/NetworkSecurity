from setuptools import find_packages,setup
from typing import List

def  get_requirements()->List[str]:
    """
    This Function will return list of requirements
    
    """
    requirement_list:List[str] = []
    try:
        with open('requirements.txt','r') as files:
            #Read lines from the file
            lines = files.readlines()
            #Process each line
            for line in lines:
                requirements = line.strip()
                #ignore empty line and -e .
                if requirements and requirements!='-e .':
                    requirement_list.append(requirements)
            
        
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name = "NetworkSecurity",
    version = '0.0.1',
    author = 'Anshika Gupta',
    author_email = "anshikagupta@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)



