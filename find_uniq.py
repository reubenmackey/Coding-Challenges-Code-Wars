# https://www.codewars.com/kata/find-the-unique-number-1/train/python

# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
# findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
# It’s guaranteed that array contains more than 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
#
# This is the first kata in series:
#
# Find the unique number (this kata)
# Find the unique string
# Find The Unique

def find_uniq(arr):                                     #function Created to take an array/list of numbers
    index = 0                                           #index variable created and assigned to the value 0
    for num in arr:                                     #for loop through the array/list then compare each num in the array to the 1st and 2nd index position (both need to be true) and it will return the number that isn't.
        if num == arr[index] and num == arr[index+1]:
            pass
        else:
            return num

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))

#OUTPUT

#Result
#2
#0.55

# Time: 3342ms Passed: 55 Failed: 0
# Test Results:
#  Basic Tests
# Test Passed
#  Value = 2
# Test Passed
#  Value = 0.55
# Test Passed
#  Value = 3
# Test Passed
#  Value = 4
# Test Passed
#  Value = 5
# Test Passed
#  Value = 6
# Test Passed
#  Value = 7
# Test Passed
#  Value = 2
# Test Passed
#  Value = 1
# Test Passed
#  Value = 0
# Test Passed
#  Value = 1099511627776
# Test Passed
#  Value = -1
# Test Passed
#  Value = 1e-07
# Test Passed
#  Value = 42
# Test Passed
#  20 random tests with integers with arrays with 1000 elements
#  Result = 29411
# Test Passed
#  Result = 94668
# Test Passed
#  Result = 88349
# Test Passed
#  Result = 82613
# Test Passed
#  Result = 32671
# Test Passed
#  Result = 14083
# Test Passed
#  Result = 60100
# Test Passed
#  Result = 40727
# Test Passed
#  Result = 95822
# Test Passed
#  Result = 2807
# Test Passed
#  Result = 64476
# Test Passed
#  Result = 65063
# Test Passed
#  Result = 94735
# Test Passed
#  Result = 67069
# Test Passed
#  Result = 42252
# Test Passed
#  Result = 18755
# Test Passed
#  Result = 78658
# Test Passed
#  Result = 48715
# Test Passed
#  Result = 2695
# Test Passed
#  Result = 17152
# Test Passed
#  20 random tests with decimals with arrays with 1000 elements
#  Result = 68750.7353092311
# Test Passed
#  Result = 40936.98840351848
# Test Passed
#  Result = 80262.51066599501
# Test Passed
#  Result = 23270.352479018173
# Test Passed
#  Result = 25590.562495931244
# Test Passed
#  Result = 15626.456728325265
# Test Passed
#  Result = 42181.67731865047
# Test Passed
#  Result = 36760.657598780635
# Test Passed
#  Result = 62240.67270637918
# Test Passed
#  Result = 31944.545974456905
# Test Passed
#  Result = 67022.01654883295
# Test Passed
#  Result = 70634.50413564956
# Test Passed
#  Result = 61454.972918607666
# Test Passed
#  Result = 20212.11168667128
# Test Passed
#  Result = 20564.134359640015
# Test Passed
#  Result = 52155.87581920321
# Test Passed
#  Result = 23978.371007379035
# Test Passed
#  Result = 24200.73757547032
# Test Passed
#  Result = 90442.85759765134
# Test Passed
#  Result = 70423.34814855117
# Test Passed
# You have passed all of the tests! :)
