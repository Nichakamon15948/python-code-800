# รับค่าจากผู้ใช้งาน
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

# คำนวณ BMI
bmi = weight / (height ** 2)

# แสดงผลลัพธ์ทศนิยม 1 ตำแหน่ง
print(f"BMI: {bmi:.1f}")

# จัดเกณฑ์ตามที่โจทย์กำหนด
if bmi < 18.5:
    print("Category: Underweight")
elif bmi <= 24.9:
    print("Category: Normal weight")
elif bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")