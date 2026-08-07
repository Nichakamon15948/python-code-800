# =============================================================================
# ส่วนที่ 1: เฉลยฟังก์ชันทั้ง 5 ข้อ
# =============================================================================

def welcome_message(name, course):
    return f"Welcome {name} to {course} class!"

def calculate_circle(radius):
    pi = 3.14159
    area = round(pi * (radius ** 2), 2)
    circumference = round(2 * pi * radius, 2)
    return {"area": area, "circumference": circumference}

def create_user_profile(username, age=18, premium=False):
    status = "Premium User" if premium else "Standard User"
    return f"{username} (age: {age}) - {status}"

def analyze_scores(scores):
    total = sum(scores)
    average = round(total / len(scores), 1)
    highest = max(scores)
    lowest = min(scores)
    passed = sum(1 for score in scores if score >= 70)
    
    return {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed
    }

def count_vowels_consonants(text):
    vowels_set = "aeiou"
    vowels_count = 0
    consonants_count = 0
    
    for char in text.lower():
        if char.isalpha():
            if char in vowels_set:
                vowels_count += 1
            else:
                consonants_count += 1
                
    return {"vowels": vowels_count, "consonants": consonants_count}


# =============================================================================
# ส่วนที่ 2: TEST SECTION - DO NOT MODIFY (ส่วนนี้จะทำหน้าที่เรียกใช้และปรินท์ผลลัพธ์)
# =============================================================================

def run_all_tests():
    """Test all functions and display results"""
    print("="*50)
    print("PYTHON FUNCTIONS QUIZ - TEST RESULTS")
    print("="*50)
    
    # Test Problem 1
    print("\n--- Problem 1 Tests ---")
    try:
        result1 = welcome_message("Alice", "Python")
        print(f"Test 1: {result1}")
        result2 = welcome_message("Bob", "Data Science")
        print(f"Test 2: {result2}")
        print("✓ Problem 1: PASSED")
    except Exception as e:
        print(f"✗ Problem 1: ERROR - {e}")
    
    # Test Problem 2
    print("\n--- Problem 2 Tests ---")
    try:
        result1 = calculate_circle(5)
        print(f"Test 1: {result1}")
        result2 = calculate_circle(3)
        print(f"Test 2: {result2}")
        print("✓ Problem 2: PASSED")
    except Exception as e:
        print(f"✗ Problem 2: ERROR - {e}")
    
    # Test Problem 3
    print("\n--- Problem 3 Tests ---")
    try:
        result1 = create_user_profile("john_doe")
        print(f"Test 1: {result1}")
        result2 = create_user_profile("alice", 25)
        print(f"Test 2: {result2}")
        result3 = create_user_profile("bob", 30, True)
        print(f"Test 3: {result3}")
        print("✓ Problem 3: PASSED")
    except Exception as e:
        print(f"✗ Problem 3: ERROR - {e}")
    
    # Test Problem 4
    print("\n--- Problem 4 Tests ---")
    try:
        scores1 = [85, 92, 78, 65, 88, 76, 95]
        result1 = analyze_scores(scores1)
        print(f"Test 1: {result1}")
        scores2 = [45, 67, 89, 72, 58]
        result2 = analyze_scores(scores2)
        print(f"Test 2: {result2}")
        print("✓ Problem 4: PASSED")
    except Exception as e:
        print(f"✗ Problem 4: ERROR - {e}")
    
    # Test Problem 5
    print("\n--- Problem 5 Tests ---")
    try:
        result1 = count_vowels_consonants("Hello World")
        print(f"Test 1: {result1}")
        result2 = count_vowels_consonants("Python Programming 2024")
        print(f"Test 2: {result2}")
        print("✓ Problem 5: PASSED")
    except Exception as e:
        print(f"✗ Problem 5: ERROR - {e}")
    
    print("\n" + "="*50)
    print("END OF TESTS")
    print("="*50)

# คำสั่งสำหรับเริ่มรันสคริปต์
if __name__ == "__main__":
    run_all_tests()