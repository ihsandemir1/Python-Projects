import requests
import json
import os
print("Dlive UNFOLLLOW Bot by mido.py")
dosya =  open('auth.txt','r')
hedef_kisi = input("kime:")
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
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

    data = {
            'operationName': 'UnfollowUser',
            'variables': {'streamer': takipedilcek},
            'extensions':{
                    "persistedQuery":{
                                    "version":1,
                                    "sha256Hash":"681ef3737bb34799ffe779b420db05b7f83bc8c3f17cdd17c7181bd7eca9859c"
                                    }
                        },


    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response = response.json()
    print(response)

while True:
	deger = dosya.readline()
	if deger == " " or deger =="":
		print('auth keyleriniz bitmiş olabilir')
		exit()
	auth = deger.replace("\n","")
	authKeybothesap = auth
	Follow(hedef_kisi)
