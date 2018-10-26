import sys
import argparse
from sanic.log import logger
from service_api.app import app
from service_api.database import create_all, drop_all, populate


def runserver(host, port):
    app.run(host=host, port=port, debug=True)


def dbinit():
    drop_all()
    create_all()
    populate()


def parse_args(args):
    parser = argparse.ArgumentParser(description="Sanic rest")
    subparsers = parser.add_subparsers(dest="command")

    sparser = subparsers.add_parser(runserver.__name__, add_help=False)
    sparser.add_argument("-h", "--host", dest="host", default="0.0.0.0", type=str)
    sparser.add_argument("-p", "--port", dest="port", default="5000", type=str)

    db_parser = subparsers.add_parser(dbinit.__name__, add_help=False)
    db_parser.add_argument(action='store_true', dest="dbinit")
    return parser.parse_args(args=args)


def main(args=None):
    parsed_args = parse_args(args or sys.argv[1:])
    print(parsed_args)
    if parsed_args.command == 'runserver':
        runserver(parsed_args.host, parsed_args.port)
    elif parsed_args.command == 'dbinit':
        dbinit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(e)
    finally:
        logger.info("Service stopped")
