import sys
import os

from setuptools import setup, find_packages
from support.setup_codes import setup_commands

name = 'amuse-framework'
version = "12.0a5"
author = 'The AMUSE team'
author_email = 'info@amusecode.org'
license = "Apache License 2.0"
url = 'http://www.amusecode.org/'
install_requires = [
    'wheel>=0.32',
    'docutils>=0.6',
    'numpy>=1.2.2',
    'nose>=0.11.1',
    'mpi4py>=1.1.0',
    'h5py>=1.1.0',
]
description = 'The Astrophysical Multipurpose Software Environment'
with open("README.md", "r") as fh:
    long_description = fh.read()
long_description_content_type = "text/markdown"
classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: C',
    'Programming Language :: C++',
    'Programming Language :: Fortran',
    'Topic :: Scientific/Engineering :: Astronomy',
]

extensions = []

all_data_files = []
all_data_files.append(('share/amuse', ['./config.mk', './build.py']))

packages = find_packages('src', exclude=["amuse.community.*"])
packages.append("amuse.community.interface")
packages.append("amuse.community.distributed")

package_data = {
    'amuse.rfi.tools': ['*.template'],
    'amuse.test.suite.core_tests': [
        '*.txt', '*.dyn', '*.ini',
        '*.nemo',
        '*.dat', 'gadget_snapshot'
    ],
    'amuse.test.suite.codes_tests': [
        '*.txt', 'test_sphray_data*'
    ],
    'amuse.test.suite.ticket_tests': [
        '*.out'
    ],
    'amuse': [
        '*rc'
    ]
}

mapping_from_command_name_to_command_class=setup_commands()

setup(
    name=name,
    version=version,
    classifiers=classifiers,
    url=url,
    author_email=author_email,
    author=author,
    description=description,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    install_requires=install_requires,
    cmdclass=mapping_from_command_name_to_command_class,
    ext_modules=extensions,
    package_dir={'': 'src'},
    packages=packages,
    package_data=package_data,
    data_files=all_data_files,
    scripts=[ "amusifier" ],
)
