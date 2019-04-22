from DBcm import useDatabase, ConnectionError, CredentialsError
from flask import Flask, render_template, request, escape, session
from flask import copy_current_request_context
from checker import check_logged_in
from funtions import search4letters
from threading import Thread
from time import sleep 
import categorizer
import ai_classifier
import math

app = Flask(__name__)
app.config['dbconfig'] = {'host':'127.0.0.1', 'user':'root', 'database':'wordlogdb',}


global_var = 0
@app.route('/search', methods=['POST'])
def do_search() -> 'html':
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        
        '''Log details of the web request and the results '''
        with useDatabase(app.config['dbconfig']) as cursor:
            _SQL = '''insert into log(phrase, letters) values (%s,%s,%) '''
            category = types.type_of_interst()
            cursor.execute(_SQL,(req.form['phrase'] ,category,res))


    phrase= request.form['phrase']
    global_var = request.form['phrase']
    category = categorizer.type_of_interset()
    ai_classifier_fake = ai_classifier.fake_guesser()
    ai_classifier_real = ai_classifier.real_guesser()
    return render_template('questions.html',
                            the_phrase= phrase,
			    the_results= category,
                            the_ai_real = ai_classifier_fake ,
                            the_ai_fake = ai_classifier_real,
			    )

@app.route('/author_post', methods=['POST'])
def do_author_post() -> 'html':
   
    phrase= request.form['phrase']
    global_var = request.form['phrase']
    author_name = request.form['name']
    category = categorizer.type_of_interset()
    return render_template('index.html',
                            the_phrase= phrase,
			    the_results= category,
                            the_author_name = author_name,
			    )

@app.route('/author_post')
def do_author_get() ->'html':
    return render_template('authorReply.html')

@app.route('/facebook_request',  methods=['POST'])
def do_fb_request() -> 'html':
    phrase= request.form['phrase']
    global_var = request.form['phrase']
    category = categorizer.type_of_interset()
    ai_classifier_fake = ai_classifier.fake_guesser()
    ai_classifier_real = ai_classifier.real_guesser()
    return render_template('questions.html',
                            the_phrase= phrase,
			    the_results= category,
                            the_ai_real = ai_classifier_fake ,
                            the_ai_fake = ai_classifier_real,
			    )

def global_return():
    return global_var
    
@app.route('/')
def entry_page() -> 'html':
    return render_template('addis.html')

@app.route('/index')
def index_page()-> 'html':
    return render_template('index.html')


@app.route('/submitQuestions')
def question_page() -> 'html':
    return render_template('submitQuestions.html')

@app.route('/author_reply')
@check_logged_in
def author_reply() -> 'html':
    return render_template('authorReply.html')

@app.route('/login')
def do_login()-> str:
    session['logged_in'] = True
    return render_template('authorReply.html')

@app.route('/logout')
def do_logout()-> str:
    session.pop('logged_in')
    return render_template('index.html')

@app.route('/apply')
def apply() -> 'html':
    return render_template('apply.html')

@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    try:
        with useDatabase(app.config['dbconfig']) as cursor:
            _SQL = '''select phrase, letters, ip, browser_string, results from log '''
            cursor.execute(_SQL)
            contents = cursor.fetchall()   
        titles = ('phrase','letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                                the_title='View Log',
                                the_row_titles= titles,
                                the_data= contents,)
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
        print('user or password is incorrect : ', str(err))
    except SQLError as err:
        print('Is your query correct ? : ',str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'Error'
    '''with open('wordsearch.log') as log:
        for line in log: 
            contents.append([])
            for item in line.split('|'): 
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles= titles,
                            the_data= contents,)'''
  


app.secret_key = 'YouWillNeverGuessMysecretKey'

    
if __name__ == '__main__':
    app.run(debug=True)