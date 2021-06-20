from quran_suras import Quran_suras

quran_suras = Quran_suras()
page = quran_suras.get_page(page_number=601)
print(page) # https://www.mp3quran.net/api/quran_pages_arabic/601.png