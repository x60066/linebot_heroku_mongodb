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
    import get_3G
    import get_4G
    import get_5G
    
    #使用者輸入的訊息
    key_search=str(event.message.text)

    #('is Nemuber')
    if str.isdigit():
        new3RVN = get_3G.RAN(str,1)
        new4RVN = get_4G.RAN(str,1) 
        new5RVN = get_5G.RAN(str,1)  
        
    # ('not Nemuber')
    else:
        new3RVN = get_3G.RAN(str,0)
        new4RVN = get_4G.RAN(str,0)   
        new5RVN = get_5G.RAN(str,0)   


    ran_search_index=1
    
    if ran_search_index != -1 :

        message = TextSendMessage(text='123' 

                                  
                                  )
        
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text='查無此站台')
        line_bot_api.reply_message(event.reply_token, message)
        



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
