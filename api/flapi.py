from flask import Flask, Response, request, redirect, url_for

app = Flask(__name__)

@app.route('/api/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/api/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

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
    return text

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  print(request.args)
  key = request.args.get('key')
  return Response("<h1>Flask</h1><p>You visited: /%s</p><p>key=%s</p>" % (path, key), mimetype="text/html")

if __name__ == "__main__":
    app.run(debug = True)