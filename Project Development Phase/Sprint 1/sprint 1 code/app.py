from flask import Flask, request, render_template
from cloudant.client import Cloudant

# Authenticate using an IAM API key
client = Cloudant.iam('06e7c9cd-cbb3-4b56-a40a-e669cf5b0906-bluemix','VPbZAA_fmWRYpJdz4kowaZwERWNd4vqCSvOzVI5DXmNn', connect=True)

# Create a database using an initialized client
my_database = client['database1']


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

@app.route("/result")
def res():
    return "<h1>result</h1>"


@app.route('/afterreg', methods=['GET'])
def afterreg():
    username = request.args.get('uname')
    password = request.args.get('password')
    print(list(request.form.values()))
    data = {
    'uname': username,
    'password': password
    }
    print(data)
    query = {'uname': {'$eq': data['uname']}}
    docs = my_database.get_query_result(query)
    print(docs)
    
    print(len(docs.all()))
    
    if(len(docs.all())==0):
        url = my_database.create_document(data)
        #response = requests.get(url)
        return render_template('login.html', pred="Registration Successful, please login using your details")
    else:
        return render_template('login.html', pred="You are already a member, please login using your details")


@app.route('/afterlogin',methods=['GET'])
def afterlogin():
    user = request.args.get('uname')
    passw = request.args.get('password')
    print(user + passw)
    query = {'uname': {'$eq': user}}    
    docs = my_database.get_query_result(query)
    print(docs)
    print(len(docs.all()))
    if(len(docs.all())==0):
        return render_template('login.html', pred="The username is not found.")
    else:
        if((user==docs[0][0]['uname'] and passw==docs[0][0]['password'])):
            return render_template('about.html')
        else:
            return render_template('login.html', pred="incorrect password, please try again.")


if __name__ == '__main__':
   app.run()





