'''1. Display the Python type of each value: 25, 25.0, the text "25",
 and the Boolean value True.'''
print(type(25))
print(type(25.0))
print(type("25"))
print(type(True))

'''2. Create a complex number with real part 10 and imaginary part 5.
Display its type, its real part, and its imaginary part.'''
complex_num = 10 + 5j
print(type(complex_num))
print(complex_num.real)
print(complex_num.imag)

'''3. Display the types of the Boolean value False and the text "False".'''
print(type(False))
print(type("False"))
'''4. Give a variable the number 10 and display its type. Give the same
variable the text "Ten" and display its type again.'''
var = 10
print(type(var))
var = "Ten"
print(type(var))

'''5. Two students scored 75 and 60. Display whether the scores are equal.'''
score1 = 75
score2 = 60
print(score1 == score2)

'''6. Two files are 8 MB and 5 MB. Display whether their sizes are different.'''
file1_size = 8
file2_size = 5
print(file1_size != file2_size)

'''7. Ravi is 20 and Anita is 22. Display whether Ravi is younger than Anita and whether Anita is older than Ravi.'''
ravi_age = 20
anita_age = 22
print(ravi_age < anita_age)
print(anita_age > ravi_age)

'''8. A student scored 40 and the pass mark is 40. Display whether the
   score is greater than or equal to the pass mark.'''
student_score = 40
pass_mark = 40
print(student_score >= pass_mark)

'''9. A bag weighs 15 kg and the limit is 15 kg. Display whether the bag's
   weight is less than or equal to the limit.'''
bag_weight = 15
limit = 15
print(bag_weight <= limit)

'''Topic 3 — Order, Indexing, Slicing, and Length

Use these names in order for questions 10–14:
Raju, Ram, Krishna, Arun, John.'''
'''10. Store the names in a list and display them in the given order.'''
names = ["Raju", "Ram", "Krishna", "Arun", "John"]
print(names)

'''11. Display the third name using a positive index.'''
print(names[2])

'''12. Display the second-last name using a negative index.'''
print(names[-2])

'''13. Use one slice to display the first three names, then another
    slice to display the last two names.'''
print(names[0:3])
print(names[-2:5])

'''14. Display the total number of names. Then display the first name
    using indexing and a one-item list containing it using slicing.
    Show the type of both results.'''
print(len(names))
print(names[0])
print(names[0:1])
print(type(names[0]))