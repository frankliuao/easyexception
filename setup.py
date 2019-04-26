from setuptools import setup, find_packages

with open("README.MD", "r") as fh:
    long_des = fh.read()

setup(
    name="easyexception",
    version="0.0.2",
    author="Ao Liu, Jie Gao",
    author_email="ao@aoliu.tech, geographer2008@gmail.com",
    description=("Easy-to-use custom error/warning/message exceptions."),
    license="MIT",
    keywords=["Exception", "Easy"],
    url="https://pypi.python.org/pypi/easyexception",
    packages=find_packages(),
    python_requires='>=3.0',
    long_description=long_des,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
