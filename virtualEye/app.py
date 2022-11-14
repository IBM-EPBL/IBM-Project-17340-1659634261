from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("./login.html")

@app.route("/about")
def about(): 
    return render_template("./about.html")

@app.route("/demo")
def demo(): 
    return render_template("./demo.html")

@app.route("/logout")
def logout(): 
    return render_template("./logout.html")

@app.route("/register")
def register(): 
    return render_template("./register.html")


if __name__ == '__main__':
   app.run()





