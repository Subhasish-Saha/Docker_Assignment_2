from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return 'Hello World : -by Subhasish'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=30)