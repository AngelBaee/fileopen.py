#4 types of opening files:

#"r"- read
#"a" -append
#"w"-write
#"x"-create
#"t"-text
#"b"-binary


#They have the same function, both are the same

#OPEN FILE ON THE SERVER

f = open("C:\Users\99293\fileopen.py\blaa.txt" ,"r")
print(f.read(5))

#return one line by using the readline() methodz;

f = open("blaa.txt", "r")
print(f.readline())

#read() moethod returns the whole code but it is possible to return some part of that :

f = open("blaa.txt", "r")
print(f.read(5))

#by calling readline() 2 times we may can raed the 2 first lines:

f = open("blaa.txt", "r")
print(f.readline())
print(f.readline())

#by looping through the lines of the file, we can read the whole file, line by line:

f = open("blaa.txt", "r")
for x in f:
    print(x)

#close the file when you are done with it:

f = open("blaa.txt", "r")
print(f.readline())
f.close()    