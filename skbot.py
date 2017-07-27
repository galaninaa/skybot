from skpy import Skype
from time import sleep
import random
import datetime

banya_answers = ['На сл неделе может?','А я все равно не пойду','Да вы там опять бухать собрались','Антоха? ты как?За?',
                 'Просто с чайком посидим?',' да Перт чай опять не сможет',
                 'А кто у нас давно не мытый?','Ток давайте без пива','Что? давно не доминировали?','@BanyaBot ты тоже пойдешь?','@BanyaBot чо как там с баней?','@BanyaBot А тебя кто написал?']


def its_your_again(text):
    res = ''
    words = text.split(' ')
    if len(words) > 15:
        res = "Чёт ты распизделся..."

    return res
def abaut_banya(text, all_banya):

    res = ''
    text=str(text)
    text=text.lower()

    for choices in all_banya:
        #print(text)
        #print(choices)
        #print(text.find(choices),choices)
        if text.find(choices)!=-1:
            res = random.choice(banya_answers)
            break

    return res
def anailze_time(time, now_time):
    time = str(time)
    now_time = str(now_time)
    time= time.split(' ')
    now  = now_time.split(' ')
    if time[0]==now[0]:
        h_m_s_time = time[1].split(':')
        h_m_s_now = now[1].split(':')
        hour_h_m_s_time = int(h_m_s_time[0])
        hour_h_m_s_now = int(h_m_s_now[0])
        min_h_m_s_time = int(h_m_s_time[1])
        min_h_m_s_now = int(h_m_s_now[1])
        if (hour_h_m_s_time-hour_h_m_s_now==0 and  min_h_m_s_time-min_h_m_s_now<10) or (hour_h_m_s_time-hour_h_m_s_now==1 and min_h_m_s_time-min_h_m_s_now>50):
            return True
    else:
        return False

def banya_generator():
    banya = 'бан'
    all_words = []
    suf = ['','ьк','юшк' ]
    end = ['а','ой','е','и','ю','ей','ом','я']

    for i in range(len(suf)):
        for j in range(len(end)):
            all_words.append(banya+suf[i]+end[j])

    return all_words

all_banya = banya_generator()

#

sk = Skype('anton@talkme.im','181818Ag')
sleep(360)

chats = sk.chats.recent()

chats_id = []
for chat in chats:

    str_ch = str(chats[chat])
    if str_ch.find('SkypeGroupChat')==1:
        chats_id.append(str(chat))


while True:
    try:
        for chat_id in chats_id:
            chat = sk.chats[chat_id]
            messages = chat.getMsgs()
            last_message = messages[0]

            last_message=str(last_message)

            res = last_message.split('\n')
            time = res [3]
            time = time[6:]
            now_time = datetime.datetime.now()
            mes_time = anailze_time(time,now_time)
            if mes_time == True:
                if res[-3]!='UserId: live:anton_4154':
                    res = res[-1]
                    last_message_text = res[9:]
                    print('in chat: ',last_message_text)
                    answer, answer_2 = abaut_banya(last_message_text, all_banya), its_your_again(last_message_text)
                    if answer!='':
                        chat.sendMsg(answer)
                        print('you', ': ', answer)
                    elif answer_2 != '':
                        chat.sendMsg(answer_2)
                        print('you', ': ', answer)

    except:
        pass
