from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/result")
def get_result():
    return jsonify({"name": "watita"})

print("Hello World")

if __name__ == "__main__":
    app.run()
