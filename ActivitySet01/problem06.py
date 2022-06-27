# Loops & Iterators
largest = None
smallest = None
b=[]
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
      num=int(num)
      bappend(num)
    except:    
        print("Invalid input")
largest=max(b)
smallest=min(b)
print("Maximum", largest)
print("Minimum",smallest)