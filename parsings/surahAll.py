


import requests
from bs4 import BeautifulSoup
# from bs4 import BeautifulSoup
def surah_all(surah_id):

    surah_section = {}
    
    url = f'https://islom.uz/mano_tarjima/{surah_id}'
    
    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')

    ids = html.find_all("span",style="display:none;")[2].text
    audio = "islom.uz" + html.find_all("span",id='url_audio')[0].text
    title ="Қироат: "+ html.find_all("div",id="seName")[0].text + " сураси"
    text = str()
    for el  in html.find_all('div',class_="copy_oyat"):
        
        text += el.get('data-clipboard-text').replace('islom.uz «Тафсири ҳилол» китобидан'," ")
    surah_section[int(ids)] = {
        'title': title,
        'audio': audio,
        'text': text
    }
    
        
    return surah_section


def surah_all_id():

    url = f'https://islom.uz/mano_tarjima/114'
    
    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')
    surah_id = {}
    k = html.find_all("span",class_="p_menu")[11:] #bu yerda malomot filtir qilinayabdi
    for e in k:
        e = e.text #text malumot ilindi
        idd, title = e.split(". ") # malumot ajratilyabdi
        surah_id[title]= int(idd) # va saqlanayabdi
    return surah_id

# print(surah_all(70))