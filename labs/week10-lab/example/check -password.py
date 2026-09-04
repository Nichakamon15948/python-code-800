#รับค่า password จากผู้ใช้ 
# password นั้นแข็งแรงหรือไม่
# password นั้นจะแข็งแรง ถ้าประกอบด้วยตัวเลข และตัวอักษร และ @ 1 ตัว ยาวมากกว่า 8 ตัว

#ตัวอย่างหน้าจอ
# Plese input you password : Boonchoo
# Your password is not strong!

# Please input your password: Bo@o15thai
# Your password is strong! 

# รับค่า password จากผู้ใช้
password = input("Please input your password: ")

# กำหนดตัวแปรสำหรับเก็บสถานะเงื่อนไขต่างๆ
has_digit = False
has_alpha = False
at_count = password.count('@') # นับจำนวนตัว @ ใน string
is_long_enough = len(password) > 8 # ตรวจสอบความยาวว่ามากกว่า 8 หรือไม่

# วนลูปตรวจเช็คอักขระแต่ละตัวในรหัสผ่าน
for char in password:
    if char.isdigit():  
        has_digit = True
    elif char.isalpha():  
        has_alpha = True

# ตรวจสอบเงื่อนไขทั้งหมด: ต้องยาวกว่า 8, มีตัวเลข, มีตัวอักษร และมี @ แค่ 1 ตัว
if is_long_enough and has_digit and has_alpha and at_count == 1:
    print("Your password is strong!")
else:
    print("Your password is not strong!")