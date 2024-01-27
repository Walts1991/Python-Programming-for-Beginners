#Two methods for saving data to a file - writing and appending
#Writing writes only that data to a file - overwriting previous file data
#Appending adds data to existing file data - retains data

appendMe = "Some more text"
saveFile = open("m5u2_exampleFile.txt","a",encoding="utf-8") #"a" for append, #encoding added
saveFile.write("\n") #Regular Expression - n Creates new line (s for space, t for tab)
saveFile.write(appendMe)  #Write the variable 'appendMe' to the file
saveFile.close()
