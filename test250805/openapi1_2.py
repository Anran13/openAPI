from openpyxl import load_workbook, Workbook
from pprint import pprint

path = 'data/'

def get_aqi(excel_name)->list[dict]:
    excel_name = path + excel_name
    wb:Workbook = load_workbook(excel_name)
    # get worksheet
    sheet = wb.worksheets[0]

    # row: list(sheet)
    column_name = [cell.value for cell in list(sheet)[0]]
    print(column_name)

    # save as dictionary
    sheets = []
    for row in list(sheet)[1:]:
        site = {column_name[idx]:cell.value for idx, cell in enumerate(row)}
        sheets.append(site)
    
    return sheets

def main():
    data = get_aqi(excel_name='aqi.xlsx')
    pprint(data)

if __name__ == '__main__':
    main()


