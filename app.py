from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "oktét 11aaa a aa1 5"
print()
print()
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
