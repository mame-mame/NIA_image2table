import csv
import io
import os


def text_files_to_csv(files,save_filepath):
    """Files must be sorted lexicographically
    Filenames must be <row>-<colum>.txt.
    000-000.txt
    000-001.txt
    001-000.txt
    etc...
    """

    rows = []


    for f in files:
        directory, filename = os.path.split(f)
        with open(f) as of:
            txt = of.read().strip()
        row, column = map(int, filename.split(".")[0].split("-"))   #000-000.gt.txt -> .으로 나눈뒤 0번째를 - 로 나눈뒤 row와 column에 저장
        if row == len(rows):
            rows.append([])

        rows[row].append(txt)



    html_string = '<table border=\"1\"> <thead></thead> <tbody> </tbody> </table>'
    html_string_return =''
    #print('<table border=\"1\">', '<thead>','</thead>','<tbody>', sep='\n')
    for row_index in rows:
        #print('<tr>')
        html_string = html_string[:-17] + '<tr>' + html_string[-17:]
        html_string_return = html_string_return+'<tr>'

        for column_index in row_index:
            if column_index == '':
                #print('<td>' + 'NaN' + '</td>')
                html_string = html_string[:-17] + '<td>' + 'NaN' + '</td>' + html_string[-17:]
                html_string_return = html_string_return+'<td>' + 'NaN' + '</td>'

            else:
                #print('<td>' + column_index + '</td>')
                html_string = html_string[:-17] + '<td>' + column_index + '</td>' + html_string[-17:]
                html_string_return = html_string_return+ '<td>' + column_index + '</td>'

        #print('</tr>')
        html_string = html_string[:-17] + '</tr>' + html_string[-17:]
        html_string_return = html_string_return + '</tr>'
    #print('</tbody>','</table>',sep='\n')


    dir = os.path.dirname(save_filepath)   #디렉토리 이름 검출



    csv_file_name = 'table_csv.csv'                 #csv파일 이름
    csv_name = os.path.join(dir, csv_file_name)
    csv_file = io.StringIO()
    writer = csv.writer(csv_file)
    writer.writerows(rows)
    with open(csv_name, 'w', newline='') as cf:
        writer2 = csv.writer(cf)
        writer2.writerows(rows)

    html_file_name = 'table_html.html'
    html_name = os.path.join(dir, html_file_name)
    html_file = open(html_name,'w')
    html_file.write(html_string)
    html_file.close()

    return html_string_return
