# StockCLI

A CLI tool to interact with a stock market API.

## Usage

To run the CLI tool:

```bash
poetry run stockcli get --symbol AAPL
poetry run stockcli list
```

## Development

This project uses [Poetry](https://python-poetry.org/) for dependency
management. To set up your development environment, follow these steps:

### Install Poetry:

On macOS / Linux:

```bash
curl -sSL https://install.python-poetry.org | python -
```

On Windows:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### Clone the repository:

```bash
git clone https://github.com/yourusername/stockcli.git
cd stockcli
```

### Install the dependencies:

```bash
make install
```

This will create a virtual environment and install the necessary dependencies.


### Testing

To run the tests:

```bash
make test
```

### Linting

To lint the code:

```bash
make lint
```
