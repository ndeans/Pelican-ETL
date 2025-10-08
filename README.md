# Pelican-ETL

Version 7 from initial conversation. 

[PelicanETL]/
├── README.md
├── pyproject.toml
├── venv/               # ignored by git
├── cli
|   ├── etl.py
|   ├── clean.sh
├── src/
│   ├── __init__.py     # optional but helps package recognition
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│   └── models.py       # contains dataclass
└── test/
     └── test_etl.py


From project base...
$ pytest -v
$ python -m cli.etl sample.enex --test
$ cli/clean.sh
