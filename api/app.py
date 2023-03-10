from flask import Flask, Response, request, Blueprint
import math
import json

app = Flask(__name__)
api = Blueprint("api", __name__)


@api.route("/")
def index():
    return Response("Hello", status=200)


@api.route("/compute", methods=["POST"])
def compute():
    payload = request.get_json()
    if "number" in payload and isinstance(payload["number"], int) and payload["number"] > 0:
        number = payload["number"]
        return Response(json.dumps({"number": int(number), "square_root": math.sqrt(int(number)), "power_of_2": pow(int(number), 2)}), status="200")
    else:
        return Response("Bad payload", status=400)


@api.route("/healthz")
def health():
    return Response("ok", status=200)
