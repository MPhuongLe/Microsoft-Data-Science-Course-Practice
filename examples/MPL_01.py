print("=" * 50)
print("⭐⭐⭐ This is Phuong's first program ⭐⭐⭐")
print("=" * 50)
print()

# ============== SIMPLE STATISTICS =================

student_names = ["Phuong", "Khoa", "Thu", "Tan", "Nhi", "Cuong"]
student_scores = [88, 85, 88, 92, 80, 87]

highest_score = max(student_scores)
index_of_highest = student_scores.index(highest_score)
print(f"Student {student_names[index_of_highest]} has the highest score of {highest_score}.")

lowest_score = min(student_scores)
index_of_lowest = student_scores.index(lowest_score)
print(f"Student {student_names[index_of_lowest]} has the lowest score of {lowest_score}.")

average_score = sum(student_scores) / len(student_scores)
print(f"The average score of the class is {average_score}.")

# =============== DICTIONARY =================
score_dictionary = dict(zip(student_names, student_scores))

sorted_by_name_items = sorted(score_dictionary.items())
sorted_by_name_dict = dict(sorted_by_name_items)
print("-" * 50)
print("Student scores (sorted by name):")
print("-" * 50)
for name, score in sorted_by_name_dict.items():
    marker = "⭐" if score == highest_score else "  "
    print(f"{marker} {name}: {score} points")

sorted_by_score_items = sorted(score_dictionary.items(), key=lambda item: item[1], reverse=True)
sorted_by_score_dict = dict(sorted_by_score_items)
print("-" * 50)
print("Student scores (sorted by score):")
print("-" * 50)
for name, score in sorted_by_score_dict.items():
    marker = "⭐" if score == highest_score else "  "
    print(f"{marker} {name}: {score} points")

# ============== IMPROVEMENT =================

print("-" * 50)
print("Sort by value with itemgetter ~ More readable")
print("-" * 50)

from operator import itemgetter
score_dict = dict(zip(student_names, student_scores))
sorted_list = sorted(score_dict.items(), key=itemgetter(1), reverse=True)
sorted_dict = dict(sorted_list)
for name, score in sorted_dict.items():
    marker = "⭐" if score == highest_score else "  "
    print(f"{marker} {name}: {score} points")

# ============== END OF PROGRAM =================