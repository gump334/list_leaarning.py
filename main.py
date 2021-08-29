# Working with lists and list methods

morning_call = ["Camille", "David", "T.J"]

print(morning_call[0])
print()

# looping through list
for x in morning_call:
  print(x +"\n")

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
print("No words start with the letter thats inputted")
print(morning_call)

