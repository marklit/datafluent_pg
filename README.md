# Data Fluent for PostgreSQL

[![Documentation Status](https://readthedocs.org/projects/datafluent/badge/?version=latest)](http://datafluent.readthedocs.io/en/latest/)
[![license](http://img.shields.io/badge/license-MIT-red.svg?style=flat)](http://opensource.org/licenses/MIT)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/datafluent.svg)](https://pypi.org/project/datafluent/)

Build a better understanding of your data in PostgreSQL.

The following shows an example report generated by this tool. It gives the numbers of rows, columns, bytes as well as human-friendly size counts for each table within a given PostgreSQL database.

![The Metrics Report](https://github.com/marklit/datafluent_pg/raw/main/example.png)

The following shows the row count for every column that represents a date grouped by year and month.

![The Time Distribution Report](https://github.com/marklit/datafluent_pg/raw/main/example2.png)

## Installation

On Ubuntu 20:

```
$ wget -qO- \
    https://www.postgresql.org/media/keys/ACCC4CF8.asc \
        | sudo apt-key add -
$ echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" \
    | sudo tee /etc/apt/sources.list.d/pgdg.list

$ sudo apt update
$ sudo apt install \
    git \
    python3-pip \
    python3-virtualenv \
    postgresql-13 \
    postgresql-client-13 \
    postgresql-contrib
```

On macOS:

```
$ brew install \
    git \
    postgresql \
    virtualenv
```

Then, regardless of platform, setup a virtual environment and install this software package.

```
$ virtualenv ~/.fluency
$ source ~/.fluency/bin/activate
$ python3 -m pip install datafluent
```

## Example Analysis

Clone FiveThirtyEight's [data repospitory](https://data.fivethirtyeight.com/). It has a large number of CSV-formatted datasets they've used for some of their articles and graphics.

```bash
$ git clone https://github.com/fivethirtyeight/data.git ~/538data
```

Make sure you can access a PostgreSQL database on your machine. Here I'm creating an ``intel`` database for the ``mark`` user on my Ubuntu 20 machine.

```bash
$ sudo -u postgres \
    bash -c "psql -c \"CREATE USER mark
                       WITH PASSWORD 'test'
                       SUPERUSER;\""
```

With PostgreSQL access setup, create a database called ``intel``.

```bash
$ createdb intel
```

I'll import one of the datasets within fivethirtyeight's repo. Note, because the dates within this dataset are not formatted in ```YYYY-MM-DD``` format, I needed to override the format so that the ```MM/DD/YYYY``` format would be read properly.

```bash
$ python3 -m pip install csvkit
$ csvsql --db postgresql:///intel \
         --insert ~/538data/congress-generic-ballot/generic_topline_historical.csv \
         --datetime-format="%m/%d/%Y"
```

I'll run the Excel Report Generator:


```bash
$ datafluent_pg
```

The above will connect to ```postgresql://localhost:5432/intel``` by default and will produce a ```fluency.xlsx``` file  with two worksheets: ```Metrics``` and ```Time Distributions```.

## Further Help

The database URL is passed through to sqlalchemy. Please see their documentation on [Database URLs](https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls) for more information on their syntax and the drivers supported.

If you need to override any parameters in this applcation, please refer to the help documentation generated by typer:

```bash
$ datafluent_pg --help
```

```
Usage: datafluent [OPTIONS]

Options:
  --url TEXT                      [default: postgresql://localhost:5432/intel]
  --output TEXT                   [default: fluency.xlsx]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.
```