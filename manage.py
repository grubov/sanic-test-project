import argparse

import sys
from sanic.log import logger

from service_api.app import app


def runserver(host, port):
    app.run(host=host, port=port, debug=True)


def parse_args(args):
    parser = argparse.ArgumentParser(description="Sanic rest")
    subparsers = parser.add_subparsers(dest="command")

    sparser = subparsers.add_parser(runserver.__name__, add_help=False)
    sparser.add_argument("-h", "--host", dest="host", default="0.0.0.0", type=str)
    sparser.add_argument("-p", "--port", dest="port", default="5000", type=str)
    return parser.parse_args(args=args)


def main(args=None):
    parsed_args = parse_args(args or sys.argv[1:])
    runserver(parsed_args.host, parsed_args.port)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(e)
    finally:
        logger.info("Service stopped")
