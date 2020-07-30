galaxies = ['Small Magellanic Cloud', 'Andromeda Galaxy', 'Centaurus A']
distance_in_mly = [0.2, 2.5, 13.7]

for galaxy, dist in zip(galaxies,distance_in_mly):
    print(galaxy, dist)

d = dict(zip(galaxies, distance_in_mly))
for item in d:
    print(item)
