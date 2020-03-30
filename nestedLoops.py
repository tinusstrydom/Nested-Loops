# Nested Loops
# Tinus Strydom
# Program nested loop to calculate pyramid

#use for loop from range from 1 to 9
#nested loop to start from 1 to i+1
#keep in mind if you dont add 1 it won't start at 1(i=2 j=1 if run to test )
#print out, placeholder replaced but i multiplied by j 
for i in range(1,10):
    for j in range(1,i+1):
        #print("i"+str(i),"j"+str(j)) #test if you take the plus 1 away to see where it starts
        print("%d" % (i*j),end=' ')
    print(" ")

