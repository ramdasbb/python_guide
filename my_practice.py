print "Hello World"
# raw_input("Enter ur name")
var = 101
if ( var  == 100 ) : print "Value of expression is 100"
print "************While loop**************"

count = 0; loop = 2#raw_input("Enter loop number")
print "Loop is ", loop

while (count < 5):
    print "loping ", count, loop
    count += 1

print "My name is %s, height is %d" %("Ramdas", 21)

def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

printme("Ramdas function is working as per requirement")

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = mylist.append([1,2,3,4]);
   # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist1 = [10,20,30];
changeme( mylist1 );
print "Values outside the function: ", mylist1


# Open a file
fo = open("python_file.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()
