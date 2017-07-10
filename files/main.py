"""Main model."""

import json
import openpyxl
import sys


def main(list_xlsx):
    list_wb = []
    dict_wb = {}
    list_return = []
    int_row_count = 1

    try:
        list_wb.append(openpyxl.load_workbook(list_xlsx[1], read_only=True))
    except Exception:
        print("File Not Found: {}".format(list_xlsx[1]))
        exit(0)

    for tab in list_wb[0].get_sheet_names():
        for row in list_wb[0][tab].rows:
            for cell in row:
                if int_row_count == 1:
                    if cell.value != '':
                        print(cell.value)
                        dict_wb[cell.value] = ''
                else:
                    for header in dict_wb:
                        # dict_wb[header] = list_wb[0][tab]
                        print(cell)
                    list_return.append(dict_wb)
            int_row_count += 1

    # print(json.dumps(list_return))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Passe arquivos XLS")
        exit(0)

    main(sys.argv)
