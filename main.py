with open("file1.txt") as f:
  file1 = f.readlines()
with open("file2.txt") as f:
  file2 = f.readlines()

result = [int(num) for num in file1 if num in file2]




# Write your code above 👆

print(result)


