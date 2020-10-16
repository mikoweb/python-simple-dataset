def filter_by_property(dataset, prop_name: str, value: str) -> list:
    rows = []
    for row in dataset.get_rows():
        if row.get_property(prop_name) == value:
            rows.append(row)

    return rows
