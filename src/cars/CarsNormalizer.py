from src.dataset.NormalizerInterface import NormalizerInterface


class CarsNormalizer(NormalizerInterface):
    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def normalize(self, value, col_label: str, col_index: int):
        normalized = value
        if value == '?':
            normalized = None

        if type(value) == str and (value.isnumeric() or self.is_float(value)):
            normalized = float(value) if '.' in value else int(value)

        return normalized
