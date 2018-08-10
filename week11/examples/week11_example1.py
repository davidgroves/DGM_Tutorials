# Week11, Example1

mywritefile = open("myfile.txt", "w")
mywritefile.write("Hello File !")
mywritefile.close()

myreadfile = open("myfile.txt", "r")
print(myreadfile.read())
