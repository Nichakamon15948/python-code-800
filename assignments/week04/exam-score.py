

scores = []

#รับคะแนน 5 ค่า เก็บใน list
for i in range(1, 6):
    score = int(input(f"Enter score of student {i}: "))
    scores.append(score)

print() 

# ใช้ loop ตรวจสอบคะแนนทีละค่า และ ใช้ condition แสดงผล
for i in range(len(scores)):
    if scores[i] >= 50:
        status = "ผ่าน"
    else:
        status = "ไม่ผ่าน"
        
    print(f"Student {i+1}: {scores[i]} -> {status}")