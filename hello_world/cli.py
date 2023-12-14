import click
from database import signup

@click.group()
def cli():
    pass

@cli.command()
def apikey():
    """This is the apikey command."""
    click.echo('1. Signup')
    click.echo('2. Signin')
    option = click.prompt('Please enter your option', type=int)

    if option == 1:
        click.echo('You chose signup.')
        email = click.prompt('Please enter your email')
        password = click.prompt('Please enter your password')
        signup(email, password)
    elif option == 2:
        click.echo('You chose signin.')
        # Call your signin function here
    else:
        click.echo('Invalid option.')

if __name__ == '__main__':
    cli()