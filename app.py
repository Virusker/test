from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "oktét 11 aa a    aa 1 5"
print()
print()
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
