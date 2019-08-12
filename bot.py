from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random

def send_message(message=None, attachment=None):
  vk_session.method('messages.send', {"user_id": event.user_id, "message": message, "attachment": attachment, "random_id": random.randint(-2147483648,+2147483648)})
  
def send_chat(message=None, attachment=None):
  vk_session.method('messages.send', {"chat_id": event.chat_id, "message": message, "attachment": attachment "random_id": random.randint(-2147483648,+2147483648)})

token = "YourToken" 
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
        print('Пользователь с id:' +str(event.user_id) +"запросил команду " +str(response))
        if(response == 'бот' or 'bot'):
          send_message(message="Бот работает исправно.", attachment="photo-184588235_457239048")
      elif(event.from_chat and not event.from_me):
        message = input('Введите сообщение в ответ: ')
        send_chat(message)
