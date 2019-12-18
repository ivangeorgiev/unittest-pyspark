import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unittest-pyspark", # Replace with your own username
    version="0.0.5",
    author="Ivan Georgiev",
    author_email="ivan.georgiev@gmail.com",
    description="Extension to unittest for pySpark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivangeorgiev/unittest-pyspark",
    packages=setuptools.find_packages(),
    install_requires=[
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
