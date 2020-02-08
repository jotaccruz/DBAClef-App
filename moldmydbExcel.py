from openpyxl import Workbook

def xlsxGen(Section,Tree):
    wb = Workbook()
    ws = wb.active
    ws.title = Section

    columnslist=Tree['columns']
    row=1
    col=1
    for titles in columnslist:
        ws.cell (column=col,row=row,value=titles)
        col=col+1

    row=2
    for lists in Tree.get_children():
        col=1
        for values in Tree.item(lists)['values']:
            ws.cell (column=col,row=row,value=values)
            col=col+1
        row=row+1

        #print(titles)

    #ws['A1']="Hola"
    #wb.save('test.xlsx')
    return wb
