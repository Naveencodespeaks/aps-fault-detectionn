from setuptools import fing_packages, setup


def get_requirements():
    pass

setup(

    name = "sensor",
    version = "0.0.1",
    author = "ineuron",
    packages = find_package(),
    install_requires = get_requirements(),
)