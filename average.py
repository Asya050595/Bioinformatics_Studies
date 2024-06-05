from statistics import mean

with open('input-average.txt','r') as fin:
    for i in fin:
        data = [str(i) for i in fin.read()]
        string_data = ''.join(str(x) for x in data)
        clean_data = string_data.strip()

def average(x):
    total = 0
    count = 0
    for i in x:
        count += 1
        total += i
    return total/count

datum = [float(i) for i in clean_data.split('\n')]

print(average(datum))
