#รับค่า password จากผู้ใช้ 
# password นั้นแข็งแรงหรือไม่
# password นั้นจะแข็งแรง ถ้าประกอบด้วยตัวเลข และตัวอักษร และ @ 1 ตัว ยาวมากกว่า 8 ตัว

#ตัวอย่างหน้าจอ
# Plese input you password : Boonchoo
# Your password is not strong!

# Please input your password: Bo@o15thai
# Your password is strong! 

text =input("Plese input you password":)
count = 0 #ตัวแปรนี้ทำหน้าที่ในการนับ
text = 'Hello World' #กำหนดตัวอักษร
for letter in text: #สำหรับตัวอักษรใน text
    if letter == 'l':
        count += 1 
print(f"{count} letters 'l' found in '{text}'")