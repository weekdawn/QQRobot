#coding=utf-8
from qqbot import QQBotSlot as qqbotslot, RunBot


i = '��ã�����QQ������'
j = 'QQ�������ѹر�'
@qqbotslot
def onQQMessage(bot, contact, member, content):
    if content == 'hello':
        bot.SendTo(contact, i.decode('gbk'))
    elif content == 'stop':
        bot.SendTo(contact, j.decode('gbk'))
        bot.Stop()

if __name__ == '__main__':
    RunBot()