import click

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
        except click.ClickException as e:
            # Catch SystemExit to prevent the shell from closing on errors
            click.echo(e);

if __name__ == "__main__":
    run_shell()