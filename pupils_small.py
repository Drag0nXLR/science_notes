class Pupil:
    def __init__(self, name, mark):
        name = name.split(' ')
        self.lastname = name[0]
        self.mark = mark
pupils = []
with (open('students.txt', 'r', encoding='utf-8') as file):
    for line in file:
        line = line.rstrip('\n')
        print(line)
        list = line.split(' - ')
        pupil = Pupil(list[0], int(list[1]))
        pupils.append(pupil)

print("\n\nВідмінники:")
marks =[]
for pupil in pupils:
    marks.append(pupil.mark)
    if pupil.mark == 5:
        print(f"\t{pupil.lastname}")
    else:
        continue

average = sum(marks)/len(marks)
print(f"Середня оцінка: {int(average)}")


