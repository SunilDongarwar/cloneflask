from flask import Flask
myapp = Flask(__name__)
@myapp.route("/")
def helloworld():
    return "Hello World! Lets Start Contributing Myapp"
if __name__ == "__main__":
    myapp.run()
