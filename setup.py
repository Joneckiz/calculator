import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='calculator',
    version='0.0.3',
    author='Jonas Vengalis',
    author_email='jovengalis@gmail.com',
    description='simple python calculator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Joneckiz/calculator',
    project_urls = {
        "Bug Tracker": "https://github.com/Muls/toolbox/issues"
    },
    license='MIT',
    packages=['calculator'],
    install_requires=['requests'],
)
