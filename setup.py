import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='calculator',
    version='0.0.1',
    author='Jonas Vengalis',
    author_email='jovengalis@gmail.com',
    description='simple python calculator packege',
    long_description='my first python project, code of a simple calculator 
    url='https://github.com/Joneckiz/calculator',
    license='MIT',
    packages=['calculator'],
    install_requires=['libpq-dev, 'python-dev'],
)
