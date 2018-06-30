# Week5, Program5

year = {}  # An empty dictionary.

year[2018] = ["Theresa May"]
year[2017] = ["Theresa May"]
year[2016] = ["David Cameron", "Theresa May"]

i = 2011
while i <= 2015:
    year[i] = ["David Cameron"]
    i = i + 1

year[2010] = ["Gordon Brown", "David Cameron"]

for i in [2008,2009]:
    year[i] = ["Gordon Brown"]

for i in [2000,2001,2002,2003,2004,2005,2006]:
    year[i] = ["Tony Blair"]

year[2007] = ["Tony Blair", "Gordon Brown"]


print(f"Year 2003: {year[2003]}")
print(f"Year 2007: {year[2007]}")
print(f"Year 2010: {year[2010]}")
print(f"Year 2016: {year[2016]}")
