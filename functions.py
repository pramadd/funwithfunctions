def odd_even(a,b):
    for i in range(a,b):
        print i
        if (i%2)==0:
            print "Number is {}. This is an even number".format(i)
        else:
            print "this is an odd number"  
odd_even(1,2001)         
# printing whether its odd/even:from 1 to 2000

#-------------------------------------------------

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

#multiplying array with number
#---------------------------------------------------

#1's times the number in the original list


def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x