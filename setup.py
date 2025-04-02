from setuptools import setup, find_packages
reqs = ['numpy', 'pandas', 'pathlib']

setup(
        name                  = "FieldSpecUtils",
        packages              = find_packages(),
        install_requires      = reqs,
        version               = "1.0.5",
        author                = "NERC Field Spectroscopy Facility",
        author_email          = "fsf@ed.ac.uk",
        description           = ("A software package forconducting calculations of various remote sensing indices from hyperspectral data, and convolution processes to transform hyperspectral data to various satellite platform outputs. "),
        license               = "MIT",
        url                   = "https://github.com/NERC-FSF/FieldSpectraUtils",
        classifiers           =[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2"
        ]
	)
		
