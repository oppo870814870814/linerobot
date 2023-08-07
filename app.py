from line_bot_api import *
from events.basic import *
from events.oil import *

app = Flask(__name__)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(100)

    return 'OK'





@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = str(event.message.text).lower()

    if message_text == '使用說明':
        about_us_event(event)
    if message_text == '查詢功能' :
        Usage(event)
    if event.message.text == '小幫手' :
        abc(event)
###################################################################
    if message_text == '油價' :
        oil_price(event)
    # if event.message.text == "油價" :
    #     content = oil_price()
    #     line_bot_api.reply_message(
    #         event.reply_token , 
    #         TextSendMessage(text = content))
        

@handler.add(FollowEvent)
def handke_follow(event):
    welcome_msg = """Hello! 您好 歡迎成為 Master Finance 的好友!
    
我是 財金小助手

-這裡有股票 匯率資訊
-直接點選下方 途中 選單功能
-期待您的光臨!"""
    line_bot_api.reply_message(
        event.reply_token , 
        TextSendMessage(text = welcome_msg))
    
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)

if __name__ == "__main__":
    app.run()