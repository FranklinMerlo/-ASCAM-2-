#tpdgpzbbkvjybhby

import yagmail
import time

coolcount = 0

def sendmail():
  user = 'realbusinessproposal@gmail.com'
  app_password = 'tpdgpzbbkvjybhby' # a token for gmail
  to = ['merlof22storage@gmail.com', 'mables1026@gmail.com', 'michaelhorvath896@gmail.com', 'mattdcir@gmail.com', 'fjmerlo@buffalo.edu']

  subject = 'ATTENTION!!!' + '------------------------------------' + str(time.time())
  f = open('completed.txt', 'r')
  response = f.read()
  f.close()
  content = [response]

  with yagmail.SMTP(user, app_password) as yag:
    for name in to:
      yag.send(name, subject, content)
      print('Sent email successfully')
