from setuptools import setup

setup(
    name="dommonitor",
    version="0.0.1",
    description="This tool is diff tool to compare html with dom",
    author="Taurin190",
    install_requires=[
        "requests",
        "beautifulsoup4",
        "selenium",
        "configparser",
        "slackweb",
        "pymongo",
    ],
    entry_points={
        "console_scripts": [
            "dommonitor = main:main"
        ]
    }
)