# เขียนโปรแกรมรับค่าข้อความจากผู้ใข้
# 1 รับค่าข้อความจากผู้ใช้ เป็นตัวแปล str ชื่อtext
# 2 รับค่าอักขระที่ต้องการนับในข้อความ text
# 3 ดำเนินการนับอักขระตามที่ผู้ใช้การ และแสดงออกทางหน้าจอ


# ตัวอย่างหน้าจอ
# Input your text : Boonchoo Jitnupong
# Which character do you want to count : o
# 5 letters 'o' found in Boonchoo Jitnupong

print("\n=== ITERATING THROUGH STRING ===") 
count = 0 #ตัวแปรนี้ทำหน้าที่ในการนับ
text = input('Input you text') #กำหนดตัวอักษร
x = input('Which character do you want to count : ')

for letter in text: #สำหรับตัวอักษรใน text
    if letter == 'x':
        count += 1 
print(f"{count} letters 'x' found in '{text}'")




