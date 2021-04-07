from flask import Flask, abort

from resources.domain_logic import ini_counters, count

app = Flask(__name__)


@app.route("/<string:webhook>/<string:secret>", methods=["POST"])
def webhook_trigger(webhook, secret):
    from resources.config import configuration
    if secret not in configuration["counter"][webhook]["secrets"]:
        abort(403)
    count(webhook)
    return "200"


@app.before_first_request
def before_first_request():
    ini_counters()
