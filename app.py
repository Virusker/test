from flask import Flask, request, abort
import os
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv(".env")
try:
    v = os.environ.get("API_KEY")
    print(v)
except:
    print(1)

@app.route("/")
def index():
    
    if v:
        return f"this var:{v}"
    else:
        return "dont have anymore var"
print()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
