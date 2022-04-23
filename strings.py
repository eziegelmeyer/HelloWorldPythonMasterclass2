print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = "Emily"
print(greeting + name)

#if we want a space, we can add that too
print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "22 years"
print(name + " is " + age_in_words + " old")
print(type(age))

print()

age_in_words = "2 years"
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

print()
#       0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#       1A :
#       01234567890123456789012345678901234567
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])
print(data[::])
print(data[::2])

