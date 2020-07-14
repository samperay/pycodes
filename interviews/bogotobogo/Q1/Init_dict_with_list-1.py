cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

from collections import defaultdict
d=defaultdict(list)
for k,v in cities.items():
    d[v].append(k)
print(d)
