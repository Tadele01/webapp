from flask import Flask, session
from checker import check_logged_in
app = Flask(__name__)

@app.route('/')
def index()-> str:
    return 'this is the index page '

@app.route('/page1')
@check_logged_in
def page1()-> str:
    return 'this is the page1 '
@app.route('/page2')
@check_logged_in
def page2()-> str:
    return 'this is the page2 '
@app.route('/page3')
@check_logged_in
def page3()-> str:
    return 'this is the page3 '

@app.route('/login')
def do_login()-> str:
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def do_logout()-> str:
    session.pop('logged_in')
    return 'You are now logged out'

app.secret_key = 'YouWillNeverGuessMysecretKey'
if __name__ == '__main__':
    app.run(debug = True)
