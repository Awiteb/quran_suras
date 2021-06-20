import setuptools

VERSION = "1.1.2"
README_FILENAME = "README.md"
KEYWORD = ['surah', 'sura', 'quran',]

with open(README_FILENAME, "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()
with open("requirements.txt", encoding="utf-8") as require_file:
    requires = [require.strip() for require in require_file]

setuptools.setup(
    name="quran_suras",
    version=VERSION,
    author="Awiteb",
    author_email="Awiteb@hotmail.com",
    description="API of the mp3quran.net, which helps you to fetch the surahs of the Qur’an via the surah number or name and more",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://codeberg.org/Awiteb/quran_suras",
    packages=setuptools.find_packages(),
    keywords=KEYWORD,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=requires,
)