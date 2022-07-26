from turtle import pos
from flask import Flask, render_template, request, send_file
import pandas as pd
from pathlib import Path
from getData import getTopTenMain
from flask_sqlalchemy import SQLAlchemy

'''
TODO:
* change font ~
* Add buttons to a change parts of speech ~
* explore why good and great show up so much in every period
* find out why dots are still in the text ~
* make sure order is correct  and date split order is correct
* check and see why tobacco is showing up as adj or 'j'
* change divers to diverse in lemmas ~
* get buttons to scale
* Add all button

'''

app = Flask(__name__)


db_name = 'both.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class BOTH(db.Model):
    __tablename__ = 'BOTH'
    key = db.Column(db.String,primary_key=True)
    commodity = db.Column(db.String)
    period = db.Column(db.String)
    pos = db.Column(db.String)
    word_num = db.Column(db.String)
    value = db.Column(db.String)




@app.route('/', methods = ['POST', 'GET'])
def form():
    posDict = {'j': 'Adj\'s',
               'n': 'Nouns',
               'a': 'Adverbs',
               'v': 'Verbs'}

    def assignColorsTobacco(p1,p2,p3,p4,p5,p6,p7):
        master = [i[0] for i in [p1+p2+p3+p4+p5+p6+p7][0]]
        seen =[]
        colors= ['#963636', '#965c36', '#968336', '#839636', '#5c9636', '#36965c',
         '#369683', '#368396', '#365c96', '#363696', '#5c3696', '#833696', '#963683',
          '#963659', '#963636', 'Olive', 'MidnightBlue', 'MistyRose'] #‘#369636‘
        c_idx = 0
        for period in [p1,p2,p3,p4,p5,p6,p7]:
            for idx, word in zip(range(len(period)),period):
                if master.count(word[0]) >=2 and word[0] not in [i[0] for i in seen]:
                    period[idx] = period[idx] + (colors[c_idx],)
                    seen.append((word[0],colors[c_idx]))
                    c_idx+=1
                elif master.count(word[0]) >=2 and word[0] in [i[0] for i in seen]:
                    period[idx] = period[idx] + (str(([x[1] for x in seen if x[0] ==word[0]][0])),)
                else:
                    period[idx] = period[idx] + ('#696969',)
        return p1,p2,p3,p4,p5,p6,p7

    def assignColorsOpium(p1,p2,p3,p4,p5):
        master = [i[0] for i in [p1+p2+p3+p4+p5][0]]
        seen =[]
        colors= ['#963636', '#965c36', '#968336', '#839636', '#5c9636', '#36965c',
            '#369683', '#368396', '#365c96', '#363696', '#5c3696', '#833696', '#963683',
            '#963659', '#963636', 'Olive', 'MidnightBlue', 'MistyRose'] #‘#369636‘
        c_idx = 0
        for period in [p1,p2,p3,p4,p5]:
            for idx, word in zip(range(len(period)),period):
                if master.count(word[0]) >=2 and word[0] not in [i[0] for i in seen]:
                    period[idx] = period[idx] + (colors[c_idx],)
                    seen.append((word[0],colors[c_idx]))
                    c_idx+=1
                elif master.count(word[0]) >=2 and word[0] in [i[0] for i in seen]:
                    period[idx] = period[idx] + (str(([x[1] for x in seen if x[0] ==word[0]][0])),)
                else:
                    period[idx] = period[idx] + ('#696969',)
        return p1,p2,p3,p4,p5

    try:

        if request.method == 'GET':
            pos='j'
            
            p1 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='1').all()]
            p2 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='2').all()]
            p3 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='3').all()]
            p4 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='4').all()]
            p5 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='5').all()]
            p6 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='6').all()]
            p7 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='7').all()]

            p1,p2,p3,p4,p5,p6,p7 = assignColorsTobacco(p1,p2,p3,p4,p5,p6,p7)

            return render_template('tobacco.html', pos=posDict[pos], date1=p1, date2=p2, date3=p3, date4=p4, 
                    date5=p5, date6=p6, date7=p7)


        if request.method == 'POST':
            if request.form.get('switch'): ####
                if request.form['action'] == 'Adjectives':
                    pos='j'
                    p1 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='1').all()]
                    p2 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='2').all()]
                    p3 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='3').all()]
                    p4 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='4').all()]
                    p5 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='5').all()]
                    p6 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='6').all()]
                    p7 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='j',BOTH.period=='7').all()]

                    p1,p2,p3,p4,p5,p6,p7 = assignColorsTobacco(p1,p2,p3,p4,p5,p6,p7)

                    return render_template('tobacco.html', pos=posDict[pos], date1=p1, date2=p2, date3=p3, date4=p4, 
                            date5=p5, date6=p6, date7=p7)

                elif request.form['action'] == 'Nouns':
                    pos='n'
                    p1 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='n',BOTH.period=='1').all()]
                    p2 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='n',BOTH.period=='2').all()]
                    p3 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='n',BOTH.period=='3').all()]
                    p4 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='n',BOTH.period=='4').all()]
                    p5 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='n',BOTH.period=='5').all()]
                    p6 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='n',BOTH.period=='6').all()]
                    p7 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='n',BOTH.period=='7').all()]

                    p1,p2,p3,p4,p5,p6,p7 = assignColorsTobacco(p1,p2,p3,p4,p5,p6,p7)

                    return render_template('tobacco.html', pos=posDict[pos], date1=p1, date2=p2, date3=p3, date4=p4, 
                            date5=p5, date6=p6, date7=p7)
    
                elif request.form['action'] == 'Verbs':
                    pos='v'
                    p1 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='v',BOTH.period=='1').all()]
                    p2 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='v',BOTH.period=='2').all()]
                    p3 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='v',BOTH.period=='3').all()]
                    p4 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='v',BOTH.period=='4').all()]
                    p5 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='v',BOTH.period=='5').all()]
                    p6 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='v',BOTH.period=='6').all()]
                    p7 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='v',BOTH.period=='7').all()]

                    p1,p2,p3,p4,p5,p6,p7 = assignColorsTobacco(p1,p2,p3,p4,p5,p6,p7)

                    return render_template('tobacco.html', pos=posDict[pos], date1=p1, date2=p2, date3=p3, date4=p4, 
                            date5=p5, date6=p6, date7=p7)

                elif request.form['action'] == 'Adverbs':
                    pos='a'
                    p1 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='a',BOTH.period=='1').all()]
                    p2 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='a',BOTH.period=='2').all()]
                    p3 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='a',BOTH.period=='3').all()]
                    p4 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='a',BOTH.period=='4').all()]
                    p5 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='a',BOTH.period=='5').all()]
                    p6 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='a',BOTH.period=='6').all()]
                    p7 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='t',BOTH.pos=='a',BOTH.period=='7').all()]

                    p1,p2,p3,p4,p5,p6,p7 = assignColorsTobacco(p1,p2,p3,p4,p5,p6,p7)

                    return render_template('tobacco.html', pos=posDict[pos], date1=p1, date2=p2, date3=p3, date4=p4, 
                            date5=p5, date6=p6, date7=p7)


            else:
                if request.form['action'] == 'Adjectives':
                    pos='j'
                    
                    p1 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='j',BOTH.period=='1').all()]
                    p2 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='j',BOTH.period=='2').all()]
                    p3 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='j',BOTH.period=='3').all()]
                    p4 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='j',BOTH.period=='4').all()]
                    p5 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='j',BOTH.period=='5').all()]


                    p1,p2,p3,p4,p5 = assignColorsOpium(p1,p2,p3,p4,p5)

                    return render_template('opium.html', pos=posDict[pos], date1=p1, date2=p2, date3=p3, date4=p4, 
                            date5=p5)

                elif request.form['action'] == 'Nouns':       
                    pos='n'
                    
                    p1 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='n',BOTH.period=='1').all()]
                    p2 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='n',BOTH.period=='2').all()]
                    p3 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='n',BOTH.period=='3').all()]
                    p4 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='n',BOTH.period=='4').all()]
                    p5 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='n',BOTH.period=='5').all()]


                    p1,p2,p3,p4,p5 = assignColorsOpium(p1,p2,p3,p4,p5)

                    return render_template('opium.html', pos=posDict[pos], date1=p1, date2=p2, date3=p3, date4=p4, 
                            date5=p5)

                elif request.form['action'] == 'Verbs':
                    
                    pos='v'
                    
                    p1 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='v',BOTH.period=='1').all()]
                    p2 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='v',BOTH.period=='2').all()]
                    p3 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='v',BOTH.period=='3').all()]
                    p4 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='v',BOTH.period=='4').all()]
                    p5 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='v',BOTH.period=='5').all()]


                    p1,p2,p3,p4,p5 = assignColorsOpium(p1,p2,p3,p4,p5)

                    return render_template('opium.html', pos=posDict[pos], date1=p1, date2=p2, date3=p3, date4=p4, 
                            date5=p5)

                elif request.form['action'] == 'Adverbs':   
                    pos='a'
                    
                    p1 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='a',BOTH.period=='1').all()]
                    p2 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='a',BOTH.period=='2').all()]
                    p3 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='a',BOTH.period=='3').all()]
                    p4 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='a',BOTH.period=='4').all()]
                    p5 = [(i.value,) for i in BOTH.query.filter(BOTH.commodity=='o',BOTH.pos=='a',BOTH.period=='5').all()]


                    p1,p2,p3,p4,p5 = assignColorsOpium(p1,p2,p3,p4,p5)

                    return render_template('opium.html', pos=posDict[pos], date1=p1, date2=p2, date3=p3, date4=p4, 
                            date5=p5)



    except Exception as e:
        # e holds description of the error
        error_text = '<p>The error:<br>' + str(e) + '</p>'
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text



if __name__ == '__main__':
    app.run(debug=True)