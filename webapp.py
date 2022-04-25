import os
from flask import Flask, url_for, render_template, request, Markup
from flask import redirect
from flask import session

app = Flask(__name__)



app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def render_main():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear()
    return redirect('/')
@app.route('/p2',methods=['GET','POST'])
def render_page2():
    session["q1"]=request.form["q1"]
    print(session["q1"])

    return render_template('page2.html')

@app.route('/p3',methods=['GET','POST'])
def render_page3():
    session["q2"]=request.form["q2"]

    return render_template('page3.html')
    
@app.route('/p_final',methods=['GET','POST'])
def render_page_final():
    session["q3"]=request.form["q3"]
    answerFinal = ''
    i = 0
    if session["q1"] == '2':
        answerFinal = answerFinal + 'You got question 1 correct' + Markup('<br>')
        i += 1
    else:
        answerFinal = answerFinal + 'You got question 1 wrong' + Markup('<br>')
        
    if session["q2"] == 'b':
        answerFinal = answerFinal + 'You got question 2 correct' + Markup('<br>')
        i += 1
    else:
        answerFinal = answerFinal + 'You got question 2 wrong' + Markup('<br>')
        
    if session["q3"] == 'c':
        answerFinal = answerFinal + 'You got question 3 correct' + Markup('<br>')
        i += 1
    else:
        answerFinal = answerFinal + 'You got question 3 wrong' + Markup('<br>')
def last_score():
    
    return render_template('page_final.html', finalAnswer = answerFinal, finalScore = str(i))
if __name__=="__main__":
    app.run(debug=True)