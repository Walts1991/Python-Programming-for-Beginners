#Two methods for saving data to a file - writing and appending
#Writing writes only that data to a file - overwriting previous file data
#Appending adds data to existing file data - retains data

writeMe = "Example Text"

#open([filename],[method e.g. w for write])
saveFile = open("m5u1_exampleWrite.txt","w",encoding="utf-8") #encoding added
saveFile.write(writeMe)  #writes the variable 'writeMe' to the file
saveFile.close()   #closes the file - need to close to save

#if file exists it will clear file
#if file does not exist it will be created
