class DataModel(object):

    def __init__(self):
        self._file_path = 'data.txt'
        self._data_dict = dict()

    def load_data(self):
        with open(self._file_path, 'r', encoding='utf-8') as f:
            rows = f.readlines()
        self._data_dict.clear()
        for row in rows:
            parts = (row.strip()).split(' - ')
            self._data_dict[parts[0]] = parts[1]
            self._data_dict[parts[1]] = parts[0]
        print(self._data_dict)

    def save_data(self):
        with open(self._file_path, 'w', encoding='utf-8') as f:
            for country, capital in self._data_dict.items():
                f.write(f'{country} - {capital}\n'
                        f'{capital} - {country}\n')

    def search_rec(self, some: str) -> str:
        if some not in self._data_dict:
            return 'Данные не найдены!'
        else:
            return self._data_dict[some]

    def add_rec(self, country: str, capital: str) -> None:
        self._data_dict[country] = capital
        self.save_data()

    def del_rec(self, some: str):
        if self._data_dict.get(some) is not None:
            self._data_dict.pop(self._data_dict.get(some))
            self._data_dict.pop(some)
            self.save_data()
        else:
            return True
