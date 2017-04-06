#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from qqbot import QQBotSlot as qqbotslot, RunBot


KEY = "f978f03fb6cc4707b9579c68a953060a"
user_id = "mingo"
#获取图灵机器人自动回复信息
def get_response(msg):
	#信息传送网址
	api_url = "http://www.tuling123.com/openapi/api"

	data = {
			'key' : KEY,
			'info' : msg,
			'userif' : user_id
			}
	try:
		#向图灵机器人发送请求
		r = requests.post(api_url,data=data).json()
		print "requests successfully"
		#返回自动回复信息
		return r.get('text')
	except:
		return "error in http requests"

@qqbotslot
def onQQMessage(bot, contact, member, content):
	if content == "-stop":
		bot.SendTo(contact, "qq_robot has stoped")
		bot.Stop()
	else:
		bot.SendTo(contact, get_response(content))

if __name__ == '__main__':
	RunBot()