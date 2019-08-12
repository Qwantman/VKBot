from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
import time
import os
def check_status():
  if(res == 1):
    return 1
  else:
    return 2
def send_message(message=None, attachment=None):
  vk_session.method('messages.send', {"user_id": event.user_id, "message": message, "attachment": attachment, "random_id": random.randint(-2147483648,+2147483648)})
#для ЛС
def send_chat(message=None, attachment=None):
  vk_session.method('messages.send', {"chat_id": event.chat_id, "message": message, "attachment": attachment, "random_id": random.randint(-2147483648,+2147483648)})
#для беседок
adminlist=['525009136']
token = "d18d76cc11b8c219d368cd861818c86821ec2b595d9bd9dbf1ff804dfbd2185c9826696e48accd3c0364c"
vk_session = vk_api.VkApi(token = token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
start_time = time.monotonic()
print('Бот запущен!')
res = 1
#если не выдало ошибок, тогда ща пойдут логи если кто-то напишет
while True:
  for event in longpoll.listen():
    if(event.type == VkEventType.MESSAGE_NEW):
      response = event.text.lower()
      if(event.from_user and not event.from_me):
        print('Пользователь с id: ' +str(event.user_id) +" запросил: " +str(response))
        if(response == 'бот'):
          send_message(message="Бот работает исправно.", attachment="photo-184588235_457239048")
        elif(response == 'аптайм'):
          send_message(message='С момента запуска прошло: ' +str(int(time.monotonic() - start_time)) +' секунд', attachment='photo-184588235_457239049')
        elif(response == 'помощь'):
          send_message(message='''
          Бот - проверка роботоспособности.
          Для админов:
          Аптайм - выдаёт время с момента запуска
          Статус - выдаёт статус хостинга бота и рабочую директорию
          ''')
        elif(response == 'статус'):
          if(str(event.user_id) in adminlist):
            dir=os.getcwd()
            stat = check_status()
            if(stat == 1):
              stat = 'OK'
            else:
              stat = 'NOT OK'
            send_message(message="Рабочая директория - " +str(dir) +'\n Статус бота - ' +stat)
          else:
            send_message(message='Не хватает прав!')
        else:
          text = 'Команда введена не верно'
          print(text)
          send_message(message=text)
      elif(event.from_chat and not event.from_me):
        message = input('Введите сообщение в ответ: ')
        send_chat(message=message)

