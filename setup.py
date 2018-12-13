#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rosnode_py_template'],
    package_dir={'': 'src'},
    scripts=['bin/rosnode_py_template_node']
)

setup(**d)
