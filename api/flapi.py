from flask import Flask, Response, request, redirect, url_for

app = Flask(__name__)

@app.route('/api/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/api/unsuccess/<name>')
def unsuccess(name):
   return '%s were rejected' % name

@app.route('/api/login',methods = ['POST', 'GET'])
def login():
  if request.method == 'POST':
      user = request.form['nm']
      passwd = request.form['passwd']
  else:
      user = request.args.get('nm')
      passwd = request.args.get('passwd')
  if user == passwd:
      return redirect(url_for('success',name = user))
  else:
      return redirect(url_for('unsuccess', name = user))

@app.route('/api/index')
def home():
  return 'Home Page Route!!'

@app.route('/api/about')
def about():
  return 'About Page Route'

@app.route('/api/portfolio')
def portfolio():
  return 'Portfolio Page Route'

@app.route('/api/contact')
def contact():
  return 'Contact Page Route'

@app.route('/api/status')
def api():
  with open('../data.json', mode='r') as my_file:
    text = my_file.read()
    print("text=", text)
    return text

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  print(request.args)
  key = request.args.get('key')
  return Response("<h1>Flask</h1><p>Now: /%s</p><p>Maybe: /%s/</p><p>key=%s</p>" % (path, path, key), mimetype="text/html")

if __name__ == "__main__":
    app.run(debug = True)