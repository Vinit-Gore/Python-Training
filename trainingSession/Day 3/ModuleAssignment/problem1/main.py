from Strings import operations

s1 = "Hello"
s2 = "How are you"

print(operations.Concat(s1, s2))
print(operations.Substring(s1, s2))

s1 = "How"
print(operations.Substring(s1, s2))

s1 = "   How     "
print(s1)
print(operations.Trim(s1))
print("Length of s1 : ", operations.Length(s1))

s1 = "SOS"
print(operations.Pallindrome(s1))

print(operations.Uppercase(s2))
print(operations.Lowercase(s2))
print(operations.Capitalize(s2))
