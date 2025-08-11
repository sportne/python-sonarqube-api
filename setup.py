import setuptools

setuptools.setup(
    name="python-sonarqube-api",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A Python wrapper for the Sonarqube Web API.",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
