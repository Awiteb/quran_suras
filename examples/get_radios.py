from quran_suras import QuranSuras

quran_suras = QuranSuras()

radios = quran_suras.get_radios('en', 3)
print(radios) #{
#         'language': 'en', 
#         'result': [
#             {'name': '---Amazing short Recitations---', 
#                 'url': 'http://live.mp3quran.net:9702/'}, 
#             {'name': '--Quran Tafseer--', 
#                 'url': 'http://live.mp3quran.net:9718/'}, 
#             {'name': '-Beautiful Recitations-', 
#                 'url': 'http://live.mp3quran.net:9992/'}
#             ]
#         }