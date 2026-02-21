# bio_card.py

# Variables
name = "John Doe"
age = 20
course = "Python Programming"
college = "ABC University"
email = "john@example.com"

# Title
title = "STUDENT BIO CARD"

# Box width
width = 40

print("=" * width)
print(title.center(width))
print("=" * width)

print(f"Name    : {name}")
print(f"Age     : {age} years")
print(f"Course  : {course}")
print(f"College : {college}")
print(f"Email   : {email}")

print("=" * width)