from setuptools import setup

setup(
    name="selenium-scraper",
    version="0.0.1",
    license="MIT",
    packages=["selenium_scraper"],
    zip_safe=False,
    install_requires=["selenium"],
    entry_points={
        "console_scripts": ["scrape = selenium_scraper.cli:main"]
    },
)
