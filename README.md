# quran_suras

A class based on the API of the [mp3quran](https://www.mp3quran.net), which helps you to fetch the surahs of the Qur’an via the surah number or name 

[Features](https://codeberg.org/Awiteb/quran_suras.py#features)

[Usage](https://codeberg.org/Awiteb/quran_suras.py#usage)

[LICENSE](https://codeberg.org/Awiteb/quran_suras.py#license)

## Features
* get surah by number
* get surah by name
* get surah name by number
* get surah number by name
* get quran page url by number

## Usage

**you can find examples [here](https://codeberg.org/Awiteb/quran_suras.py/src/branch/master/examples)**


you can get surah by number like this
```python
from quran_suras import Quran_suras

quran_suras = Quran_suras()

suras = quran_suras.get_sura_by_number(sura_number=12, amount=1)
print(suras) # {
    # 'sura_name': 'يوسف', 
    #     'result': [
    #         {'reader': 'أحمد الحذيفي', 
    #             'url': 'https://server8.mp3quran.net/ahmad_huth/012.mp3'}
    #         ]
    #     }
```
you can get surah by name like this
```python
from quran_suras import Quran_suras

quran_suras = Quran_suras()

suras = quran_suras.get_sura_by_name(sura_name="النحل", amount=1)
print(suras) # {
    # 'sura_name': 'النحل', 
    #     'result': [
    #         {'reader': 'أحمد الحواشي', 
    #             'url': 'https://server11.mp3quran.net/hawashi/016.mp3'}
    #         ]
    #     }
```
you can get surah name by number like this
```python
from quran_suras import Quran_suras

quran_suras = Quran_suras()

sura_name = quran_suras.get_sura_name(sura_number=88)
print(sura_name) # الغاشية
```
you can get surah number by name like this
```python
from quran_suras import Quran_suras

quran_suras = Quran_suras()

sura_number = quran_suras.get_sura_number(sura_name="النمل")
print(sura_number) # 27
```
you can get page from quran by page number like this
```python
from quran_suras import Quran_suras

quran_suras = Quran_suras()
page = quran_suras.get_page(page_number=601)
print(page) # https://www.mp3quran.net/api/quran_pages_arabic/601.png
```


## LICENSE
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)