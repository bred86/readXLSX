"""Main model."""

import json
import sys

from csv import DictReader
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers


def main(list_xlsx):
    list_action = []
    dict_reader = DictReader(open(list_xlsx[1], 'r'), delimiter=';')

    for tmp_line in dict_reader:
        dict_es = {}
        line = {}

        try:
            tmp_line["@timestamp"] = datetime.strptime("{}T{}".format(tmp_line["DATA_TRANSACAO"], tmp_line["HORA_TRANSACAO"]), "%Y%m%dT%H%M%S").strftime("%Y-%m-%dT%H:%M:%S-03:00")
        except Exception:
            tmp_line["@timestamp"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        for header in tmp_line:
            if header == "":
                line["line_number"] = int(tmp_line[header])
            else:
                line[header.lower()] = tmp_line[header]

        dict_es["_op_type"] = "index"
        dict_es["_index"] = "v1-pdv"
        dict_es["_type"] = "pdv"
        dict_es["_source"] = line

        list_action.append(dict_es)

        del dict_es

    return list_action

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Passe arquivos XLS")
        exit(0)

    list_es = []
    list_action = main(sys.argv)
    es = Elasticsearch()

    for action in list_action:
        list_es.append(action)
        if len(list_es) >= 100:
            print("Enviando {}".format(len(list_es)))

            helpers.bulk(es, list_es)

            del list_es
            list_es = []

    if len(list_es) != 0:
        print("Enviando {}".format(len(list_es)))

        helpers.bulk(es, list_es)
