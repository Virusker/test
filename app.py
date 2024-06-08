from flask import Flask, request, abort
import os
from dotenv import load_dotenv
app = Flask(__name__)
<<<<<<< HEAD

load_dotenv(".env")


@app.route("/")
def index():
    v = os.environ.get("A")
=======
try:
   v = os.environ.get('VERCEL_URL')
except:
   print("nothing")
@app.route("/")
def index():
   
>>>>>>> b7e49d62930377da4b40c388a1288d5a4f684e52
    if v:
        return f"this var:{v}"
    else:
        return "dont have anymore var"
print()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
