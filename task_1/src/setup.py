from setuptools import setup, find_packages

setup(
    name="test_figures_package",
    version="0.0.1",
    author="Leyla",
    author_email="saryymova@gmail.com",
    description="la-la-la",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7.0",
    url="https://github.com/Leila132/Mindbox-test-tasks",
)