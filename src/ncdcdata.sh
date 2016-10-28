for i in {1901..2012}
do
  cd /Users/archer/Downloads/noaa/
  proxychains4 wget -r -np -nH .cut-dirs=3 -R index.html http://ftp3.ncdc.noaa.gov/pub/data/noaa/$i/
  cd pub/data/noaa/$i/
  cp *.gz /Users/archer/Downloads/noaa/files
  cd /Users/archer/Downloads/noaa/
  rm -r pub/
done
