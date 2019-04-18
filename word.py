from DBcm import useDatabase, ConnectionError, CredentialsError
from flask import Flask, render_template, request, escape, session
from flask import copy_current_request_context
from checker import check_logged_in
from funtions import search4letters
from threading import Thread
from time import sleep 

app = Flask(__name__)
app.config['dbconfig'] = {'host':'127.0.0.1', 'user':'root', 'database':'wordlogdb',}


@app.route('/search', methods=['POST'])
def do_search() -> 'html':
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        sleep(15) # This makes log_request to delay for 15 seconds
        '''Log details of the web request and the results '''
        with useDatabase(app.config['dbconfig']) as cursor:
            _SQL = '''insert into log (phrase, letters, ip, browser_string, results) values (%s,%s,%s,%s,%s) '''
            cursor.execute(_SQL,(req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res, ))


    phrase= request.form['phrase']
    letters= request.form['letters'] 
    title= 'Here are your results: '
    results= str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
        
    except Exception as err:
        print('****Logging failed with this error : ',str(err))
    return render_template('result.html',
                            the_phrase= phrase,
			    the_letters= letters,
			    the_title=title,
			    the_results= results,)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
			    the_title='Welcome to this page')


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
    app.run(debug=True)