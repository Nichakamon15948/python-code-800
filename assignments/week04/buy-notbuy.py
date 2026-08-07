

prices = []

#  รับราคาสินค้า 6 ค่าและเก็บใน list
print("Enter prices of 6 items:")
for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    prices.append(price)

print()

# รับงบประมาณรวม 1 ค่า
budget = int(input("Enter total budget: "))
print()

# ตัวแปรสำหรับเก็บยอดใช้จ่ายสะสม และ list สินค้าที่ซื้อได้
current_total = 0
bought_items = []

#ใช้ loop และ if-else ตรวจสอบราคาสินค้า
for i in range(len(prices)):
    price = prices[i]
    
    # ถ้ายอดสะสมบวกราคาสินค้าปัจจุบันไม่เกินงบประมาณ
    if current_total + price <= budget:
        print(f"Item {i+1} = {price} -> buy")
        current_total += price       # อัปเดตยอดใช้จ่ายสะสม
        bought_items.append(price)   # เก็บรายการที่ซื้อได้
    else:
        # ถ้าเกินงบประมาณ
        print(f"Item {i+1} = {price} -> cannot buy")
        
    print(f"Current total = {current_total}")
    print()

# คำนวณงบประมาณคงเหลือ
remaining_budget = budget - current_total

# แสดงรายการสินค้าที่ซื้อได้ ยอดใช้จ่าย และงบคงเหลือ
print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {remaining_budget}")