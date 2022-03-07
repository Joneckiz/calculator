import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='calculator',
    version='0.0.1',
    author='Jonas Vengalis',
    author_email='jovengalis@gmail.com',
    description='simple python calculator',
    long_description='simple python calculator long_description',
    url='https://github.com/Joneckiz/calculator',
    license='MIT',
    packages=['code'],
    install_requires=['requests'],
)
