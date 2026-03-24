from flask import Flask, render_template, request

app = Flask(__name__, 
            # template_folder="jinja_templates"
            )

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




