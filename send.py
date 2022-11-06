#tpdgpzbbkvjybhby

import yagmail

def sendmail():

  user = 'realbusinessproposal@gmail.com'
  app_password = 'tpdgpzbbkvjybhby' # a token for gmail
  to = ['notharrisonhutton2@gmail.com']

  subject = 'ATTENTION'
  f = open('completed.txt', 'r')
  response = f.read()
  f.close()
  content = [response]

  with yagmail.SMTP(user, app_password) as yag:
    for name in to:
      yag.send(name, subject, content)
      print('Sent email successfully')