import docx
from dateutil.parser import parse

# Open's a file and iterates through the tables
# adding each row to a list and adding that list
# to a root list
def read():
    f = 'documents/HI302_30-Lesson_Course_Schedule_19-2_Final.docx'
    if 'docx' in f:
        data = []
        doc = docx.Document(f)
        tables = doc.tables
        for table in tables:
            for i, row in enumerate(table.rows):
                text = (cell.text for cell in row.cells)
                if i == 0:
                    keys = tuple(text)
                    continue
                row_data = dict(zip(keys, text))
                data.append(row_data)
        lesson_list = []
        for x in data:
            lesson_list.append(list(x.items()))
        return lesson_list