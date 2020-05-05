from flask import Flask, render_template, redirect, url_for
from wtforms import Form, StringField, IntegerField, validators

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')  

class BirthdayForm(Form):
    day = IntegerField('Day', [validators.NumberRange(min=1, max=31, message=_(u"Enter a valid date"))])  
    month = StringField('Month', [validators.Length(max=10, message=_(u"Enter a valid month"))])  

@app.route('/horoscope', methods=['GET', 'POST'])    
def getSign():
    form = BirthdayForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('horoscope.html')
    return render_template('horoscope.html', form=form) 

if __name__ == '__main__':
    app.run(debug=True)
