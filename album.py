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
def top5year():
    """show top 5 years which have most albums selected in list"""
    df = pd.read_csv('albumlist.csv', encoding= 'unicode_escape')
    df = df.groupby(['Year'])['Album'].count()
    df = df.sort_values(ascending = False)
    print(df[0:5])

@app.command()
def countartist():
    """show the unique artists who entered the list"""
    df = pd.read_csv('albumlist.csv', encoding= 'unicode_escape')
    artist = df.Artist.unique()
    artist.sort()
    n = len(pd.unique(df['Artist']))
    print(f'There are {n} artists who entered the 500 list')
    print('They are')
    print(artist)


@app.command()
def albumyear():
    """users can select a year and it will show all the albums released in that year in this list"""
    df = pd.read_csv('albumlist.csv', encoding= 'unicode_escape')
    year = input("please enter the year you want to search: ")
    year = int(year)
    if year > 2011:
        print(" this list contains album that release between 1955 - 2011")
    elif year <1955:
        print(" this list contains album that release between 1955 - 2011")
    else:
        con = df["Year"] == year
        print(df[con])


if __name__ == "__main__":
    app()