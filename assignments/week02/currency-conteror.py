# กำหนดอัตราแลกเปลี่ยน
exchange_rate = 35.5

# ให้ผู้ใช้เลือกทิศทางการแปลง
print("Choose conversion direction:")
print("1: THB to USD")
print("2: USD to THB")
choice = input("Enter 1 or 2: ")

# รับจำนวนเงิน
amount = float(input("Enter the amount to convert: "))

if choice == '1':
    # แปลงบาทเป็นดอลลาร์ (หารด้วยอัตราแลกเปลี่ยน)
    result = amount / exchange_rate
    print(f"Calculation formula: {amount} / {exchange_rate}")
    print(f"Result: {result:.2f} USD")
    
elif choice == '2':
    # แปลงดอลลาร์เป็นบาท (คูณด้วยอัตราแลกเปลี่ยน)
    result = amount * exchange_rate
    print(f"Calculation formula: {amount} * {exchange_rate}")
    print(f"Result: {result:.2f} THB")
    
else:
    print("Invalid choice. Please run the program again.")