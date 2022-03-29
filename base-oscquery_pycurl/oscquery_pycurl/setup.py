import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

LONG_DESCRIPTION = 'PyCurl based interactions with the Open Source Context APIs'

setuptools.setup(
    name="oscquery-pycurl",
    version="0.0.2",
    author="Open Source Context",
    author_email="support.tech@oscontext.com",
    description="OSC PyCurl based query",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/oscquery_pycurl/issues",
    },
    keywords=['python', 'OSC', 'pycurl'],
    install_requires=['pycurl'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
