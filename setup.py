from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
  """
  this function will return list of requirements
  """
  requirements=[]
  with open(file_path) as file_obj:
    requirements = file_obj.readlines()
    #requirements = [req.replace("\n","") for req in requirements]
    requirements =[req.strip() for req in requirements]
    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)

  return requirements

setup(name = "AI_ML_PROJECT",
      version="0.0.1",
      author="suresh",
      author_email="suresh.savaram@gmail.com",
      packages=find_packages(),
      install_requires = get_requirements("requirement.txt"))
