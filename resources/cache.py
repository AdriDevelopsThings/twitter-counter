from json import load, dumps
from os.path import exists

cache = {}


def read_cache():
    from resources.config import configuration

    with open(configuration["cache"]) as f:
        return load(f)


def write_cache(cache):
    from resources.config import configuration

    with open(configuration["cache"], "w") as f:
        f.write(dumps(cache))


def write_default():
    write_cache({})


def load_cache():
    global cache
    from resources.config import configuration

    if not exists(configuration["cache"]):
        write_default()
    cache = read_cache()


load_cache()
