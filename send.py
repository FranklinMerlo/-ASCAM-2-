#canoobclmyijuuhi

import yagmail
import time

def sendmail():
  for i in range(100):
  
    user = 'therealfreduniversity@gmail.com'
    app_password = 'canoobclmyijuuhi' # a token for gmail
    to = ['mlfarrin@buffalo.edu', 'notharrisonhutton2@gmail.com'] #Any targets go here
  
    subject = 'ATTENTION!!!' + '------------------------------------' + str(time.time()) #This ensures every email is fresh and new, not a chain
    f = open('completed.txt', 'r')
    response = f.read()
    f.close()
    content = [response]
  
    with yagmail.SMTP(user, app_password) as yag:
      for name in to:
        yag.send(name, subject, content)
        print('Sent email successfully')


