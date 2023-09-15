from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "hello world"
        return {"data": data}
    else:
        return {
            "ERROR": {
                "valid_methods": ["GET"]
            }
        }


@app.route("/personal", methods=["POST"])
def disp():
    if request.method == "POST":
        posted_data = request.get_json(force=True)
        if posted_data.get("name"):
            return {
                "response": "hi {}".format(posted_data.get("name"))
            }
    else:
        return {
            "ERROR": {
                "valid_methods": ["POST"]
            }
        }


if __name__ == "__main__":
    app.run(debug=True)
