#mean
clinical_psychology = [100,80,90]
neuroscience = [100,90,80]
social_psychology = [80,80,80]

n_class = 3
student_num = len(clinical_psychology)

total_sum = list()
for _ in range(n_class):
    total_sum.append(0)

for student_idx in range(student_num):
    total_sum[0] += clinical_psychology[student_idx]
    total_sum[1] += neuroscience[student_idx]
    total_sum[2] += social_psychology[student_idx]
print("sum of subject",total_sum)

total_avg = list()
for student_idx1 in range(n_class):
    class_avg = total_sum[student_idx1]/student_num
    total_avg.append(class_avg)
print("average of subject",total_avg)