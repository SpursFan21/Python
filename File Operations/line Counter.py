def fileCount(fname):
    i=0
    with open (fname) as f:
        for lines in f:
            i+=1
    return i
print("number of line in the file", fileCount("geek.txt"))