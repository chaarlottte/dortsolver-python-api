from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="dort",
    version="1.4",
    description="dort solver/email api wrapper for python",
    url="https://github.com/chaarlottte/dortsolver-python-api",
    author="chaarlottte",
    packages=[ 
        "dort",
        "dort.captcha",
        "dort.mail"
    ],
    install_requires=[ 
        "imap-tools",
        "requests"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown"
)