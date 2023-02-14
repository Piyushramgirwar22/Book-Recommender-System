from flask import Flask, render_template, url_for, redirect,request
import pandas as pd
from data_dao import visits
from data_dao import recommend_books
from data_dao import year_range

########### Data Work ###############
df = pd.read_csv(r'C:\Users\lenovo\OneDrive\Desktop\book reccomender\app_folder\goodreads.csv')
########### flask app ##############

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    data = df.T.to_dict().values()
    return render_template('new.html', data = data)

@app.route('/home')
def Home():
    data = df.T.to_dict().values()
    return render_template('new.html', data = data)

@app.route('/low')
def low():
    data = visits("less visited",df)
    return render_template('new.html', data = data)

@app.route('/medium')
def medium():
    data = visits("average visited",df)
    return render_template('new.html', data = data)

@app.route('/high')
def high():
    data = visits("highely visited",df)
    return render_template('new.html', data = data)

@app.route('/year_one')
def year_one():
    data = year_range(1600,1900,df)
    return render_template('new.html', data = data)

@app.route('/year_two')
def year_two():
    data = year_range(1900,2000,df)
    return render_template('new.html', data = data)

@app.route('/year_three')
def year_three():
    data = year_range(2000,3000,df)
    return render_template('new.html', data = data)

@app.route('/movies',methods=['POST'])
def movie():
    if request.method == 'POST':
        data = recommend_books(request.form['search movie'],df)
        return render_template('new.html', data = data)







if __name__ == '__main__':
    app.run(debug = True)