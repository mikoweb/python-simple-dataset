def split_dataset(dataset, names: list, ranges: list) -> dict:
    splits = {}
    for index, name in enumerate(names):
        splits[name] = dataset.get_rows(ranges[index])

    return splits
