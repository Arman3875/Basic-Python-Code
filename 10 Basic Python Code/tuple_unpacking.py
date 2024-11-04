# Example 2: Tuple Unpacking
# Unpacking a tuple with multiple values into variables, including using the * operator for remaining values.

personal_info = (
    'Arman Hossain',
    1999,
    'Student',
    'EEE',
    'Mathmatics',
    'Reading','Gaming'
)
# Unpaking
name, birth_year, occupation, department, favorite_subject, *hobbies = personal_info
print('Name:', name)
print('Birth Year:', birth_year)
print('Occupation:', occupation)
print('Department:', department)
print('Favorite Subject:',favorite_subject)
print('Hobbies:', hobbies)