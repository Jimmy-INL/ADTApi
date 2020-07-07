from setuptools import setup, find_packages

setup(
      name='digitaltwins',
      version='0.1',
      description='ADT python SDK',
      author='Azure Digital Twin autogenerated using autorest by Paul Hernandez',
      url='https://github.com/pauldj54/ADTApi'
      packages=[find_packages(exclude=['tests*'])
      )