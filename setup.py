import os
from setuptools import setup

kwds = {}

# Read the long description from the README.txt
thisdir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(thisdir, 'README.rst')) as f:
    kwds['long_description'] = f.read()


with open('grin.py') as fp:
    _locals = {}
    for line in fp:
        if line.startswith('__version__'):
            exec(line, None, _locals)
            break
    __version__ = _locals['__version__']

setup(
    name='grin',
    version=__version__,
    author='Robert Kern',
    author_email='robert.kern@enthought.com',
    description="A grep program configured the way I like it.",
    license="BSD",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],

    py_modules=["grin"],
    entry_points=dict(
        console_scripts=[
            "grin = grin:grin_main",
            "grind = grin:grind_main",
        ],
    ),
    install_requires=[
        'six>=1.6',
        'colorama>=0.3',
    ],
    extras_require={
        ':python_version == "2.6"': ['argparse>=1.1'],
    },
    tests_require=[
        'nose >= 0.10',
    ],
    test_suite='nose.collector',
    **kwds
)
