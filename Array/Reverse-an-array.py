# two pointer l pointer increase and right pointer decrease by one 

def reverseArray(array):
    n=len(array);
    l=0;
    r=n-1;

    while l<r:
        array[l], array[r] = array[r] ,array [l];
        l+=1
        r-=1


    return array;


array = [1,4,3,2,6,5];

print(reverseArray(array));
