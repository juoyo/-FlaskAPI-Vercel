from flask import Flask, Response, request, redirect, url_for

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/index/')
def home():
  return 'Home Page Route!!'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  print(request.args)
  key = request.args.get('key')
  return Response("<h1>Flask</h1><p>You visited: /%s</p><p>key=%s</p>" % (path, key), mimetype="text/html")

@app.route('/about/')
def about():
  return 'About Page Route'

@app.route('/portfolio')
def portfolio():
  return 'Portfolio Page Route'

@app.route('/contact')
def contact():
  return 'Contact Page Route'

@app.route('/status')
def api():
  with open('../data.json', mode='r') as my_file:
    text = my_file.read()
    return text

  
if __name__ == "__main__":
    app.run(debug = True)