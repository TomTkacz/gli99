import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gli99",
    version='1.1.5',
    description="Web scraper for gifcities.org",
    package_dir={'':'src'},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    python_requires=">3.10.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'selenium',
        'requests',
        'webdriver-manager',
    ],
    url=f"https://github.com/TomTkacz/gli99",
    author="Tom Tkacz",
    author_email="thomasatkacz@gmail.com",
)