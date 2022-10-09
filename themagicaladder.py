# Take the input from the user
user_input = input("Please enter three numbers: ")

# split the given input string into 3 parts
string_tokens = user_input.split(",")

# convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# calculate the result: a + b - c
a,b,c = int_tokens
result = a + b - c

# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# output the result
print(result)