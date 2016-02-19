from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='rpi-dots-minecraft',
    version='0.1.3',
    install_requires= ['rpi.gpio >= 0.5.5'],
    packages=find_packages(),
    scripts=['scripts/rpi_dots_minecraft'],
    url='https://github.com/gbaman/rpi_dots_minecraft',
    long_description=read('README.rst'),
    license='MIT',
    author='Andrew Mulholland',
    author_email='gbaman1@gmail.com',
    description='A Python program that reads the selected dots on the Raspberry Pi DOTs board and uses these to generate a 3d simulated airplane inside Minecraft Pi.'

)
