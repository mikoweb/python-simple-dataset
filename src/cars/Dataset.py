from src.dataset.CSVReader import CSVReader
from src.cars.Labels import Labels
from src.cars.CarsNormalizer import CarsNormalizer


class Dataset:
    def __init__(self, file_name='imports-85.data'):
        self._reader = CSVReader(file_name, False, Labels(), ',', [CarsNormalizer()])

    def get_dataset(self) -> CSVReader:
        return self._reader

    def get_labels(self) -> tuple:
        return self.get_dataset().get_labels().get_labels()

    def get_rows(self, list_range: range = None) -> list:
        return self.get_dataset().get_rows(list_range)

    def get_all_makes(self):
        makes = []
        for row in self.get_rows():
            make = row.get_property('make')
            if make not in makes:
                makes.append(make)

        return makes

    def filter_by_property(self, prop_name: str, value: str) -> list:
        rows = []
        for row in self.get_rows():
            if row.get_property(prop_name) == value:
                rows.append(row)

        return rows
