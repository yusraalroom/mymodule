from flask import Flask, Response
from flask import request
import hashlib
import xmlrpclib
app = Flask(__name__)
salt = "UNIQUE_SALT"
default_name = 'test'
db = 'your database'
username = 'your user name'
password = 'your password'
@app.route('/', methods=['GET', 'POST'])
def mainpage():
    name = default_name
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
	common = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/2/common')
	uid = common.authenticate(db, username, password, {})
	find = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/2/object')
	find.execute_kw(db, uid, password, 'res.users', 'create', [{'name': '%s' % name,'login':'%s' % email}])
    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()

    header = '<html><head><title>Identidock</title></head><body>'
    body = '''<form method="POST">
              Name : <input type="text" name="name" >
	      Email : <input type="text" name="email" >
              <input type="submit" value="submit">
              </form>
              
           '''.format(name, name_hash)
    footer = '</body></html>'
    re = 'echo name'
    return header + body + footer +name + email
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


