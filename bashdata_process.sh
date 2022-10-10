echo "Simple data processing using command line"
DATE=`date +%Y-%m-%d`
echo "Date is: "$DATE
echo ""
echo "The name of the file is:" $1
echo ""
lines=$(wc -l < $1)
echo ""
echo "The file has" $lines "lines"
echo ""
colnames=$(head -n 1 < $1)
echo ""
echo "Column names are: "
echo ""
echo $colnames
echo ""
years=$(cut -d',' -f2 albumlist.csv | sort | uniq )
echo "Unique years are: "
echo ""
echo $years
echo ""
artist=$(cut -d',' -f4 albumlist.csv | sort | uniq | wc -l)
echo "the number of unique artists are: "
echo ""
echo $artist
echo ""
genre=$(cut -d',' -f5 albumlist.csv | sort | uniq | wc -l)
echo "the number of unique genres are: "
echo ""
echo $genre
