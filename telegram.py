import time, datetime
import telepot
from telepot.loop import MessageLoop


def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text'] #to get the only text of the message
    print (command)

    if 'hi' in command:
        ab = 'hello shivam'
        telegram_bot.sendMessage(chat_id, ab) #to send the message to bot
    if 'members' in command:
        ab = 'Shivam,Sayali,Praveen'
        telegram_bot.sendMessage(chat_id, ab)
    if 'photo' in command:
        pic = 'https://cdn.pixabay.com/photo/2016/06/18/17/42/image-1465348_960_720.jpg'
        telegram_bot.sendPhoto(chat_id, pic) # to send image to the bot


telegram_bot = telepot.Bot('Access token') #paste the access token in this area
print (telegram_bot.getMe())

a = MessageLoop(telegram_bot, action).run_as_thread()
print ('up and runing')

while 1:
    time.sleep(10)
