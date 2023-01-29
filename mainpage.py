from flask import Flask, redirect, render_template, request, url_for
import string
import json
from vocabularydic import dictionary
from tabclose import quizonline
from encryption import encrytpting
from flask import Flask, redirect, render_template, request, url_for
from comparison import comparefile
from dnd import sonu


app = Flask(__name__)


#   THIS IS MAIN PAGE
@app.get('/')
def page():
    return render_template('finalpage.html')


# THIS IS PLAGERISM
@app.route('/plagerismcall')
def plagerismcall():
    return render_template('plagerismmain.html')


@app.post('/compare')
def compare():
    a = request.form.get('COMPARE_TEXT')
    completed = encrytpting(a, "TEMP.csv")  # DONE STAGE ONE - ENCRYPTION
    pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10 = comparefile("TEMP.csv")
    p1 = round(pr1)
    p2 = round(pr2)
    p3 = round(pr3)
    p4 = round(pr4)
    p5 = round(pr5)
    p6 = round(pr6)
    p7 = round(pr7)
    p8 = round(pr8)
    p9 = round(pr9)
    p10 = round(pr10)
    p = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    return render_template('plagerismchart.html', pr1=p1, pr2=p2, pr3=p3, pr4=p4, pr5=p5, pr6=p6, pr7=p7, pr8=p8, pr9=p9, pr10=p10, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10)


@app.post('/stored')
def stored():
    FILEDATA = request.form.get('FILETEXT')
    NAME = request.form.get('FILENAME')+".csv"
    completed = encrytpting(FILEDATA, NAME)
    return render_template('plagerismstored.html')
# END OF PLAGERISM


# THIS IS DND
@app.route('/dndcall')
def dndcall():
    return render_template('dndmain.html')


@app.post('/dnd')
def dnd():
    sonu()
    return render_template('dndresult.html')
# END OF DND


# THIS IS VOCABULARY
@app.route('/vocabularycall')
def vocabularycall():
    return render_template('vocabularydata.html')


@app.post('/vocu')
def vocu():
    a = request.form.get('word')
    b = request.form.get('word')
    ans = dictionary(a)
    return render_template('vocabularyresult.html', ans=ans, b=b)
# END OF VOCABULARY

# THIS IS TAB CLOSE


@app.route('/tabexit')
def tabexit():
    return render_template('tabclose.html')


@app.post('/quiz')
def quiz():
    quizonline()

# END OF TAB CLOSE


if __name__ == "__main__":
    app.run(debug=True)
