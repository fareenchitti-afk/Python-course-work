#Q1.
text = "Hello World"
result = text.lower()
print(result)

#Q2.
greeting = "good morning"
greeting.upper()
print(greeting)

#Q3.
data = " hello python "
data.strip()
print(data)

#Q4.
line = "Python is tough"
line.replace("tough", "easy")
print(line)

#Q5.
word = "banana"
word.count("a")
print(word)
#Q6.
info = "python is fun"
info.split()
print(info)

#Q7.
sentence = "learn python"
len(sentence)
print(sentence)


#Q8.
value = "test123"
value.isalnum()
print(value)

#Q9.
text = "HELLO"
text.lower().capitalize()
print(text)

#Q10.
email = "student@domain.com"
email.endswith(".com")
print(email)

#Q11.
marks = [45, 67, 89, 32]
marks.sort()
print(marks)

#Q12.
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

#Q13.
colors = ["red", "blue", "green"]
colors.remove("blue")
print(colors)

#Q14.
values = [1, 2, 3, 2, 1]
values.count(2)
print(values)

#Q15.
items = ["pen", "book", "pencil"]
",".join(items)
print(items)

#Q16.
scores = [100, 90, 80]
scores.reverse()
print(scores)

#Q17.
students = ("Anu", "Ravi", "Meena")
second_item = students[1]
print(students)

#Q18.
details = ("ID101", "Sita", "CSE")
list(details)
print(details)

#Q19.
data = (5, 3, 9, 1)
max(data)
print(data)

#Q20.
group = ("A", "B", "C", "D")
group[-2:]
print(group)

#Q21.
names = ["Anu", "Ravi", "Anu", "Sam"]
set(names)
print(names)


#Q22.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b))

#Q23
x = {1, 2, 3}
y = {2, 4}

print(x.intersection(y))

#Q24.
numbers = {5, 10, 15}
numbers.add(20)
print(numbers)

#Q25.
items = {1, 2, 3, 4}
items.remove(3)
print(items)

#Q26.
marks = {"Ravi": 90, "Anu": 85}
marks["Sita"] = 88
print(marks)

#Q27.
student = {"name": "Asha", "grade": "A"}
student.get("grade")
print(marks)
#Q28.
record = {"math": 75, "science": 80}
record["math"] = 85
print(record)


#Q29.
profile = {"id": 101, "name": "John"}
profile.keys()
print(profile)

#Q30.
data = {"x": 1, "y": 2}
data.pop("y")
print(data)