import math 
import csv  
with open('std.csv', newline='') as f :
    reader = csv.reader(f) 
    file_data = list(reader) 
data = file_data[0]
def mean(data):
    n = len(data) 
    total = 0 
    for i in data: 
        total += int(i) 
    mean = total/n 
    return mean 

squared_list = [] 
for num in data: 
    a = int(num) - mean(data) 
    a = a**2  
    squared_list.append(a) 
                   
sum = 0
for x in squared_list: 
    sum += x 

result = sum/(len(data)-1) 
std = math.sqrt(result)
print(std)