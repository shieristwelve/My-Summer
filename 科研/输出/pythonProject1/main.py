dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two= {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):print(k2, '->', v2)

#print(k1, '->', v1)


