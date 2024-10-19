#1 reverse a string

'''name = "Vivek Kumar"
name_reverse = name[::-1]
print(name_reverse)
'''

#2 count the number of vowel in string
'''name = "Vivek Kumar"
vowel = ["a", "e", "i", "o", 'u']
countv = 0
for i in name.lower():
    if i in vowel:
        countv += 1
print("Number of vowel", countv)
'''

#3 palindrome question

'''name = "mad am"

def is_palindrome(s):
    #convert all the case in lower
    s=s.lower()
    #removespace
    s = s.replace(" ","")
    print(s)
    #reverse to check
    s_reverse = s[::-1]
    #check
    if s==s_reverse:
        print("Yes")
    else:
        print("No")

is_palindrome(name)'''

# anagram
'''
def is_anagram(str1, str2):
    #lower to str1, str2
    str1 = str1.lower()
    str2 = str2.lower()
    #remove space
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    #sort, they should be eqaul if anagram
    so_str1 =sorted(str1)
    so_str2 =sorted(str2)
    return so_str1 ==so_str2

result = is_anagram("vivek","kumar")
print(result)
 - False
result = is_anagram("silent","listen")
print(result)
- True

# learning - sorted will return sorted but not change the orginal, so so_str1 is needed
'''

#occurance

'''name = "Hello Hello Vivek"
substr = "Hello"
def sub_occurance(name, substr):
    return name.count(substr)


result = sub_occurance(name, substr)
print(result)'''

#6 string compression

'''s = 'aaabsssc'

prev_s = s[0]
compressed_s = ""
count_s = 1

for i in range(1,len(s)):
    if prev_s == s[i]:
        count_s += 1
    else:
        compressed_s = compressed_s + f"{prev_s}{count_s}"
        prev_s = s[i]
        count_s = 1
#handling last character because it will be left if last two character are same

compressed_s = compressed_s + f"{s[-1]}{count_s}"
print(compressed_s)'''

#7 string has unique character

'''def is_unique(s) :
    seen = set()
    for i in s:
        if i in seen:
            return False
        else :
            seen.add(i)
    return True
result = is_unique("vivek")
print(result)'''

#8 string to upper or lower case

str = "vivek"
'''print(str.upper())
print(str.lower())
print(str.title())
print(str.casefold())
print(str.count("v"))'''

#9 number of words

'''str = "vivek"
print(len(str))
'''
#10 concatenate
'''
str = "vivek"
str2 = "kumar"
print("/".join([str,str2]))
print(" ".join([str,str2]))'''

#11

'''def remove_occurance(str, s):
    result = ""
    for char in str:
        if char != s:
            result += char
    return result

result = remove_occurance("vivek", "v")
print(result) '''
#ii approach
'''def remove_occurance(str, s):
   return str.replace(s,"")

result = remove_occurance("vivek", "v")
print(result)'''

#12 remove largest
'''numbers =[1,2,3,4,5,43,45, 2, 3]
unique_numbers = list(set(numbers))  # Remove duplicates
unique_numbers.sort()  # Sort the list
if len(unique_numbers) < 2:  # Check if there are at least 2 unique numbers
        print("None") # Return None if there isn't a second largest number
print(unique_numbers[-2]) # Return the second largest number'''''

#13 occurance of each element in list > use of dictionary concept

'''my_list = [1,2,3,5,35,6,32,4,2,22,1]

list_occurance = {} # creating a dict to store number as key and count as value

for i in my_list:
    if i in list_occurance:
        list_occurance[i] += 1
    else:
        list_occurance[i] =1

my_list_final = list(list_occurance.keys())
list_occurrence = list(list_occurance.values())

# Print the results
print("Unique items:", my_list_final)
print("Occurrences:", list_occurrence)'''

#14 sway the list

'''my_list = [1,2,3,4]

start_index = 0
end_index = len(my_list)-1

while start_index<end_index:
    my_list[start_index], my_list[end_index] = my_list[end_index], my_list[start_index]
    start_index += 1
    end_index -= 1

print(my_list)'''

#15
'''def remove_duplicates(lst):
    seen = set()  # To track seen elements
    result = []   # To store unique elements in original order

    for item in lst:
        # Only add the item if it hasn't been seen before
        if item not in seen:
            result.append(item)
            seen.add(item)  # Mark item as seen

    return result
lst = [1,2,2,2,3,4,4]
result= remove_duplicates(lst)
print(result)
    '''



#16

'''lst = [1,2,3,4,52,6,3]
for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        return False
return True'''

#17

'''def merge_and_sort_lists(lst1, lst2):
    lst1.extend(lst2)
    lst1.sort()
    return lst1

lst1 = [1, 3, 5, 7]
lst2 = [2, 4, 6, 8]

merged = merge_and_sort_lists(lst1, lst2)
print(merged)
'''

#18
'''def list_intersection(lst1, lst2):
    intersection = []
    for element in lst1:
        if element in lst2:
            intersection.append(element)
    return intersection

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]

result = list_intersection(lst1, lst2)
print(result)
'''

#19

'''def list_union(lst1, lst2):
    union_list = lst1 + lst2  
    return list(set(union_list)) 
    
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]

result = list_union(lst1, lst2)
print(result)
'''

#20
'''import random
my_list = [1, 2, 3, 4, 5, 6]

shuffled_list = my_list[:]
random.shuffle(shuffled_list)

print("Original list:", my_list)
print("Shuffled list:", shuffled_list)
'''

#21
'''def common_elements(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    
    common_set = set1.intersection(set2)

    common_tuple = tuple(common_set)
    
    return common_tuple

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

result = common_elements(tuple1, tuple2)
print(result) 
'''

#23 tuple then join the clened tuple

'''
tuple1_input = input("Enter the first tuple elements separated by commas: ")
tuple2_input = input("Enter the second tuple elements separated by commas: ")

tuple1_list = tuple1_input.split(',')
tuple2_list = tuple2_input.split(',')

cleaned_tuple1 = []
cleaned_tuple2 = []

for item in tuple1_list:
    cleaned_tuple1.append(item.strip()) 

for item in tuple2_list:
    cleaned_tuple2.append(item.strip()) 

tuple1 = tuple(cleaned_tuple1)
tuple2 = tuple(cleaned_tuple2)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
'''

#24 wrirte a code prompt user to enter two string
# then print the element that are present in first but not in second

'''# Prompt user for input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

list1 = list(string1)
list2 = list(string2)

 unique_elements = []

for char in list1:
    if char not in list2:  # Check if the character is not in the second list
        unique_elements.append(char)  # Add to unique elements list

# Print the result
print("Elements present in the first string but not in the second:", ''.join(unique_elements))
'''

#26 takes two sets of characters as input and prints their union
'''def get_union_of_sets(set1, set2):
    # Calculate the union of the two sets
    return set1.union(set2)

# Get user input for the first set
set1_input = input("Enter the first set of characters (separated by commas): ")
# Convert input string into a set
set1 = set(item.strip() for item in set1_input.split(','))

# Get user input for the second set
set2_input = input("Enter the second set of characters (separated by commas): ")
# Convert input string into a set
set2 = set(item.strip() for item in set2_input.split(','))

# Get the union of the two sets
result_union = get_union_of_sets(set1, set2)

# Print the result
print("Union of the two sets:", result_union)
'''

#27 two tuple of integer as input and it
# should return maximum and minimun value from tuple

'''def find_max_min_from_tuples(tuple1, tuple2):
    # Combine both tuples
    combined_tuple = tuple1 + tuple2
    # Find maximum and minimum values
    max_value = max(combined_tuple)
    min_value = min(combined_tuple)
    return max_value, min_value

# Get user input for the first tuple
tuple1_input = input("Enter the first tuple of integers (separated by commas): ")
# Convert input string into a tuple of integers
tuple1 = tuple(int(item.strip()) for item in tuple1_input.split(','))

# Get user input for the second tuple
tuple2_input = input("Enter the second tuple of integers (separated by commas): ")
# Convert input string into a tuple of integers
tuple2 = tuple(int(item.strip()) for item in tuple2_input.split(','))

# Find maximum and minimum values
max_value, min_value = find_max_min_from_tuples(tuple1, tuple2)

# Print the results
print("Maximum value from both tuples:", max_value)
print("Minimum value from both tuples:", min_value)
'''

#28 code to define two set of integers and
# print the union, intersection and difference of tow sets
'''# Define two sets of integers
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Calculate union
union_set = set1 | set2  # Alternatively, you can use set1.union(set2)

# Calculate intersection
intersection_set = set1 & set2  # Alternatively, you can use set1.intersection(set2)

# Calculate difference (set1 - set2)
difference_set = set1 - set2  # Alternatively, you can use set1.difference(set2)

# Print the results
print("Set 1:", set1)
print("Set 2:", set2)
print("Union of Set 1 and Set 2:", union_set)
print("Intersection of Set 1 and Set 2:", intersection_set)
print("Difference of Set 1 (Set 1 - Set 2):", difference_set)
'''

#29

'''def count_occurrences(tup, element):
    # Count the occurrences of the element in the tuple
    count = tup.count(element)
    return count

# Prompt the user for input
tuple_input = input("Enter a tuple (elements separated by commas): ")
element_input = input("Enter the element to count: ")

# Convert the input string into a tuple
# Remove any spaces around elements and split by comma
tup = tuple(item.strip() for item in tuple_input.split(','))

# Get the count of occurrences
occurrences = count_occurrences(tup, element_input)

# Print the result
print(f"The element '{element_input}' occurs {occurrences} time(s) in the tuple {tup}.")
'''



#35 code to invert a dictionary, swapping keys and values.
#ensure that the inversted dictionary correctly handles case where

#mUltiple keys have the same value by storing a keys as list in the inversted dictonar

'''def invert_dictionary(original_dict):
    inverted_dict = {}
    
    for key, value in original_dict.items():
        # If the value is already a key in the inverted dictionary
        if value in inverted_dict:
            # If it's not a list, convert it to a list
            if not isinstance(inverted_dict[value], list):
                inverted_dict[value] = [inverted_dict[value]]
            # Append the current key to the list
            inverted_dict[value].append(key)
        else:
            # Assign the key to the value
            inverted_dict[value] = key
            
    return inverted_dict

# Example usage
original_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3
}

inverted_dict = invert_dictionary(original_dict)
print("Original Dictionary:", original_dict)
print("Inverted Dictionary:", inverted_dict)
'''