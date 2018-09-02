from setuptools import setup

setup(
    name="PyHickmanSales",
    version="1.1.0",
    packages=["PyHickmanSales", ],
    license="MIT",
    description="Library providing access to sales listings from Hickman Chevrolet Cadillac",
    url="https://github.com/nint8835/PyHickmanSales",
    author="nint8835",
    author_email="riley@rileyflynn.me",
    install_requires=[
        "lxml", "requests"
    ]
)
