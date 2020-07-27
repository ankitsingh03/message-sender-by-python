import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo,showerror

def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'jsE4OYzAIpMKkVbGhS92L5qJ70nfCctXxePvFDwlW1o6UR8BQuVNjh7fOSYQnTDHcqyUiumG56Lbzpr1',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')

def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0",END)
    a = send_sms(num, msg)
    if a:
        showinfo("send success","successfully sent")
    else:
        showerror("Error", "something went wrong")

#GUI
root = Tk()
root.title("Message Sender")
root.geometry("400x550")
font = ("helvetica", 22, 'bold')

textNumber = Entry(root,font= font)
textNumber.pack(fill=X, pady=20)

textMsg = Text(root)
textMsg.pack(fill=X)

sendBtn = Button(root, text="SEND SMS",command= btn_click)
sendBtn.pack()

root.mainloop()
