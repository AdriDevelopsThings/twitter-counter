import logging

from yaml import load, dump
from os.path import exists

from resources.parser import args

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

configuration = None


def read_config():

    with open(args.config_file) as f:
        return load(f, Loader=Loader)


def write_config(config):

    with open(args.config_file, "w") as f:
        f.write(dump(config, Dumper=Dumper))


def write_default_config():
    write_config(
        {
            "http": {"bind": {"host": "0.0.0.0", "port": "80"}},
            "twitter": {
                "consumer_key": "",
                "consumer_secret": "",
                "access_token_key": "",
                "access_token_secret": "",
            },
            "counter": {},
            "cache": "cache.json",
        }
    )


def load_config():
    global configuration

    if args.generate_config or not exists(args.config_file):
        write_default_config()
        logging.info("Wrote default config.")
        exit(0)
    else:
        logging.info("Read configuration successful.")
        configuration = read_config()


load_config()
