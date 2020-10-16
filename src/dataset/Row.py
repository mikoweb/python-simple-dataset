from src.dataset.Labels import Labels


class Row:
    def __init__(self, line: str, labels: Labels, separator: str = ',', normalizers: list = None):
        row = line.strip().split(separator)
        data = {}

        for index, label in enumerate(labels.get_labels()):
            data[label] = row[index]
            if normalizers is not None:
                for normalizer in normalizers:
                    data[label] = normalizer.normalize(data[label], label, index)

        self._row = row
        self._data = data

    def get_data(self) -> dict:
        return self._data

    def get_row(self) -> list:
        return self._row

    def get_index(self, index):
        return self._row[index]

    def get_property(self, name: str):
        return self._data[name]
