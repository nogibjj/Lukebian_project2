import pandas as pd
from pandasql import sqldf
import typer
from psycopg2.extras import NamedTupleCursor
from tabulate import tabulate

app = typer.Typer()

@app.command()
def loadData(): 
    """Load dataset"""
    df = pd.read_csv('albumlist.csv')
    table = df.iloc[[0,1],:]
    print("Successfully load dataset")
    print(table)

@app.command()
def fetchlist():
    """fetch items list"""
    df = pd.read_csv('albumlist.csv')
    print(df)




if __name__ == "__main__":
    app()