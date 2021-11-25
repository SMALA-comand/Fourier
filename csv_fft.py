import csv


def get_csv_coord(csv_path):
    """
    Получает на вход csv файл с коэффициентами полинома
    :param csv_path: путь до csv файла
    :return: массив вида [x1, x2, ..., xn]
    """
    coordinates = []
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        count = 0
        for line in reader:
            x = line[0]
            try:
                x = float(x)
            except ValueError:
                if count == 0:
                    count += 1
                    continue
                else:
                    return 'Лишние символы в координатах!'
            else:
                count += 1
                coordinates.append(x)

    return coordinates
