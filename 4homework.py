import codecs

def dist(str1, string):
    distance = 0
    for i in range(len(str1)):
        if str1[i] != string[i]:
            distance += 1
    return distance

while True:
    dict_of_distance = {}
    string = str(input('Введите строку для сравнения: '))
    len_string = len(string)
    output_file = str(input('Введите путь к файлу со строками: '))
    with codecs.open(output_file, "r", "utf_8_sig") as file:
        strings = [current_place.rstrip() for current_place in file.readlines()]
        for i in strings:
            if len(i) == len_string:
                dict_of_distance[i] = dist(string, i)
        sorted_d = sorted(dict_of_distance.items(), key=lambda item: item[1])
        i = 0
        result = []
        while i < len(sorted_d):
            result.append(sorted_d[i][0])
            i += 1
        print(result)
        with open('output.txt', 'w') as result1:
            for i in result:
                result1.write(i)
                result1.write('\n')
        print('Ищите ответ в файле "output.txt"')