'''Topic 1 — Strings: Indexing, Slicing, Concatenation, and replace()'''
'''15. From the word "Python", display the first character, the last
    character, and the number of characters.'''
word = "Python"
print(word[0])
print(word[-1])
print(len(word))

'''16. Take a slice of "Python" that gives "yth" and display it.'''
print(word[1:4])
print(word[1:-2])
print(word[-5:-2])

'''17. Store "Raju" and "Kumar" separately. Join them with one space
    and display the full name.'''
first_name = "Raju"
last_name = "Kumar"
full_name = first_name + " " + last_name
print(full_name)

'''18. Start with "Raju Kumer". Use replace() to correct the surname to
    "Kumar". Save the result separately and display both strings.'''
original_name = "Raju Kumer"
corrected_name = original_name.replace("Kumer", "Kumar")
print(original_name)
print(corrected_name)

'''19. In the text "red red blue", replace every "red" with
    "green". Display the new text.'''
text = "red red blue"
new_text = text.replace("red", "green")
print(new_text)

'''Topic 2 — List CRUD: Create, Read, Update, and Delete
Create and add'''
'''20. Create a list containing Raju and Ram. Add Arun at the end
    and display the list.'''
names = ["Raju", "Ram"]
names.append("Arun")
print(names)

'''21. Create a list containing Raju, Ram, and Arun. Insert Anita
    immediately before Ram and display the list.'''
names = ["Raju", "Ram", "Arun"]
names.insert(1, "Anita")
print(names)

'''22. Start with a list containing Raju and Ram. Add Anita and Arun
    as separate items using one call to extend(). Display the list.'''
names = ["Raju", "Ram"]
names.extend(["Anita", "Arun"])
print(names)

'''23. Create a list containing Ram, Anita, Ram, and Arun. Find the
    index of the first Ram and count how many times Ram appears.'''
names = ["Ram", "Anita", "Ram", "Arun"]
first_index = names.index("Ram")   
count = names.count("Ram")
print(f"Index of the first 'Ram': {first_index}")
print(f"Count of 'Ram': {count}")

'''24. Store 70, 85, 90, and 75 in a list. Display the second mark,
    a slice containing the first two marks, and the list's length.'''
marks = [70, 85, 90, 75]
second_mark = marks[1]
first_two_marks = marks[:2]
length_of_list = len(marks)
print(f"Second mark: {second_mark}")
print(f"First two marks: {first_two_marks}")
print(f"Length of the list: {length_of_list}")

'''25. Create a list containing Raju, Ram, and Anita. Replace Ram
    with Ramesh using its position. Display the list and its length.'''
names = ["Raju", "Ram", "Anita"]
names[1] = "Ramesh"
print(f"Updated list: {names}")
print(f"Length of the list: {len(names)}")

'''26. Put 80, 65, 90, and 75 in a list. Sort the marks from lowest
    to highest and display the list.'''
marks = [80, 65, 90, 75]
marks.sort()
print(f"Sorted marks: {marks}")

'''27. Create a list containing 80, 65, and 90 in that order. Reverse
    its current order and display the list.'''
marks = [80, 65, 90]
marks.reverse()
print(f"Reversed marks: {marks}")

'''28. Create a list containing Ram, Anita, Ram, and Arun. Remove the
    first Ram by value and display the remaining names.'''
names = ["Ram", "Anita", "Ram", "Arun"]
names.remove("Ram")
print(f"Remaining names: {names}")

'''29. Create a list containing Raju, Ram, and Anita. Use pop() to
    remove the item at index 1. Display the removed item and the list.'''
names = ["Raju", "Ram", "Anita"]
removed_item = names.pop(1)
print(f"Removed item: {removed_item}")
print(f"Remaining list: {names}")

'''30. Create a list containing Raju, Ram, and Anita. Use pop() with
    no index. Display the removed item and the remaining list.'''
names = ["Raju", "Ram", "Anita"]
removed_item = names.pop()
print(f"Removed item: {removed_item}")
print(f"Remaining list: {names}")

'''31. Create a list containing Raju, Ram, Anita, and Arun. Use one
    del statement with a slice to delete the first two names.
    Display the remaining list.'''
names = ["Raju", "Ram", "Anita", "Arun"]
del names[:2]
print(f"Remaining list: {names}")

'''32. Create a list with three names. Empty it using clear(), then
    display the list and its length.'''
names = ["Raju", "Ram", "Anita"]
names.clear()
print(f"Cleared list: {names}")
print(f"Length of the list: {len(names)}")

'''33. Store 1920 and 1080 in a tuple. Display the type, the first
    value, the last value, and the length.'''
dimensions = (1920, 1080)
print(f"Type: {type(dimensions)}")
print(f"First value: {dimensions[0]}")
print(f"Last value: {dimensions[-1]}")
print(f"Length: {len(dimensions)}")

'''34. Create a tuple containing 80, 90, 80, and 75. Use a slice to
    display the last two scores as a tuple.'''
marks = (80, 90, 80, 75)
last_two_scores = marks[-2:]
print(f"Last two scores: {last_two_scores}")

'''35. Use a tuple containing 80, 90, 80, and 75. Count how often
    80 appears and find the index of its first occurrence.'''
marks = (80, 90, 80, 75)
count_of_80 = marks.count(80)
index_of_80 = marks.index(80)
print(f"Count of 80: {count_of_80}")
print(f"Index of first occurrence of 80: {index_of_80}")

'''36. Create a tuple containing only the score 80. Display the
    tuple and its type.'''
single_score = (80,)
print(f"Tuple: {single_score}")
print(f"Type: {type(single_score)}")

'''37. Start with a tuple containing 70, 85, and 90. Create a new
    tuple with the first score corrected to 75 and the other
    scores in the same order. Display both tuples.'''
original_scores = (70, 85, 90)
corrected_scores = (75,) + original_scores[1:]
print(f"Original scores: {original_scores}")
print(f"Corrected scores: {corrected_scores}")