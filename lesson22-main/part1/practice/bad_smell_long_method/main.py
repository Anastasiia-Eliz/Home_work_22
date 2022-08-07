csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
	data = _read(csv)
	data = _sort(data)
	return _filter(data)


def _read(csv):
	return [line.split(';') for line in csv.split('\n')]


def _sort(data):
	return sorted(data, key=lambda age: int(age[1]))


def _filter(data):
	return [age for age in data if int(age[1]) < 10]


if __name__ == '__main__':
	print(get_users_list())
