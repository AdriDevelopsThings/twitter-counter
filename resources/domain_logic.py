import logging

from requests import RequestException

from resources import twitter
from resources.cache import cache, write_cache
from resources.config import configuration


def ini_counters():
    for counter_name, values in configuration["counter"].items():
        if counter_name not in cache:
            cache[counter_name] = {
                "id": twitter.tweet(values["name"]).id_str,
                "count": 0,
            }
            logging.info(f"Counter {counter_name} initialized.")
    write_cache(cache)


def count(counter_name):
    try:
        id_str = cache[counter_name]["id"]
        cache[counter_name]["count"] += 1
        cache[counter_name]["id"] = twitter.tweet(
            str(cache[counter_name]["count"]), in_reply_to_status_id=id_str
        ).id_str
        write_cache(cache)
        logging.info(f"Increase count of {counter_name} to {cache[counter_name]['count']}.")
    except RequestException as e:
        if e.response.status_code == 404:
            del cache[counter_name]
            ini_counters()
        else:
            raise e
