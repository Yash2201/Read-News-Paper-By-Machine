# Akhbaar Padhke Sunaao
# News API.org Free NEWS API Key :- 9909426f851746168632e9e88ff49327
import requests
import json
import time

def speak(str):
    from win32com.client import  Dispatch

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def NEWSPAPER():

    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=9909426f851746168632e9e88ff49327"
    try:
        json_data = requests.get(url)
    except:
        print("No Internet Connection")
        exit(0)

    news = json.loads(json_data.text)

    for new in news['articles']:
        print("############################################\n")
        print(str(new['title']),"\n\n")
        speak(new['title'])
        print('---------------------------\n')


        print(str(new['description']), "\n\n")
        speak(new['description'])
        print('.................................................\n')
        time.sleep(2)

if __name__ == '__main__':
    NEWSPAPER()
