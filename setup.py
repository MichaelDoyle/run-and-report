#!/usr/bin/env python
from distutils.core import setup

version = "0.3.2"

setup(name="run-and-report",
      version=version,
      description="Run a command and report it to Riemann",
      author="Sam Neubardt",
      author_email="samneubardt@gmail.com",
      url="https://github.com/samn/run-and-report",
      scripts=['run-and-report.py']
    )
