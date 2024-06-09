# Creating a string
import string

String1 = "Hello, I'm a Srishti Jaitly"
print("Initial String: ")
print(String1)

# Accessing characters
print("\nAccessing characters:")
print("First character:", String1[0])
print("Last character:", String1[-1])

# String slicing
print("\nString slicing:")
print("Slicing characters from 2 index-7 position:", String1[2:7])
print("Slicing characters from 2nd to 2nd last:", String1[2:-2])

# Reversing a string
print("\nReversing a string:")
print("Reversed string:", String1[::-1])

# Updating a character
print("\nUpdating a character:")
list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("Updated String:", String2)

# Deleting entire string
print("\nDeleting entire String:")
del String1
# Uncommenting the below line will raise an error
# print(String1)

# String formatting
print("\nString formatting:")
String3 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Formatted String:", String3)

# String methods
print("\nString methods:")
print("Uppercase:", String3.upper())
print("Lowercase:", String3.lower())
print("Length:", len(String3))
print("Starts with 'Geeks'?", String3.startswith('Geeks'))
print("Ends with 'Life'?", String3.endswith('Life'))

# Splitting a string
print("\nSplitting a string:")
String4 = "Welcome,to,the,Geeks,World"
split_string = String4.split(',')
print("Split string:", split_string)

# Joining strings
print("\nJoining strings:")
joined_string = '-'.join(split_string)
print("Joined string:", joined_string)

# Finding substring
print("\nFinding substring:")
print("Index of 'For':", String3.find('For'))

# Replacing substring
print("\nReplacing substring:")
print("Replaced string:", String3.replace('Life', 'World'))

# Checking if string is digit or alpha
String5 = "12345"
String6 = "Hello"
print("\nChecking if string is digit or alpha:")
print("String5 is digit?", String5.isdigit())
print("String6 is alpha?", String6.isalpha())

# Stripping whitespace
String7 = "   Hello, World!   "
print("\nStripping whitespace:")
print("Stripped string:", String7.strip())

# Creating strings
String1 = "Hello, I'm a Geek"
String2 = "Welcome to the Geeks World"
String3 = "Geeks For Geeks"

# Concatenation
concatenated_string = String1 + " " + String2
print("Concatenated string:", concatenated_string)

# Slicing with 2 colons
print("\nSlicing with 2 colons:")
print("Every 2nd character:", String1[::2])

# Comparing operators on strings
print("\nComparing operators on strings:")
print("String1 == String2?", String1 == String2)
print("String1 != String2?", String1 != String2)
print("String1 < String2?", String1 < String2)
print("String1 > String2?", String1 > String2)

# Splitting a string
print("\nSplitting a string:")
split_string = String2.split()
print("Split string:", split_string)

# Replacing substring
print("\nReplacing substring:")
replaced_string = String1.replace("Hello", "Hi")
print("Replaced string:", replaced_string)

# Finding substring
print("\nFinding substring:")
index = String2.find("Geeks")
print("Index of 'Geeks':", index)

# Other built-in functions
print("\nOther built-in functions:")
print("ASCII letters:", string.ascii_letters)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)


# Count vowels , consonants , digits and special character
def countInString(st):
    v, c, d, s = 0 , 0, 0, 0
    for i in st:
        if ('a' <= i <= 'z') or('A' <= i <= 'Z'):
            if i in ["a","e","i","o","u"]:
                v += 1
            else:
                c += 1
        elif "0" <= i <= "9":
            d += 1
        else:
            s += 1
    return v, c, d, s


st = "dhedueeidnddnsodjd 23486@%(!68+"
v, c, d, s = countInString(st)
print("-------------------------------------")
print(f"Vowels: {v}, Consonants: {c}, Digits: {d}, Special characters: {s}")

print(len(st))
print(v+s+d+c)
