from quran_suras import QuranSuras

quran_suras = QuranSuras()

suras = quran_suras.get_sura_by_name(sura_name="النحل", amount=1)
print(suras) # {
    # 'sura_name': 'النحل', 
    #     'result': [
    #         {'reader': 'أحمد الحواشي', 
    #             'url': 'https://server11.mp3quran.net/hawashi/016.mp3'}
    #         ]
    #     }