j={}

j['name'] = 'fruit'
j['season'] = 'winter'
j['base'] = 'price'
print(j)
print(j.get('name' , 'default value'))
print(j.get('anything' , 'default value'))


# Sorted by keys (returns a list of tuples)
sorted_by_keys = sorted(j.items())
print(sorted_by_keys)


# To get a sorted dictionary by keys (Python 3.7+)
sorted_dict_by_keys = dict(sorted(j.items()))
print(sorted_dict_by_keys

      
