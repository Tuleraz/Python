largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        input_num = float(num)
    except:
        print("Invalid input")
        continue
    if(smallest is None): smallest = input_num
    if(largest is None): largest = input_num
    if(largest < input_num):
        largest = input_num
    if (smallest > input_num):
        smallest = input_num
print("Maximum is", largest)
print("Minimum is", smallest)
