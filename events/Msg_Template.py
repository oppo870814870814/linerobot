from line_bot_api import *

def stock_reply_other(stockNumber):
    content_text = "及時股價和K線圖"
    text_message = TextSendMessage(
                                text = content_text , 
                                quick_reply = QuickReply(
                                    items = [
                                        QuickReplyButton(
                                                action = MessageAction(
                                                    label = "即時股價" , 
                                                    text = "#" + stockNumber , 
                                                )   
                                        ) ,
                                        QuickReplyButton (
                                                action = MessageAction(
                                                    label = "K線圖" , 
                                                    text = "@K" + stockNumber
                                                )
                                        ),
                                    ]
                                ))
    return text_message


# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/7qKEALz.jpg",
    "position": "relative",
    "size": "full"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "幣別種類",
        "weight": "bold",
        "size": "xl",
        "color": "#AA2B1D"
      }
    ],
    "background": {
      "type": "linearGradient",
      "angle": "0deg",
      "startColor": "#000000",
      "endColor": "#ffffff"
    }
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "美金",
              "text": "USD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "日圓",
              "text": "JPY"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "港幣",
              "text": "HKD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#000000",
          "endColor": "#ffffff"
        }
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "英鎊",
              "text": "GBP"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "澳幣",
              "text": "AUD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "加拿大幣",
              "text": "CAD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#000000",
          "endColor": "#ffffff"
        }
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "瑞士法郎",
              "text": "CHF"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "新加坡",
              "text": "SGD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "南非幣",
              "text": "ZAR"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#000000",
          "endColor": "#ffffff"
        }
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "瑞典幣",
              "text": "SEK"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "泰幣",
              "text": "THB"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "菲比索",
              "text": "PHP"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#000000",
          "endColor": "#ffffff"
        }
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "印尼幣",
              "text": "IDR"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "韓元",
              "text": "KRW"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "馬來幣",
              "text": "MYR"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#000000",
          "endColor": "#ffffff"
        }
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "越南盾",
              "text": "VND"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "人民幣",
              "text": "CNY"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "紐元",
              "text": "NZD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#97CBFF",
            "margin": "sm"
          }
        ],
        "background": {
          "type": "linearGradient",
          "angle": "0deg",
          "startColor": "#000000",
          "endColor": "#ffffff"
        }
      }
    ],
    "background": {
      "type": "linearGradient",
      "angle": "0deg",
      "startColor": "#000000",
      "endColor": "#ffffff"
    }
  }
}
                    
    )
    return flex_message