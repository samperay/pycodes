s = """Solar system:
Planets 8
Dwarf Planets: 5
Moons: Known = 149 | Provisional = 24 | Total = 173
Comets: More than 3400
Asteroids: More than 715000"""

import re
d = re.findall('\d+',s)
print(d)
