import requests
import json
import difflib

class Quran_suras():
    def __init__(self,):
        self.API = "https://www.mp3quran.net/api/"
    
    def get_sura_by_name(self, sura_name:str, amount:int):
        """ get sura by name

        Args:
            sura_name (str): name of sura
            amount (int): amount of suras

        Returns:
            dict: dictionary of suras
        """
        sura_number = self.get_sura_number(sura_name) # get sura number use get_sura_number method
        return self.__get_sura(sura_number, amount)
    
    def get_sura_by_number(self, sura_number:int, amount:int):
        """ get sura by number

        Args:
            sura_number (int): number of sura
            amount (int): amount of suras

        Returns:
            dict: dictionary of suras
        """
        return self.__get_sura(sura_number, amount)
    
    def get_sura_name(self, sura_number:int):
        """get sura name by number

        Args:
            sura_number (int): number of the sura you want to name

        Raises:
            Exception: if sura number bigger than 114

        Returns:
            str: sura name
        """
        if sura_number <= 114:
            for ob in json.loads(requests.get(self.API+"_arabic_sura.php").text)['Suras_Name']:
                if ob['id'] == str(sura_number):
                    return self.__strip_tashkeel(ob['name'].strip())
        else:
            raise Exception("Invalid sura number: sura not found '%s'" % sura_number)
        
    def get_sura_number(self, sura_name:str):
        """ Returns the number of sura

        Args:
            sura_name (str): name of the sura you want to number

        Raises:
            Exception: if sura name It is not in the list of suras, He will suggest three suras for you if there is a match

        Returns:
            int: number of sura
        """
        suras_ids = {self.__strip_tashkeel(ob['name'].strip()): ob['id'] for ob in json.loads(requests.get(self.API+"_arabic_sura.php").text)['Suras_Name']}
        if sura_name in suras_ids.keys():
            return int(suras_ids.get(sura_name))
        else:
            spell_checker = self.__spell_checker(sura_name, list(suras_ids.keys()))
            raise Exception(f"Invalid sura name: '{sura_name}' not found {(', did you mean '+' or '.join(spell_checker)) if spell_checker else ''}")
    
    def get_page(self, page_number:int):
        """ Return url of page by page_number

        Args:
            page_number (int): number of page

        Raises:
            Exception: if page_number bigger than 604 or smaller than 1

        Returns:
            str: url of page by page_number
        """
        if page_number > 0 and page_number <= 604:
            page_number = self.__get_number(page_number)
            return f"{self.API}quran_pages_arabic/{page_number}.png"
        else:
            raise Exception("Invalid page number: {} not found".format(page_number))
    
    def __get_sura(self, sura_number:int, amount:int):
        """get sura by sura_number

        Args:
            sura_number (int): number of sura
            amount (int): amount of suras

        Returns:
            dict: dictionary of suras
        """
        suras_dict = {"sura_name":self.get_sura_name(sura_number),
                        "result":[]
                        }
        for ob in json.loads(requests.get(self.API+"_arabic.php").text)['reciters']:
            if len(suras_dict['result']) != amount:
                if str(sura_number) in ob['suras']:
                    sura_dict = {"reader":ob['name'],
                                    "url":self.__get_url(sura_number, ob['Server'])
                                    }
                    suras_dict['result'].append(sura_dict)
                else:
                    pass
            else:
                break
        return suras_dict
    
    def __strip_tashkeel(self, text):
        """Strip vowels from a text, include Shadda.
        this function from 
            https://github.com/linuxscout/pyarabic/blob/bc8438ff06e199d42c757847d4fd5da775673d64/pyarabic/araby.py#L742
        """
        # Diacritics
        FATHATAN = u'\u064b'
        DAMMATAN = u'\u064c'
        KASRATAN = u'\u064d'
        FATHA = u'\u064e'
        DAMMA = u'\u064f'
        KASRA = u'\u0650'
        SHADDA = u'\u0651'
        SUKUN = u'\u0652'
        TASHKEEL = (FATHATAN, DAMMATAN, KASRATAN, FATHA, DAMMA, KASRA,
                        SUKUN, SHADDA)
        for char in TASHKEEL:
            text = text.replace(char, '')
        return text
    
    def __spell_checker(self, sura_name:str, suras:list):
        """use difflib.get_close_matches to extract the nearest sura from the suras that matches the sura_name
        Args:
            sura_name (str): name of sura
            suras (list): suras

        Returns:
            list: None if there is no match or a list of suras that match
        """
        sura =  difflib.get_close_matches(sura_name, map(self.__strip_tashkeel, suras))
        return sura if sura else None
    
    def __get_url(self, sura_number:int, server:str):
        """ Return the url of sura

        Args:
            sura_number (int): number of sura
            server (str): The server that contains the surah 

        Returns:
            str: Sura link in mp3 extension
        """
        sura_number = self.__get_number(sura_number)
        return f"{server}/{sura_number}.mp3"
    
    def __get_number(self, sura_number:int):
        """Return number with zero if length smaller than 3

        Args:
            sura_number (int): number

        Returns:
            str: number with zero if length smaller than 3
        """
        length = len(str(sura_number))
        return ('0' if length == 2 else '00' if length == 1 else '')+str(sura_number)