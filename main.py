import struct
from collections import Counter
# Задача 1: Записать в новый файл только четные числа
with open('input.txt', 'r') as input_file, open('output_even.txt', 'w') as output_file:
    numbers = map(int, input_file.read().split())
    even_numbers = [str(num) for num in numbers if num % 2 == 0]
    output_file.write('\n'.join(even_numbers))




# Задача 2: Найти максимальный элемент в бинарном файле


with open('binary_file.bin', 'wb') as binary_file:
    data = [1, 5, 2, 8, 3]
    binary_file.write(struct.pack('5i', *data))

with open('binary_file.bin', 'rb') as binary_file:
    data_read = struct.unpack('5i', binary_file.read())
    max_element = max(data_read)
    print(f'Maximum element: {max_element}')






# Задача 3: Найти количество простых чисел
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

with open('binary_file.bin', 'rb') as binary_file:
    data_read = struct.unpack('5i', binary_file.read())
    prime_count = sum(1 for num in data_read if is_prime(num))
    print(f'Number of prime numbers: {prime_count}')



# Задача 4: Проверить, образуют ли числа возрастающую последовательность
with open('binary_file.bin', 'rb') as binary_file:
    data_read = struct.unpack('5i', binary_file.read())
    is_increasing = all(data_read[i] < data_read[i + 1] for i in range(len(data_read) - 1))
    print(f'The numbers form an increasing sequence: {is_increasing}')





# Задача 5: Проверить, образуют ли числа симметричную последовательность
with open('binary_file.bin', 'rb') as binary_file:
    data_read = struct.unpack('5i', binary_file.read())
    is_symmetric = data_read == data_read[::-1]
    print(f'The numbers form a symmetric sequence: {is_symmetric}')




# Задача 6: Создать новый текстовый файл с числами в обратном порядке
with open('text_file.txt', 'r') as input_file, open('reversed_text.txt', 'w') as output_file:
    numbers = map(int, input_file.read().split())
    reversed_numbers = reversed(list(numbers))
    output_file.write('\n'.join(map(str, reversed_numbers)))





# Задача 7: Создать новый бинарный файл с числами в обратном порядке
with open('binary_file.bin', 'rb') as binary_file:
    data_read = struct.unpack('5i', binary_file.read())

with open('reversed_binary_file.bin', 'wb') as reversed_binary_file:
    reversed_data = struct.pack('5i', *reversed(data_read))
    reversed_binary_file.write(reversed_data)




# Задача 8: Создать новый текстовый файл с словами в обратном порядке
with open('text_words.txt', 'r') as input_file, open('reversed_text_words.txt', 'w') as output_file:
    words = input_file.read().split()
    reversed_words = reversed(words)
    output_file.write(' '.join(reversed_words))





# Задача 9: Сортировать числа в порядке возрастания
with open('binary_file.bin', 'rb') as binary_file:
    data_read = struct.unpack('5i', binary_file.read())
    sorted_data = sorted(data_read)
    with open('sorted_numbers.txt', 'w') as output_file:
        output_file.write('\n'.join(map(str, sorted_data)))



# Задача 10: Работа с данными о городах
cities_data = [
    {"name": "City1", "country": "Germany", "population": 1200000, "area": 100},
    {"name": "City2", "country": "France", "population": 800000, "area": 80},
]

# Найти самый населенный город в Германии
germany_cities = [city["population"] for city in cities_data if city["country"] == "Germany"]
max_population_germany = max(germany_cities)
print(f'Max population in Germany: {max_population_germany}')

# Найти город с наибольшей плотностью населения
cities_density = [(city["population"] / city["area"], city["name"]) for city in cities_data]
max_density_city = max(cities_density)[1]
print(f'City with max population density: {max_density_city}')

# Распечатать названия стран с городами, население которых более 1000000 человек
countries_over_1m = set(city["country"] for city in cities_data if city["population"] > 1000000)
print(f'Countries with cities over 1 million population: {", ".join(countries_over_1m)}')

# Найти количество городов во Франции
france_cities_count = sum(1 for city in cities_data if city["country"] == "France")
print(f'Number of cities in France: {france_cities_count}')







# Задача 11: Найти наиболее часто встречающуюся букву в тексте
with open('text_file_letter.txt', 'r') as text_file:
    text = text_file.read()

text_lower = text.lower()

letter_counts = Counter(letter for letter in text_lower if letter.isalpha())

most_common_letter = max(letter_counts, key=letter_counts.get)

print(f'Most common letter: {most_common_letter.upper()}')



# Задача 12: Формирование уникальных логинов для студентов
login_counts = {}

with open('students.txt', 'r') as students_file:
    n = int(students_file.readline().strip())

    for _ in range(n):
        student_name = students_file.readline().strip()
        last_name, _ = student_name.split(None, 1) 

        login = last_name
        if login in login_counts:
            login_counts[login] += 1
            login = f'{last_name}{login_counts[login]}'
        else:
            login_counts[login] = 1

        print(f'{student_name}: {login}')




# Задача 13: Печать строчных английских букв и их частот
with open('input_sequence.txt', 'r') as input_file:
    sequence = input_file.read().lower()

letter_counts = {letter: sequence.count(letter) for letter in set(sequence) if letter.isalpha()}
sorted_letters = sorted(letter_counts.items())

for letter, count in sorted_letters:
    print(f'{letter}: {count}')