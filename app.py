from flask import Flask, request, abort
import os
app = Flask(__name__)
try:
   v = os.environ.get('VERCEL_URL')
except:
   print("nothing")
@app.route("/")
def index():
   
    if v:
        return f"this var:{v}"
    else:
        return "dont have anymore var"
print()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
