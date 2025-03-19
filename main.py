def product_of_even_position(lst):
    product =1
    for i in range(0, len(lst), 2):
        product *=lst[i]
    return product

def sum_of_odd_postion(lst):
    total=0
    for i in range(1,len(lst),2):
        total +=lst[i]
    return total
n1= int(input("Enter size of first list : "))
n2= int(input("Enter size of Second list : "))

print(f"Enter {n1} elements for the first list: ")
list1 = list(map(int, input().split()))

print(f"Enter {n2} elements for the Second list: ")
list2 = list(map(int, input().split()))

if len(list1) !=n1 or len(list2) !=n2:
    print("Error: The size dose not match")
else:
    product1 = product_of_even_position(list1)
    sum2=sum_of_odd_postion(list2)

    if sum !=0 and product1 % sum2 == 0:
        print("The product is completely divsible by the sum")

    else:
        print("The product is Not divisible by the sum")

print("done")
