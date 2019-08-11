from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
token = "d18d76cc11b8c219d368cd861818c86821ec2b595d9bd9dbf1ff804dfbd2185c9826696e48accd3c0364c" 
vk_session = vk_api.VkApi(token = token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
print('Бот запущен!')
while True:
  for event in longpoll.listen():
    if(event.type == VkEventType.MESSAGE_NEW):
      print('Текст сообщения: '+ str(event.text))
    if(event.t):
      vk.session.method('messages.send')
