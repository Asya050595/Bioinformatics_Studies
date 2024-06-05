from statistics import median

with open('input-median.txt','r') as fin:
    for i in fin:
        data = [str(i) for i in fin.read()]
        string_data = ''.join(str(x) for x in data)
        clean_data = string_data.strip()


datum = [float(i) for i in clean_data.split('\n')]

print(median(datum))
