# Example 9: Dictionary Filtering Based on Conditions
student_score = {

    'Arman': 89,
    'Rasel': 80,
    'Kobir': 49,
    'Sakib': 58,
    'Tonny': 78,
    'Tanjila': 69,
    'Nusrat': 76,
}
filtered_scores = {Name: student_score for Name, student_score in student_score.items() if student_score >= 75}
print('Filtered Scorea:',filtered_scores)
                   