from flask import Flask, request, json, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return "HelloWorld!"

@app.route("/hello2")
def hello2():
    return "HelloWorld2!"

@app.route('/', methods = ['POST'])  
def register():
    print request.headers
    print request.form
    print request.form['name']
    print request.form.get('name')
    print request.form.getlist('name')
    # print request.form['array']
    # print request.form.get('array')
    # print request.form.getlist('array')
    print request.form.get('something', default='little apple')
    resp = Response(json.dumps("response from flask"))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.run()