def findMissing(arr,n):
    arraysum = sum(arr)             # Calculate the sum of given array
    totalsum = (n+1)*n//2           # Equation for finding sum of n integer
    print(abs(totalsum-arraysum))
arr = [1,2,3,5,6,7]
n = 7
findMissing(arr,n)