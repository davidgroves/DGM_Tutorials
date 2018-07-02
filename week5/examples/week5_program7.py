# Week5, Program7

moons = {"Earth": "Luna", "Mars": ["Phobos", "Deimos"]}

print(f"The moons of Earth are {moons['Earth']}")
print(f"The moons of Mars are {moons['Mars']}")

print("Advanced Space Aliens move Charon from Pluto to Mars !")
moons["Mars"].append("Charon")
print(f"The moons of Earth are {moons['Earth']}")
print(f"The moons of Mars are {moons['Mars']}")

print("Evil space aliens destroy Earth's moon !")
moons["Earth"] = None
print(f"The moons of Earth are {moons['Earth']}")
print(f"The moons of Mars are {moons['Mars']}")
