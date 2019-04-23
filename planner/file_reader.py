import docx, PyPDF2, pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from dateutil.parser import parse

def is_date(string):
    try: 
        dt = parse(string, fuzzy_with_tokens=True)
        return dt
    except ValueError:
        return False
def read():
    dates = []
    full_data = []

    # Tk().withdraw()
    # f = askopenfilename()
    f = 'documents/HI302_30-Lesson_Course_Schedule_19-2_Final.docx'
    if 'docx' in f:
        doc = docx.Document(f)
        tables = doc.tables
        for table in tables:
            data = []
            for i, row in enumerate(table.rows):
                text = (cell.text for cell in row.cells)
                if i == 0:
                    keys = tuple(text)
                    continue
                row_data = dict(zip(keys, text))
                data.append(row_data)
                full_data.append(data)
        for entry in full_data:
            for lesson in entry:
                for k, v in lesson.items():
                    if is_date(v) and v not in dates:
                        dates.append(v)
        lesson_list = []
        for x in data:
            # print(', '.join("{!s}={!r}".format(key,val) for (key,val) in x.items()))
            lesson_list.append(list(x.items()))
        return lesson_list
    # elif 'pdf' in f:
    #     pdf = open(f,'rb')
    #     pdfReader = PyPDF2.PdfFileReader(pdf)
    #     numPages = pdfReader.getNumPages()
    #     for page in range(numPages):
    #         pageObj = pdfReader.getPage(page)
    #         print(pageObj.extractText())
    # elif 'xlsx' in f:
    #     df = pd.read_excel(f)
    #     print(df.columns)
    #     # print(df)
    # else:
    #     with open(f, 'r') as fi:
    #         for line in fi:
    #             print(line)