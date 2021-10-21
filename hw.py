import pandas as pd
import numpy as np

def separate(n): #функция, которая принимает на ввод строку, содержащую название фильма и ее номер, на выходе возвращает только номер фильма
    if "'" in n:
        temp1 = str(n.index)
        temp2 = temp1.split("'")[1]
        result = temp2.split(":")[0]
    else:
        temp1 = str(n)
        result = temp1.split(":")[0]
    return int(result)
    
#1 задание

dataframe = pd.read_csv('C:/Users/anast/AppData/Local/Temp/HW1-data.csv', 
                        delimiter = ",")
df = dataframe.drop(['User', 'Gender (1 =F, 0=M)'], axis = 1) #убираем два первых столбика, пригодится
actual_series = np.mean(df) #нашли среднее значение, оно хранится в типа как словаре 
max_rate = max(actual_series) #среди среднего ищем максимум
temp = actual_series[actual_series == max_rate] #эта ерунда возвращает и записывает в переменную ключ по нужному значению (максимальному)
finish_result = separate(temp) #фиксим название и готово

print(f'1 задание - {finish_result}')

#2 задание
count = {} #количество голосов за каждый фильм
for i in dataframe: #заполняет непосредственно переменную count
    a = 0
    for key, value in dataframe[i].iteritems():
        if (value > 0):
             a += 1
    count[i] = a
    
del count['Gender (1 =F, 0=M)'] #эти строки нам вообще не нужны
del count['User']  
temp2 = max(count, key=count.get) #ищем максимальное кол-во голосов
finish_result_for_2 = separate(temp2)
print(f'2 задание - фильм с номером {finish_result_for_2}')

#3 задание


#4  задание

#5 задание
cor = {} #сюда будем записывать через цикл значения корреляции
for i in df:
    cor[i] = df[i].corr(df['1: Toy Story (1995)'])
del cor['1: Toy Story (1995)']    #убираем значение кор с самим собой
temp5 = max(cor, key=cor.get)   #ищем максимум
finish_result_for_5 = separate(temp5)

print(f'3 задание - фильм с номером {finish_result_for_5}')

#6 задание
for i in dataframe:
    rslt_w = df.loc[dataframe['Gender (1 =F, 0=M)'] == 0] #записываем табличку с фильтром по полу
    rslt_m = df.loc[dataframe['Gender (1 =F, 0=M)'] == 1]

rate_by_women = np.mean(rslt_w) #в каждой табличке ищем среднее
rate_by_men = np.mean(rslt_m)        

difference = abs(rate_by_men - rate_by_women) #тут мы ищем разницу и ее модуль

max_difference = difference.max() #ищем максимум
temp6 = difference[difference == max_difference] #опять по этому убожескому методу ищем ключ по значению
finish_result_6 = separate(temp6)

print(f'6 задание - фильм с номером {finish_result_6}')