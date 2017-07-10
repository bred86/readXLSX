##How to


```
docker build -t readxlsx .
docker run -it --rm -v file.csv:/tmp/file.csv readxlsx python3 /opt/readCSV.py /tmp/file.csv
```
