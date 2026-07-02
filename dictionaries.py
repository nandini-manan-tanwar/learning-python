#dictionaries - collection of pairs {key: values}ordered and unchangable.no duplicates
movies={'dhurandhar1':'rehman dakait',
        'dhurandhar2':'hamza ali',
        'teach you a lesson':'na hwajin'
        }

print(movies.get('dhurandhar2'))    
movies.update({'teach you a lesson':'im han rim'})
print(movies.get('teach you a lesson'))
movies.update({'weak hero ':'ahn suho'})
movies.pop('dhurandhar1')
print(movies)
keys=movies.keys()
print(keys)
values=movies.keys()
for key,value in movies.items():
    print(f'{key}:{value}')