# twitter-counter
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://adridoesthings.com"><img src="https://avatars.githubusercontent.com/u/45321107?v=4?s=100" width="100px;" alt=""/><br /><sub><b>AdriDevelopsThings</b></sub></a><br /><a href="https://github.com/AdriDevelopsThings/twitter-counter/commits?author=AdriDevelopsThings" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!