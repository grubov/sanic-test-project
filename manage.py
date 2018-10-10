import click
from app.app import app


# @click.command()
# @click.option('--runserver', help='Run server', show_default=True)
# def main():
#     app.run(host="0.0.0.0", port=8000)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)