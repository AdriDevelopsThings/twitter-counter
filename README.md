# twitter-counter
*by AdriDevelopsThings*

# Install
## From source
You need python>=3.8 with pip. You should install the requirements in the requirements.txt: ``pip install -r requirements.txt``

Start the `__main__.py`.

## Docker
``docker-compose build``

Start with:

`docker-compose up -d`

# Configuration

### Cli

```
usage: __main__.py [-h] [-c CONFIG_FILE] [-gc]

twitter-counter

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_FILE, --config-file CONFIG_FILE
                        Path of the config file. The config file must have the yaml syntax. More in README.md.
  -gc, --generate-config
```

## Config file

The config file should have this yaml syntax:
```yaml
http:
  bind:
    host: 0.0.0.0
    port: 8080

twitter:
  consumer_key: ""
  consumer_secret: ""
  access_token_key: ""
  access_token_secret: ""

counter:
  webhook_name:
    name: "The text of the twitter thread."
    secrets: # list_of_webhook_secrets
      - "aJFJAGSBhushuaffsaius"
cache: "cache.json" # Path of the cache file (more in the Configuration.cache path)
```

## Cache

The id's of the twitter threads and the current count would be saved in the cache file. So you have to save the file, also for docker container.

# Increase Counter

The counter would be triggered with webhooks. The link of the webhook is: ``/webhook_name/one_secret``.
If the secrets list of the webhook do not contains the secret the app will response 403 Forbidden.
