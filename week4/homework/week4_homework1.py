# Week4, Homework1

planets = ['Mercury', 'Venus', 'Earth', 'Mars']
planets.extend(['Jupiter', 'Saturn', 'Uranus', 'Neptune'])

print("Planets Backwards")
print(planets[::-1])

print("Rocky Planets")
print(planets[:4])

print("Gas Giants")
print(planets[4:])

print("Gas Giants Backwards")
print(planets[:-5:-1])

print("Every other planet")
print(planets[::2])

print("Every other planet backwards, starting at Saturn")
print(planets[-3::-2])
