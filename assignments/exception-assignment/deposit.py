"""
Assignment-3: Function + try-except
สร้าง function ชื่อ deposit(money) จำลองการฝากเงินเข้าบัญชี
กำหนดยอดเงินเริ่มต้น 1,000 บาท
"""

balance = 1000


def deposit(money):
    try:
        amount = float(money)
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")
    else:
        global balance
        balance += amount
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")


# ทดลองใช้ function-
print(f"ยอดเงินเริ่มต้น: {balance} บาท")
money_input = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
deposit(money_input)
