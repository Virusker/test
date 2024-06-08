from flask import Flask, request, abort
import os
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv(".env")


@app.route("/")
def index():
    v = os.environ.get("A")
    if v:
        return f"this var:{v}"
    else:
        return "dont have anymore var"
print()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
