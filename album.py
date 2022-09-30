import pandas as pd
from pandasql import sqldf
import typer
from psycopg2.extras import NamedTupleCursor
from tabulate import tabulate

app = typer.Typer()

@app.command()
def datahead(): 
    """show the fisrt 5 lines in dataset"""
    df = pd.read_csv('albumlist.csv', encoding= 'unicode_escape')
    table = df.head()
    print("Successfully load dataset")
    print(table)

@app.command()
def fetchlist():
    """fetch items list"""
    df = pd.read_csv('albumlist.csv', encoding= 'unicode_escape')
    print(df)




if __name__ == "__main__":
    app()