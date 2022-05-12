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
    sht = gc.open_by_url(
'https://docs.google.com/spreadsheets/d/1WlBoMCOuSe1n026LIsJcBJrFn2FrTVtVaEWBGERziwM/'
)
    wks_list = sht[0]
    str_list = wks_list.find(key_search)
    
    a1 = sht[0].cell((str_list[0].row,18)).value
    a2 = sht[0].cell((str_list[0].row,19)).value
    
    #*************************************************
    
    pretty_note = '♫*♬'
    pretty_text = ''
    for i in event.message.text:
        pretty_text += i
        pretty_text += random.choice(pretty_note)
        
    
    message = TextSendMessage(text='('+a1+')'+'+'+'('+a2+')')
    line_bot_api.reply_message(event.reply_token, message)



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
