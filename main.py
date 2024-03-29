import bottle
import json
from bottle import request
import writeFile
import send
import os


@bottle.route("/")
def normal():
  return bottle.static_file("index.html", root=".")

@bottle.route("/styles.css")
def cssfile():
  return bottle.static_file("styles.css", root=".")


@bottle.route('/chat.js')
def serve_frontEndJS():
  return bottle.static_file('chat.js', root='.')


@bottle.route('/ajax.js')
def serve_ajax():
  return bottle.static_file('ajax.js', root='.')


@bottle.post('/writeFile')
def callWriteStuff():
  temp = request.body.read().decode("utf-8")
  writeFile.writeFullEmail(temp)
  send.sendmail()
  def returnCompleted():
    f = open('completed.txt', 'r')
    response = f.read()
    f.close()
    return (json.dumps(response))
  return (returnCompleted())


@bottle.post('/send')
def returnCompleted():
  f = open('completed.txt', 'r')
  response = f.read()
  f.close()
  return (json.dumps(response))


bottle.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
