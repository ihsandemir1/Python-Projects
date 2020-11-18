# -*- coding: cp1254 -*-
import requests
import json
import os
import time
from colorama import Fore, Style
os.system("title " + " Dlive Follower Bot V2")
print("Dlive Follower Bot by mido.py")
dosya =  open('auth.txt','r')
hedef_kisi = input("Takipci Gönderilecek Kişi:")
def Follow(takipedilcek):
    url = 'https://graphigo.prd.dlive.tv'
            
    headers = {
                    'accept': '/',
                    'authorization': authKeybothesap,
                    'content-type': 'application/json',
                    'fingerprint': '',
                    'gacid': 'undefined',
                    'Origin': 'https://dlive.tv/',
                    'User-Agent':
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
               }

    data = {
            'operationName': 'FollowUser',
            'variables': {'streamer': takipedilcek},
            'extensions':{
                    "persistedQuery":{
                                    "version":1,
                                    "sha256Hash":"daf146d77e754b6b5a7acd945ff005ae028b33feaa3c79e04e71505190003a5d"
                                    }
                        },


            }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response = response.json()
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result,"- Gönderme Başarılı")
    time.sleep(1)
while True:
	deger = dosya.readline()
	if deger == " " or deger =="":
		print('auth keyleriniz bitmis olabilir')
		time.sleep(5)
		exit()
	auth = deger.replace("\n","")
	authKeybothesap = auth
	Follow(hedef_kisi)
