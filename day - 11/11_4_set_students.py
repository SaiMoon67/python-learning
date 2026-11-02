group1 = {"Анна", "Кирилл", "Мария", "Дмитрий", "Екатерина"}
group2 = {"Иван", "Ольга", "Сергей", "Дмитрий", "Анна"}
big_group = group1 | group2
common_students = group1 & group2
group1_only = group1 - group2

print("Объединение групп:", big_group)
print("Общие студенты в обеих группах:", common_students)
print("Студенты только из первой группы:", group1_only)  