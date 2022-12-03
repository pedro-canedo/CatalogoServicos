import os


CONFIG_STRING = """
POSTGRES_DB=db
POSTRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=localhost
"""


def generate_env():
    with open('.env', 'w') as f:
        f.write(CONFIG_STRING)
        



