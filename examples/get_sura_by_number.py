from quran_suras import QuranSuras

quran_suras = QuranSuras()

suras = quran_suras.get_sura_by_number(sura_number=12, amount=1)
print(suras) # {
    # 'sura_name': 'يوسف', 
    #     'result': [
    #         {'reader': 'أحمد الحذيفي', 
    #             'url': 'https://server8.mp3quran.net/ahmad_huth/012.mp3'}
    #         ]
    #     }