from skpy import Skype

def its_your_again(text):
    res = ''
    words = text.split(' ')
    if len(words) > 4:
        res = "Чёт ты распизделся..."
    return res

sk = Skype('anton_galanin','***************')
sk.user
contact = 'in__the__mirror'
con = sk.contacts[contact]
ch=con.chat
ch=str(ch)
res = ch.split('\n')
chat_id = res[1]
chat_id=chat_id[4:]

while True:
    try:
        chat = sk.chats[chat_id]
        messages = chat.getMsgs()
        last_message = messages[0]
        #print(last_message)
        last_message=str(last_message)
        res = last_message.split('\n')
        res = res[-1]
        #print(res)
        last_message_text = res[9:]
        print(contact,': ',last_message_text)
        answer = its_your_again(last_message_text)
        if answer!='':
                chat.sendMsg(answer)
        print('you', ': ', answer)
    except:
        pass



