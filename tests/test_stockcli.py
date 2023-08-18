import pytest
from click.testing import CliRunner
from stockcli import cli

def test_get_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['get', '--symbol', 'AAPL'])
    assert result.exit_code == 0
    assert 'Fetching price for AAPL...' in result.output

def test_list_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['list'])
    assert result.exit_code == 0
    assert 'Listing all available stock symbols...' in result.output
