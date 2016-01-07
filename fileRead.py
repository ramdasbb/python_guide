file = open("resume.txt","r+")
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
file.close();

print "Word************** count"

for w,c in wordcount.items():
    print w,c        


