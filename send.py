#cljuacexlfvgcxza

import yagmail
import time

def sendmail():
  for i in range(30):
  
    user = 'notarealbusinessorami@gmail.com'
    app_password = 'cljuacexlfvgcxza' # a token for gmail
    to = ['mables1026@gmail.com', 'michaelhorvath896@gmail.com'] #Any targets go here
  
    subject = 'ATTENTION!!!' + '------------------------------------' + str(time.time()) #This ensures every email is fresh and new, not a chain
    f = open('completed.txt', 'r')
    response = f.read()
    f.close()
    content = [response]
  
    with yagmail.SMTP(user, app_password) as yag:
      for name in to:
        yag.send(name, subject, content)
        print('Sent email successfully')


