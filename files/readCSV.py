"""Main model."""

import sys

from csv import DictReader
from datetime import datetime


def main(list_xlsx):
    dict_reader = DictReader(open(list_xlsx[1], 'r'), delimiter=';')

    for line in dict_reader:
        try:
            line["@timestamp"] = datetime.strptime("{}T{}".format(line["DATA"], line["HORA"]), "%Y%m%dT%H%M%S").strftime("%Y-%m-%dT%H:%M:%S-03:00")
        except Exception:
            line["@timestamp"] = ""
        print(line)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Passe arquivos XLS")
        exit(0)

    main(sys.argv)
