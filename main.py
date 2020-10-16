from src.cars.Dataset import Dataset
from src.dataset.filter_by_property import filter_by_property
from src.dataset.split_dataset import split_dataset
from src.storage_path import storage_path
from src.dataset.save_to_csv import save_to_csv

if __name__ == '__main__':
    dataset = Dataset()

    # Etykiey
    print(dataset.get_labels())

    # Wypisanie danych datasetu
    for row in dataset.get_rows():
        #print(row.get_data())
        pass

    # Podział datasetu na zbiór treningowy, testowy i walidacyjny
    splits = split_dataset(dataset, ['training', 'test', 'validate'], [range(0, 2), range(5, 15), range(0, 20)])
    print(splits)

    # Klasy decyzyjne
    print(dataset.get_all_makes())

    # Liczba klas decyzyjnych
    print(len(dataset.get_all_makes()))

    # Wypisz dane dla podanej wartości klasy decyzyjnej
    for row in filter_by_property(dataset, 'make', 'honda'):
        print(row.get_data())

    # Zapisanie danych do pliku csv
    save_to_csv(splits['training'], storage_path('training-data.csv'))
