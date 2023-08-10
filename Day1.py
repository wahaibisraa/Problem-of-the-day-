#write a program that comparing three numbers and get the largest number (user should enter the numbers)

def largestNumber():
    numbers = []
    
    for i in range(3):
        num = int(input(f"Enter a number {i+1}: "))
        numbers.append(num)
        
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
                
        print(f"The largest number is: {largest} ")
        

largestNumber()