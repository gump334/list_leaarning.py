# Working with lists and list methods

morning_call = ["Camille", "David", "T.J"]

# looping through list
for x in morning_call:
  print(f"{x.upper()} It's a pleasure to have you on this call today. \n")
print("Thank you all for joining the morning call\n")

# appending to list
morning_call.append("Terrell")
print(morning_call)

courses = ["python", "terraform", "git", "linux"]

for x in courses:
  morning_call.append(x)
print(morning_call)
print()

# remove a word that start witha certain letter from a lisr 
for x in morning_call[:]:
  if x.startswith("g"):
    morning_call.remove(x)
print("No words start with the letter thats inputted\n")
morning_call.sort() # sort my list from Caps to lowercase order
print(morning_call)
print()

#using range method for creating a list of numbers.
# Range always end 1 number less then the number that you put in the brackets
for num in range(6):
  print(num)

numbers = list(range(1,11))
print(numbers)
print()

# using range to get even numbers
even_numbers = list(range(2, 21, 2))
print(even_numbers)
print()

#square root 
squares = []
for value in range(1,11):
  square = value ** 2
  squares.append(square)
print(squares)
print()

#power of 2
powers = []
for value in range(1,11):
  powers.append(value*value)
print(powers)
print()

#print the values of the power output to dollar signs. let's get money
for num in powers:
  print(num * "$")

# getting the min, man and sum value of the  powers lists
print(min(powers))
print(max(powers))
print(sum(powers))
print()

#list comprehensions
listpowers =  [value * value for value in range(1,11)]
print(listpowers)

