from argparse import ArgumentParser

parser = ArgumentParser(description="twitter-counter")
parser.add_argument(
    "-c",
    "--config-file",
    default="config.yaml",
    help="Path of the config file. The config file must have the yaml syntax. More in README.md.",
)
parser.add_argument("-gc", "--generate-config", action="store_true")

args = parser.parse_args()
