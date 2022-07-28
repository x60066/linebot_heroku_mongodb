import random
import pygsheets
# 增加了 render_template
from flask import Flask, request, abort, render_template

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

# 增加的這段放在下面
@app.route("/")
def home():
    return render_template("home.html")
# 增加的這段放在上面

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
    import get_ele_num

    #使用者輸入的訊息
    key_search=str(event.message.text)
    
    if key_search.isdigit() and len(key_search)==11 :
        ele_num=get_ele_num.RAN(key_search)
        
        if ele_num.ran_search_index != -1 :
            message = TextSendMessage(text=ele_num.ran_id)
            line_bot_api.reply_message(event.reply_token, message)
        else:
            message = TextSendMessage(text='查無此電號')
            line_bot_api.reply_message(event.reply_token, message)
        
    else:

        #('is Nemuber').ran_4Id
        if key_search.isdigit():
            if len(key_search)==4:
                new3RVN = get_3G.RAN(key_search,1)
                new4RVN = get_4G.RAN(new3RVN.ran_4Id,1) 
                new5RVN = get_5G.RAN(new4RVN.ran_5Id,1)
            elif len(key_search)==6:                
                new3RVN = get_3G.RAN(key_search,2)
                new4RVN = get_4G.RAN(key_search,1)                   
                new5RVN = get_5G.RAN(new4RVN.ran_5Id,1)                              
            elif len(key_search)==7:
                new3RVN = get_3G.RAN('41'+key_search[3:],2) 
                new4RVN = get_4G.RAN('41'+key_search[3:],1)
                new5RVN = get_5G.RAN(key_search,1)                
                 
            
        # ('not Nemuber')
        else:
            new3RVN = get_3G.RAN(key_search,0)
            new4RVN = get_4G.RAN(key_search,0)   
            new5RVN = get_5G.RAN(key_search,0)   

        ran_search_index=1
        
        if new3RVN.ran_search_index != -1 or new4RVN.ran_search_index!= -1 or new5RVN.ran_search_index!= -1 :

            message = TextSendMessage(text=
                                      '【 '+new4RVN.XRAN+' 】\n'+'\n' +
                                    '【BtsId】'+'\n' +
                                    ''+new3RVN.ran_id+' '+new3RVN.SiteName+'\n' +
                                    ''+new4RVN.ran_id+' '+new4RVN.SiteName+'\n' +
                                    ''+new5RVN.ran_id+' '+new5RVN.SiteName+'\n' +'\n' +
                                    '【Co-Site】'+'\n' +
                                    '3：'+new3RVN.wCoSite+'\n' +
                                    '4：'+new4RVN.wCoSite+'\n' +
                                    '5：'+new5RVN.wCoSite+'\n' +'\n' +
                                    '【RF_Module】'+'\n' +
                                    '3：'+new3RVN.RFModule+'\n' +
                                    '4：'+new4RVN.RFModule+'\n' +
                                    '5：'+new5RVN.RFModule+'\n' +'\n' +
                                    '【IP address】'+'\n' +
                                    '3：'+new3RVN.BTSIP+'\n' +
                                    '4：'+new4RVN.BTSIP+'\n' +
                                    '5：'+new5RVN.BTSIP+'\n' +'\n' +
                                    '【PCI】'+'\n' +
                                    '4：'+new4RVN.ran_PCI+'\n' +
                                    '5：'+new5RVN.ran_PCI+'\n' +'\n' +
                                    '【GPS】'+'\n' +
                                    'GPS：'+new4RVN.GPSE + ' , ' + new4RVN.GPSS  +'\n'
                                    'TRS：'+new4RVN.TRS                                 
                                    )
            
            line_bot_api.reply_message(event.reply_token, message)
        else:
            message = TextSendMessage(text='查無此站台+'+'\n'+'上次更新時間2022/06/30')
            line_bot_api.reply_message(event.reply_token, message)
            



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
