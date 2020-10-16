from src.dataset.Labels import Labels
from src.storage_path import storage_path
from src.dataset.Row import Row


class CSVReader:
    def __init__(self, file_name: str, has_labels: bool, labels: Labels = None, separator: str = ',',
                 normalizers: list = None):
        if not has_labels and Labels is None:
            raise Exception('No LABELS')

        if not has_labels:
            self._labels = labels

        self._file_name = file_name
        self._has_labels = has_labels
        self._separator = separator
        self._normalizers = normalizers
        self._import_file()

    def get_labels(self) -> Labels:
        return self._labels

    def get_rows(self, list_range: range = None) -> list:
        return self._rows if list_range is None else self._rows[list_range.start:list_range.stop]

    def _import_file(self):
        file_path = self._file_name if self._file_name[0] == '/' else storage_path(self._file_name)
        line_number = 1
        self._rows = []
        with open(file_path, 'r', encoding='utf-8') as file_reader:
            for line in file_reader:
                if self._has_labels and line_number == 1:
                    self._labels = Labels(tuple(line.strip().split(self._separator)))
                else:
                    self._rows.append(Row(line, self._labels, self._separator, self._normalizers))
                line_number += 1
