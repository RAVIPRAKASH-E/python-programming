numbers=(0,1,2,3,4,5,6)
count_odd=0
count_even=0
for x in numbers:
    if not x%2:
        count_even+=1
    else:
        count_odd+=1
        print("number of even numbers:"count_even)
        print("number of odd numbers:"count_odd)
