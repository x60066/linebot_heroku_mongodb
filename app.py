import random
import pygsheets
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
# Channel Access Token
line_bot_api = LineBotApi('TnS1t96rjGH7IvlqxyHqQ25e/e6jvVLOQfDUBaalj71kZu4miy9PRZk9r38DQJ2XcUV/mzlOc7b7hZZ62geq0gjDb37OsyGkpaG3+Gnkhu/Asvul9cj959G/hnoVAQ35H6V1XHdKmESJrF+yYF7RqAdB04t89/1O/w1cDnyilFU=')
# Channel Secret1
handler = WebhookHandler('c3dedfb2e69582e5d91aa3775c2b3eb4')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    key_search=str(event.message.text)
    #*************************************************
    gc = pygsheets.authorize(service_file='Google python.json')
    print('123')
    sheet_4G = gc.open_by_url(
'https://docs.google.com/spreadsheets/d/1WlBoMCOuSe1n026LIsJcBJrFn2FrTVtVaEWBGERziwM/'
)
    sheet_3G = gc.open_by_url(
'https://docs.google.com/spreadsheets/d/1sWBdjt98vF_Bo5Tvs_Iji7jdJSnkrt7uDYy_VQs2vqo/edit#gid=1669047201'
)
    wks_list = sheet_4G[0]
    ran_name_list=list(wks_list.get_col(2))
    
    try:
        ran_search_index=ran_name_list.index(key_search)
        ran_search_index+=1
    except:
        ran_search_index=-1
        
    wks_list_3G=sheet_3G[0]
    ran_name_list_3g=list(wks_list_3G.get_col(4))
    try:
        ran_search_index_3g=ran_name_list_3g.index(key_search)
    except:
        ran_search_index_3g=-1
        

    

    
    #*************************************************
    
    if ran_search_index != -1 :
        ran_3g_id=sheet_3G[0].cell((ran_search_index_3g,3)).value
        ran_4g_id=sheet_4G[0].cell((ran_search_index,1)).value
        a1 = sheet_4G[0].cell((ran_search_index,27)).value
        a2 = sheet_4G[0].cell((ran_search_index,28)).value
        ran_ip = sheet_4G[0].cell((ran_search_index,32)).value
        ran_staue = sheet_4G[0].cell((ran_search_index,13)).value
        message = TextSendMessage(text= 
                                  ran_3g_id
                                  +'\n'+ ran_4g_id
                                  +'\n'+ ran_staue
                                  +'\n'+ a1 
                                  +'\n'+a2
                                  +'\n'+str(ran_ip)
                                  
                                  )
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text='查無此站台')
        line_bot_api.reply_message(event.reply_token, message)
        



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
