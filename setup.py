from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path : str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ req.replace("\n","") for req in requirements]  #requirements LIST COMPREHENDING as we read through line by line we will occur with \n @ the end, so replacing it with <no space "">
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(

name = 'ml-project',
version = '0.0.1',
author='Sridhar',
author_email='sridharksananth04@gmail.com',
packages=find_packages(), #This find_package() will search for __init__.py being present in how many folders and consider those foldres as a package and tris to build it as a package
install_requires = get_requirements('requirements.txt')

)