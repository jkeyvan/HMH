# -*- coding: utf-8 -*-
import json
import urllib

import requests
import time
TOKEN = "402101982:AAGdxgIx7NezHHAEHpW-P3DXzlS4VT5eDTs"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"

    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def send_message_to_admin_bot(text):

    URL2 = "https://api.telegram.org/bot239297426:AAF6WPDPGtfvx_tm6GroSgHsukKPZmdrCo4/"
    sendToMe=("feedBack: "+"\n"+ "{}").format(text)

    sendToMe=urllib.quote(sendToMe)
    #print sendToMe
    #url = URL2 + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(sendToMe, 130627497)
    url = URL2 + "sendMessage?text={}&chat_id={}&parse_mode=HTML".format(sendToMe, 130627497)
    get_url(url)
    print 10

def send_message(text, chat_id,reply_markup=None):
    text = urllib.quote(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)

def handle_updates(updates):
    for update in updates["result"]:
        chat = update["message"]["chat"]["id"]
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            username=update["message"]["chat"]["username"]
            if text =="/start":
                send_message("لطفا هرگونه #انتقاد و #پیشنهاد خود را  پیرامون عملکرد هیات مُحبان الحُسَین (علیه السلام) خوابگاه داخل سال 95-96 , وارد فرمایید :  "  + "\n" ,chat)
                print 4
            else:
                send_message_to_admin_bot(text.encode("utf-8"))
                send_message("نظر شما ثبت شد."+"\n"+"از همکاری شما متشکریم " , chat)

        except Exception as e:
            send_message("لطفا نظر خود را در به صورت متن وارد نمایید",chat)
            print e

def get_last_id(updates):
    updates_id=[int(updates["result"][nthitem]["update_id"]) for nthitem in range(len(updates["result"]))]
    last=max(updates_id)
    return last

def main():
    offset=None

    while True:
        updates=get_updates(offset)
        print "getting updates"
        if len(updates["result"])>0:
            handle_updates(updates)
            offset = get_last_id(updates) + 1
        time.sleep(0.5)

if __name__=="__main__":

    main()
