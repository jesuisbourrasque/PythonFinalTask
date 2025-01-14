from setuptools import setup, find_packages


setup(
    name="rss_reader",
    version="4.1",
    description="Pure Python RSS reader",
    url="https://github.com/jesuisbourrasque/PythonFinalTask",
    author="Nikita Isakov",
    author_email="jesuisbourrasque@gmail.com",
    packages=find_packages(include=["rss_reader"]),
    install_requires=[
        "pycodestyle==2.7.0",
        "nose==1.3.7",
        "coverage==5.5",
        "termcolor==1.1.0",
        "feedparser==6.0.2",
        "pytest==6.2.4",
        "pytest-mock==3.6.1",
        "pytest-cov==2.12.1",
        "python-dateutil==2.8.1",
        "requests==2.25.1",
        "fpdf2==2.4.1",
        "Pillow==8.2.0",
        "jinja2==3.0.1",
                      ],
    entry_points={"console_scripts": ["rss-reader=rss_reader.main:main"]},
)
