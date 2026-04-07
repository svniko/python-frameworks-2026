import random
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__, 
            # template_folder="jinja_templates"
            )

app.config['SECRET_KEY'] = "09a3c518e4b652986a6d"

class FirstForm(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

pets = [
    {
        'species':'cat',
        'name':'Tom',
        'age':10,
        'color':'grey'
    },
    {
        'species':'cat',
        'name':'Barsyk',
        'age':5,
        'color':'white'
    },
    {
        'species':'dog',
        'name':'Patron',
        'age':7,
        'color':'brown'
    }
]


def init_game():
    session['you_win'] = 0
    session['comp_win'] = 0
    session['round'] = 0
    session['player_choice'] = None
    session['game_over'] = False

@app.route('/start/')
def start():
    init_game()
    return render_template('rsp.jinja2',
                           title='Game')  

@app.route('/select/<int:ch>')  
def select(ch):
    session['player_choice'] = ch
    return redirect(url_for('rsp'))


@app.route('/game/')
def rsp():
    if 'round' not in session:
        return redirect(url_for('start'))
    
    names = {0:"Rock", 1:"Scissors", 2:"Paper"}

    if session['player_choice'] is not None and session['round'] < 5:
        session['round'] += 1
        comp_choice = random.randint(0, 2)
        user_choice = session['player_choice']
        
        session['player_choice'] = None

        # if user_choice == comp_choice:
        #     flash(f'Нічія! Обидва обрали {names[user_choice]}', 'warning')
        # elif user_choice == 0 and comp_choice == 1:
                       
        #     # TO DO
        #     flash(f'Перемога', 'success')
        #     session['you_win'] += 1
        # else:
        #     flash('Програш', 'danger')
        #     session['comp_win'] += 1

        result = (user_choice - comp_choice) % 3

        if result == 0:
            flash(f'Нічія! Обидва обрали {names[user_choice]}', 'warning')
        elif result == 2:
            flash(f'Перемога', 'success')
            session['you_win'] += 1
        else:
            flash('Програш', 'danger')
            session['comp_win'] += 1
    


    if session['round'] == 5:
        session['game_over'] = True
        if session['you_win'] > session['comp_win']:
            flash('Вітаємо! Ви виграли', 'info')
        elif session['you_win'] < session['comp_win']:
            flash('Нажаль! Ви програли', 'info')
        else:
            flash('Тотальні нічія', 'info')

    return render_template('rsp.jinja2', title='Game',
                           round=session.get('round'),
                           y_win=session.get('you_win'),
                           c_win=session.get('comp_win'),
                           game_over=session.get('game_over')
                           )
             


    

@app.route("/lect5/", methods=["GET", "POST"])
def lecture5():
    name = None
    form = FirstForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template("lecture5.jinja2",
                           title = "Lecture5",
                           form=form,
                           name=name)


@app.route("/lect5_1/", methods=["GET", "POST"])
def lecture5_1():
    # name = None
    form = FirstForm()
    if form.validate_on_submit():
        session["name"] = form.name.data
        if len(session["name"]) < 3:
            flash ("Looks like your name is too short!")
            session.pop('name', None)
        form.name.data=''
        return redirect(url_for("lecture5_1"))
    return render_template("lecture5.jinja2",
                           title = "Lecture5",
                           form=form,
                           name=session.get("name"))

@app.route("/")
def hello_world():
    return render_template("about.jinja2", title="About Page")

@app.route("/about/")
def about():
    return render_template("about.jinja2", title="About Page")

@app.route("/name/<name>/")
def name(name):
    return f"<h2>Hello, {name}!</h2>"

# Так не можна робити!!!!
# @app.route("/add/")
# def add():
#     return '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Hello word</title>
# </head>
# <body>
#     <h1>Hello, World!</h1>
#     <p>This is a simple HTML page.</p>

# </body>
# </html>
# '''

@app.route("/home/<name>/")
def home(name):

    return render_template("index.jinja2", 
                           name=name)

@app.route("/name/")
def greet():
    name = "Mary"
    age = 30
    profession = "Developer"
    template_context = dict(name=name, 
                            age=age, 
                            profession=profession)
    return render_template("index.jinja2", 
                           name=name,
                        #    age=age,
                        #    profession=profession,
                           title="Greeting Page",
                            # **template_context
                           )

@app.route("/pets/")
def pets_list():
    return render_template("pets.jinja2", 
                           pets=pets,
                           title="Pets List")

@app.route("/lect4/")
def lecture4():
    return render_template("lecture4.jinja2", 
                           title="Lecture 4")

@app.route("/greeting/", methods=["GET", "POST"])
def greeting():
    if request.method == "GET":
        return render_template("greeting.jinja2", 
                           title="Greeting",
                           name="Guest")
    else:
        name = request.form.get("name")
        if not name:
            return render_template("lecture4.jinja2", 
                            title="Lecture 4", flag=1)
        return render_template("greeting.jinja2", 
                            title="Greeting",
                            name=name)



@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.jinja2", title="Page Not Found"), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("405.jinja2", title="Method Not Allowed"), 405




# if __name__ == "__main__":
#     app.run(debug=True, port=8000)




