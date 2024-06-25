#same result, 2 vs 6 lines of code with just one formula @_@

counter = 1
x=1
while counter <= 2024:
  print(counter)
  counter=2**x
  x=x+1

for power in range (0,11):
  print(2**power)

#List Generator
start=int(input("Start at: "))
end=int(input("End before: "))
increment=int(input("Increment between values: "))
print()
for i in range(start,end,increment):
  print(i)
