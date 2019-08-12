from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
import time
event=' '
event.text=' '
def send_message(message=None, attachment=None):
  vk_session.method('messages.send', {"user_id": event.user_id, "message": message, "attachment": attachment, "random_id": random.randint(-2147483648,+2147483648)})
#для ЛС
def send_chat(message=None, attachment=None):
  vk_session.method('messages.send', {"chat_id": event.chat_id, "message": message, "attachment": attachment, "random_id": random.randint(-2147483648,+2147483648)})
#для беседок
token = "d18d76cc11b8c219d368cd861818c86821ec2b595d9bd9dbf1ff804dfbd2185c9826696e48accd3c0364c"
vk_session = vk_api.VkApi(token = token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
start_time = time.monotonic()
print('Бот запущен!')
#если не выдало ошибок, тогда ща пойдут логи если кто-то напишет
while(event.text.lower() != 'выкл' or 'off'):
  for event in longpoll.listen():
    if(event.type == VkEventType.MESSAGE_NEW):
      print('Текст сообщения: '+ str(event.text))
      response = event.text.lower()
      if(event.from_user and not event.from_me):
        print('Пользователь с id: ' +str(event.user_id) +" запросил: " +str(response))
        if(response == 'бот' or 'bot'):
          send_message(message="Бот работает исправно.", attachment="photo-184588235_457239048")
        elif(response == 'аптайм' or 'uptime'):
          send_message(message='Прошло: ' +str(int(time.monotonic() - start_time)), attachment='photo-184588235_457239049')
        else:
          text = 'Комманда введена не верно'
          print(text)
          send_message(message=text)
      elif(event.from_chat and not event.from_me):
        message = input('Введите сообщение в ответ: ')
        send_chat(message=message)

