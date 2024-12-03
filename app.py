from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello World! Lets Start Contributing Myapp"
if __name__ == "__main__":
    app.run()
