"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

**Generating Distribution Archives:**
https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives

** Uploading Distribution Archives:**
https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

**Notes:**
    In order for the Custom Install wrapper to run successfully we have to use the source distribution
    when we are building our archives. This is done by running the command:
        python setup.py sdist

    This creates a *.tar.gz source file that we use to send to PyPi/TestPyPi that will run setup.py
    compared to shipping a wheel, *.whl, which is binary and does not run any post-install logic.

**Contributors:**
    Greg Amato, amatobahn@gmail.com, June 18, 2020.
"""
from setuptools import setup, find_packages
from setuptools.command.install import install
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")


class CustomInstall(install):
    def run(self):
        # Run the standard PyPi Copy
        install.run(self)

def read_requirements():
    with open('requirements.txt') as reqs:
        return reqs.read().splitlines()


setup(
    # Metadata
    name="bqt",
    version="1.4.2",  # don't forget to update the bl_info version
    description="Files to help bootstrap PySide2 with an event loop within Blender.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=["Technical", "Art", "TechArt", "TechArtOrg", "Blender", "Qt", "PySide", "tool", "pipeline", "gamedev", "vfx", "3d"],
    license="Mozilla Public License 2.0 (MPL 2.0)",
    url="https://github.com/techartorg/bqt",
    author="tech-artists.org",
    # Classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3.7",
    ],
    # Requirements
    python_requires=">=3.7",
    packages=["bqt"],
    install_requires=read_requirements(),
    # Package Data
    include_package_data=True,
    package_data={"bqt": ["*.png", "*.qss"]},
    # Install Wrapper
    cmdclass={"install": CustomInstall},
)
