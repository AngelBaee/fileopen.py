f = open("blaa.txt", "a")
f.write("I'm trying to add something")
f.close()

#open and read the file after appending:

f = open("blaa.txt", "r")
print(f.read())

#open the file to overwrite the content
f = open("blaa.txt", "w")
f.write("Wooops, I have delted the content")
f.close()

#open and read the file after the overwriting
f = open("blaa.txt", "r")
print(f.read())
