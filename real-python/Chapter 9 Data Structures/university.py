universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats():

    enrolled_students = [university[1] for university in universities]

    annual_fees = [university[2] for university in universities]

    return enrolled_students, annual_fees

def mean():
    total_students_mean = sum(enrollment_stats()[0])/len(enrollment_stats()[0])

    total_tuition_mean = sum(enrollment_stats()[1])/len(enrollment_stats()[1])

    return total_students_mean, total_tuition_mean

def median():
    ordered_students_list = sorted(enrollment_stats()[0])

    ordered_tution_list = sorted((enrollment_stats()[1]))


    list_len = len(ordered_students_list)
    mid = (list_len - 1) // 2

    if mid % 2 == 0:
        median_students = (ordered_students_list[mid] + ordered_tution_list[mid])/2
        
        median_tuition = (ordered_tution_list[mid] + ordered_tution_list[mid + 1])/2

        return round(median_students), round(median_tuition)
    else:
        return ordered_students_list[mid], ordered_tution_list[mid]

print("******************************")
print(f'Total students: {sum(enrollment_stats()[0])}')
print(f'Total tuition: {sum(enrollment_stats()[1])}\n')

print(f'Student mean: {mean()[0]:.2f}')
print(f'Student median: {median()[0]}\n')

print(f'Tuition mean: {mean()[1]:.2f}')
print(f'Tuition median: {median()[1]}')