# # adding a sting and showing its id, type and value
# new_string = "This is a string"
# print(id(new_string))
# print(type(new_string))
# print(new_string)

# s1 = 'this is a string'
# s2 = 'this is "another" string'
# s3 = 'this is a \'third\' string'
# s4 = """this is a
# multiline
# string"""
# print(s1,s2,s3,s4)
# print(s3 + '\n' + s4)
#
# print(' '.join([s1, s2]))
# print(s1[::-1]) # reverses the string

# # different types of lists
# l1 = ['eggs', 'flour', 'butter']
# l2 = list([1, 'drink', 10, 'sandwiches', 0.45e-2])
# l3 = [1, 2, 3, ['a', 'b', 'c'], ['Hello', 'Python']] # nested list
# print(l1,l2,l3)
#
# # indexing lists
# print(l1[0])
# print(l1[0] +' '+l1 [1])
#
# # slicing lists
# print(l2[1:3])

# number = list(range(10))
# print(number)
# print(number[2:5])
# print(number[:])
# print(number[::2])

## concatenating and mutating lists
# print(number*2)
# print(number + l2)

# # handling nested lists
# print(l3)
# print(l3[3])
# print(l3[4])
# l3.append(' '.join(l3[4]))  # appending
# print(l3)
# l5 = (' '.join(l3[4]))
# print(l5)
#
# print(l3.pop(3)) # pop operation

# sets.. use set() or {} to write sets
# l1 = [1,1,2,3,5,5,7,9,1]
# print(set(l1))  # makes the list as a set/ it removes the duplicate elements
# s1= set(l1)
# print(1 in s1)
# print(10 in s1)

## initialize a second set
# s2 = {5, 7, 11}
# print(s1-s2)  # difference
# print(s1 | s2)  # union
# print(s1 & s2)  # intersection
# print(s1 ^ s2)  # elements which do not appear in both sets

## Dictionaries
# d1 = {'eggs': 2, 'milk': 3, 'spam': 10, 'ham': 15}
# print(d1)
# # retrieving items based on key
# print(d1.get('eggs'))
# print(d1['eggs'])
# get is better than direct indexing since it does not throw errors
# print(d1.get('orange'))
# print(d1['orange'])
## setting items with a specific key
# d1['orange'] = 25
# print(d1)
# # viewing keys and values
# print(d1.keys())
# print(d1.values())
# create a new dictionary using dict function
# d2 = dict({'orange': 5, 'melon': 17, 'milk': 10})
# print(d2)
# update dictionary d1 based on new key-values in d2
# d1.update(d2)
# print(d1)


# # complex and nested dictionary
# d3 = {'k1': 5, 'k2': [1,2,3,4,5], 'k3': {'a': 1, 'b': 2, 'c': [1,2,3]}}
# print(d3)
# print(d3.get('k3'))
# print(d3.get('k3').get('c'))

# # Tuples
# # creating a tuple with a single element
# single_tuple = (1,)
# print(single_tuple)
# # original address of the tuple
# print(id(single_tuple))
# # modifying contents of the tuple but its location changes (new tuple is created)
# single_tuple = single_tuple + (2, 3, 4, 5)
# print(single_tuple)
# print(id(single_tuple)) # different address indicating new tuple with same name
# # tuples are immutable hence assignment is not supported like lists
# single_tuple[3] = 10
# # accessing and unpacking tuples
# tup = (['this', 'is', 'list', '1'], ['this', 'is', 'list', '2'])
# print(tup[0])
# l1,l2 =tup
# print(l1,l2)


# # Files
# f = open('text_file.txt', 'w') # open in write mode
# f.write("This is some text\n") # write some text
# f.write("Hello world!")
# f.close() # closes the file
#
# # lists files in current directory
# import os
# print(os.listdir(os.getcwd()))
# f = open('text_file.txt', 'r') # opens file in read mode
# data = f.readlines() # reads in all lines from file
# print(data)  # prints the text data

# # if statement
# var = "foo"
# if var == 'spam':
#     print('spam')
# elif var == 'ham':
#     print('ham')
# else:
#     print('Neither spam nor ham')

# # illustrating for loops
# numbers = range(0,5)
# for number in numbers:
#     print(number)
#
# sum = 0
# for number in numbers:
#     sum += number
# print(sum)
#
# # role of the trailing else and break constructs
# for number in numbers:
#     print(number)
# else:
#     print("loop exited normally")
#
# for number in numbers:
#     if number < 3:
#         print(number)
#     else:
#         break
# else:
#     print("loop exited normally")

# illustrating while loops
# number = 5
# while number > 0:
#     print(number)
#     number -=1
#

# import nltk
# sentence = "The brown fox wasn't that quick and he couldn't win the race"
# word = nltk.word_tokenize(sentence)
# print(word)
# treebank_wt = nltk.TreebankWordTokenizer()
# words = treebank_wt.tokenize(sentence)
# print(words)

# def pypart(n):
#     for i in range(1,n): # to handle no. of rows
#         for j in range(0,i):  # to handle no of columns
#             print("*",end=" ")
#         print("\r")
#
# pypart(6)

def triangle(n):
    k = 2*n-2  # number of space
    for i in range(0,n): # to handle no. of rows
        for j in range(0,k): # to handle no. of spaces
            print(end=" ")
        k = k-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")

triangle(12)

