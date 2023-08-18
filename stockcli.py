import time
import click
import rich_click as click
from rich.console import Console
from rich.progress import Progress
from rich.traceback import install
import requests

install()
console = Console()

def validate_symbol(ctx, param, value):
    if not value:
        raise click.BadParameter('Symbol must be provided')
    if len(value) < 1:
        raise click.BadParameter('Symbol must be at least 1 character long')
    return value

@click.group()
def cli():
    pass

@cli.command()
@click.option('--symbol', callback=validate_symbol, help='The stock symbol to fetch.')
def get(symbol):
    with Progress() as progress:
        task = progress.add_task("[cyan]Fetching price...", total=100)

        # Simulate long-running operation
        while not progress.finished:
            progress.update(task, advance=0.5)
            time.sleep(0.02)

    response = requests.get(f'https://api.example.com/stocks/{symbol}')
    price = response.json().get('price')

    console.print(f'Price for [bold green]{symbol}[/bold green]: [bold cyan]{price}[/bold cyan]')

@cli.command()
def list():
    console.print('Listing all available stock symbols...')

if __name__ == "__main__":
    cli()
