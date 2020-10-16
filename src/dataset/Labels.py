class Labels:
    def __init__(self, labels: tuple):
        self._labels = labels

    def get_labels(self) -> tuple:
        return self._labels

    def get_index(self, label: str) -> int:
        return self._labels.index(label)

    def get_label(self, index: int) -> str:
        return self._labels[index]
