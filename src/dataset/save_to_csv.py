def save_to_csv(rows, file_name):
    f = open(file_name, 'w')

    for row in rows:
        line = ''
        for item in row.get_row():
            line += item + ','
        f.write(line[0:-1] + '\n')

    f.close()
    pass
