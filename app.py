from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "🚀 Hello from GitHub + CRC + Webhook!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

#test1
#test2
