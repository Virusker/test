from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "oktét 123"
print()
print()
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
