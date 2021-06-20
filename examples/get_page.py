from quran_suras import QuranSuras

quran_suras = QuranSuras()
page = quran_suras.get_page(page_number=601)
print(page) # https://www.mp3quran.net/api/quran_pages_arabic/601.png