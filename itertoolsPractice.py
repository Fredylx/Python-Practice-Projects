'''
Title:          Itertools Practice
Lang:           Python
'''
import itertools

counter = itertools.count(start=5, step=-2.5)
# 
# data = [100, 200, 300, 400]
# 
# daily_data = list(zip(itertools.count(), data))
# 
# print(daily_data)
# 
# 

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#for num in counter:
#    print(num)
    

