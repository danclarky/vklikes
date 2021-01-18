import requests
import vk_api.vk_api
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from datetime import datetime,timedelta

vk_session_bot = vk_api.VkApi(token='token')
vk_bot = vk_session_bot.get_api()


vk_session = vk_api.VkApi(login='login',password='pass')

try:
vk_session.auth()
except vk_api.AuthError as error_msg:
    print(error_msg)

longpoll = VkBotLongPoll(vk_session, id)

vk = vk_session.get_api()



count = 20
idminus = -id
id = id
now = datetime.now()
week = now + timedelta(-8)




wallget=vk.wall.search(owner_id=idminus,count=count,query='www.ru',filter='owner')
posts=wallget['items']
message=""

listkpk = [***]
for post in posts: 
    
    if post['text'].find('kpk-finansyst') != -1: 
        ts = datetime.fromtimestamp(int(post['date']))
        if ts>=week and ts<=now:
            messagelike='Не лайкнули из сотрудников:\n'
            messagereply='Не репостнули из сотрудников:\n'
            likeslist=[]
            replylist=[]
            idpost=post['id']
            message += 'Запись https://vk.com/kpk_fin?w=wall-'+str(id)+'_'+str(idpost)+'\n'
            likesgetlist=vk.likes.getList(type='post',owner_id=idminus,item_id=idpost,filter='likes',extended='1')
            countlikes = likesgetlist['count']
            if countlikes !=0:
                likes = likesgetlist['items']
                for like in likes:
                    likeslist.append(like['id'])
            likesdiff=list(set(listkpk)-set(likeslist))
            for el in likesdiff:
                usersgetlikes=vk.users.get(user_ids=el)
                for user in usersgetlikes:
                    if user['first_name'] != 'DELETED':
                        messagelike += user['first_name']+' '+user['last_name']+'\n'

                

            replygetlist=vk.likes.getList(type='post',owner_id=idminus,item_id=idpost,filter='copies',extended='1')
            countreples = replygetlist['count']
            if countreples !=0:
  
                reples = replygetlist['items']
                for reply in reples:

                    replylist.append(reply['id']) 

            replydiff=list(set(listkpk)-set(replylist))
            for el in replydiff:
                usersgetreply=vk.users.get(user_ids=el)
                for user in usersgetreply:
                    if user['first_name'] == 'DELETED':
                        groupsgetreply=vk.groups.getById(group_ids=el)
                        for group in groupsgetreply:
                            messagereply+=group['name']+'\n'
                    else:
                        messagereply += user['first_name']+' '+user['last_name']+'\n'    
                
            message = message+messagelike + messagereply
        
print(message)




vk_bot.messages.send(peer_id='id',random_id = 0, message=message)













