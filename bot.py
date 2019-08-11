from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
from datetime import datetime

def send_message(message):
  vk_session.method('messages.send', {"user_id": event.user_id, "message": message, "random_id": random.randint(-2147483648,+2147483648)})

def send_chat_msg(message):
  vk_session.method('messages.send', {"chat_id": event.chat_id, "message": message, "random_id": random.randint(-2147483648,+2147483648)})

token = "d18d76cc11b8c219d368cd861818c86821ec2b595d9bd9dbf1ff804dfbd2185c9826696e48accd3c0364c" 
vk_session = vk_api.VkApi(token = token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
print('Бот запущен!')
while True:
  for event in longpoll.listen():
    if(event.type == VkEventType.MESSAGE_NEW):
      print('Текст сообщения: '+ str(event.text))
      response = event.text.lower()
      if(event.from_user and not event.from_me):
        if(response != ' '):
          if(response != ' '):
            break
        else:
          message = input('Введите сообщение в ответ: ')
          try: 
            send_message(message)
          except:
            send_chat_msg(message)
