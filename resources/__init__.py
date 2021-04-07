import logging

from twitter import TwitterAuth, TwitterApi
from resources.config import configuration

logging.getLogger("").setLevel(logging.INFO)


twitter = TwitterApi(
    TwitterAuth.get_oauth1_auth(
        configuration["twitter"]["consumer_key"],
        configuration["twitter"]["consumer_secret"],
        configuration["twitter"]["access_token_key"],
        configuration["twitter"]["access_token_secret"],
    )
)


def main():
    global twitter
    from resources.flask_server import app

    app.run(
        host=configuration["http"]["bind"]["host"],
        port=configuration["http"]["bind"]["port"],
        debug=False,
        threaded=True,
    )
