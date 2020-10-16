def convert_to_list(dataset) -> list:
    rows = []
    for row in dataset.get_rows():
        rows.append(row.get_data())

    return rows
