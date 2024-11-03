import click
from parser_1 import parse_krisha
from parser_1 import parse_apartment_in_city
from parser_1 import cities

@click.group()
def cli():
    """Custom shell CLI app."""
    pass

@cli.command()
def hello():
    """Say hello."""
    click.echo("Hello, World!")

@cli.command()
@click.argument('name')
def greet(name):
    """Greet a person."""
    click.echo(f"Hello, {name}!")
    
@cli.command()
@click.argument('url')
@click.argument('max_page', default=1)
@click.argument('sleep_time', default=1)
def parse(url, max_page, sleep_time):
    parse_krisha(f'{url}', max_page, sleep_time)

@cli.command()
@click.argument('city')
@click.argument('max_page', default=1)
@click.argument('sleep_time', default=1)
def parse_city(city, max_page, sleep_time):
    parse_apartment_in_city(f'{city}', max_page, sleep_time)

@cli.command()
@click.argument('max_page', default=5000)
@click.argument('sleep_time', default=1)
def parse_all(max_page, sleep_time):
    for city in cities:
        parse_apartment_in_city(f'{city}', max_page, sleep_time)

def run_shell():
    while True:
        try:
            # Read user input
            command = input("mycli> ")
            if command.lower() in ('exit', 'quit'):
                break
            # Use click to invoke the command
            cli.main(args=command.split(), prog_name="mycli", standalone_mode=False)
        except (KeyboardInterrupt, EOFError):
            # break
            pass
        except Exception as e:
            # Catch SystemExit to prevent the shell from closing on errors
            click.echo(e)

if __name__ == "__main__":
    run_shell()
