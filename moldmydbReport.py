#import pandas as pd
#import matplotlib
#from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
#from fpdf import FPDF
#from datetime import date

#def TreeviewTreatment(TreeviewObj):
    #df = pd.DataFrame()
    #df = TreeviewObj.get_children()

def ReportAssessment(servername,treeview,pdf):
    #today = date.today().strftime("%m.%d.%y")

    #df = pd.DataFrame()
    #df['VERSION'] = ["2012", "2012", "2012", "2012"]
    #df['EOS'] = [3, 4, 5, 3]
    #df['NAME'] = [3, 3, 4, 4]
    #df['SP'] = [3, 3, 4, 4]
    #df['CU'] = [3, 3, 4, 4]
    #df['KBLIST'] = [3, 3, 4, 4]

    #title("TI - Database Administrator - Database Server Assessment")
    #xlabel('Question Number')
    #ylabel('Score')

    #c = [2.0, 4.0, 6.0, 8.0]
    #m = [x - 0.5 for x in c]

    #xticks(c, df['Question'])

    #bar(m, df['Mike'], width=0.5, color="#91eb87", label="Mike")
    #bar(c, df['Charles'], width=0.5, color="#eb879c", label="Charles")

    #legend()
    #axis([0, 10, 0, 8])
    #savefig('barchart.png')

    #pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 11)
    pdf.cell(60)
    pdf.cell(75, 10, "TI - DBA - "+servername+" Standard Setup Report", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-50)

    pdf.set_font('arial', '', 11)
    pdf.cell(40, 5, 'Instance Information:', 0, 2, 'C')
    #pdf.line(10, 30, 200, 30)
    #pdf.cell(90, 5, " ", 0, 2, 'C')
    pdf.cell(40, 5, 'Server Instance', 1, 0, 'C')
    pdf.cell(30, 5, 'Server Name', 1, 0, 'C')
    pdf.cell(40, 5, 'Windows Name', 1, 0, 'C')
    pdf.cell(40, 5, 'Net Bios Name', 1, 0, 'C')
    pdf.cell(40, 5, 'Instance Name', 1, 2, 'C')
    pdf.cell(90, 5, " ", 0, 2, 'C')
    pdf.cell(-150)

    pdf.cell(40, 5, 'Missing Updates:', 0, 2, 'C')
    #pdf.line(10, 30, 200, 30)
    #pdf.cell(90, 5, " ", 0, 2, 'C')
    pdf.cell(40, 5, 'Version', 1, 0, 'C')
    pdf.cell(30, 5, 'EOS', 1, 0, 'C')
    pdf.cell(40, 5, 'Name', 1, 0, 'C')
    pdf.cell(20, 5, 'SP', 1, 0, 'C')
    pdf.cell(20, 5, 'CU', 1, 0, 'C')
    pdf.cell(40, 5, 'KB List', 1, 2, 'C')
    pdf.cell(-150)

    tree=treeview
    #print (tree['columns'])
    for i in tree.get_children():
        pdf.cell(40, 5, '%s' % (tree.item(i)['values'][0]), 1, 0, 'C')
        pdf.cell(30, 5, '%s' % (tree.item(i)['values'][1]), 1, 0, 'C')
        pdf.cell(40, 5, '%s' % (tree.item(i)['values'][2]), 1, 0, 'C')
        pdf.cell(20, 5, '%s' % (tree.item(i)['values'][3]), 1, 0, 'C')
        pdf.cell(20, 5, '%s' % (tree.item(i)['values'][4]), 1, 0, 'C')
        pdf.cell(40, 5, '%s' % (tree.item(i)['values'][5]), 1, 2, 'C')
        pdf.cell(-150)
        #pdf.cell(40, 10, '%s' % (tree.item(i)['values'][6]), 1, 2, 'C')

    #for i in range(0, len(df)):
    #    pdf.cell(40, 10, '%s' % (df['VERSION'].loc[i]), 1, 0, 'C')
    #    pdf.cell(30, 10, '%s' % (str(df['EOS'].loc[i])), 1, 0, 'C')
    #    pdf.cell(40, 10, '%s' % (str(df['NAME'].loc[i])), 1, 0, 'C')
    #    pdf.cell(20, 10, '%s' % (str(df['SP'].loc[i])), 1, 0, 'C')
    #    pdf.cell(20, 10, '%s' % (str(df['CU'].loc[i])), 1, 0, 'C')
    #    pdf.cell(40, 10, '%s' % (str(df['KBLIST'].loc[i])), 1, 2, 'C')
    #    pdf.cell(-150)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-30)
    #pdf.image('barchart.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
    #pdf.output('Assessment-'+servername+'-'+today+'.pdf', 'F')
    return pdf
