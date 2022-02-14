import re
from setuptools import setup, find_packages

readme = ""
with open("README.md") as f:
    readme = f.read()

requirements = []

version = ""
with open("fuwa/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("No version set")

EXTRAS_REQUIRE = {
    "gateway": "fuwa-gateway"
}

setup(
    name="fuwa",
    version=version,
    packages=find_packages(),
    description="The advertisement and parent package for the fuwa eco-system",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="justanotherebyte",
    url="https://github.com/fuwa-py/fuwa",
    install_requires=requirements,
    install_package_data=True,
    python_requires='>=3.8.0',
    extras_require=EXTRAS_REQUIRE,
    classifiers=[

        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
    project_urls={
        "Issue Tracker": "https://github.com/fuwa-py/fuwa/issues"
    }
)