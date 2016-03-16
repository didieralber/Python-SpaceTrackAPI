from setuptools import setup, find_packages
from codecs import open
from os import path
import spacetrackapi

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

requirements = []
with open(path.join(here, 'requirements.txt')) as f:
    for line in f:
        requirements.append(line)

setup(
    name='spacetrackapi',
    version=spacetrackapi.__version__,
    description='A client for the Space-Track API',
    long_description=long_description,
    url='https://github.com/didieralber/Python-SpaceTrackAPI',
    author='Didier Alber',
    author_email='didier.alber@gmail.com',
    license='MIT',

    packages=['spacetrackapi'],
    install_requires=requirements,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='spacetrack Space-Track'
)
