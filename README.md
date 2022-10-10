
## Project #2: Bash Command-Line Tool
Build a Bash command-line tool that performs a useful data preparation task such as truncating data, sorting it, cleaning data, or doing ETL. It should be portfolio worthy.

## How to use command line to run the data processing

First, you need to install all the packages you will use. Type in the code in your terminal
```
 pip install -r requirements.txt
 
```
Then, type in 

```
 python album.py --help
 
```
you can check all the commands you can use to process the data. They are
```
 python album.py albumyear    
 python album.py countartist  
 python album.py datahead    
 python album.py top5year     
 
```
albumyear    users can select a year and it will show all the albums' year
countartist  show the unique artists who entered the list
datahead     show the fisrt 5 lines in dataset
top5year     show top 5 years which have most albums selected in list

you can type in the 
```
 bash bashdata_process.sh albumlist.csv > result.txt
 
```
it will run the bash pipline automatically and put the reuslt into the result.txt file

## Acknowledgments
The knowledge for making this project is gained from Prof. Noah Gift's lecture.
