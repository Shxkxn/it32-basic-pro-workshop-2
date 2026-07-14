name = input("ชื่อ: ")
age = int(input("อายุ: "))
height = int(input("ส่วนสูง: "))
power = int(input("กำลัง (1-10): "))
money = int(input("เงินติดตัว: "))

if age >= 20 and power >= 9 and height >= 175:
    print(name, "ผ่าน : หัวหน้าทีม")

elif age >= 18 and power >= 8:
    print(name, "ผ่าน : รองหัวหน้าทีม")

elif age >= 18 and power >= 7:
    print(name, "ผ่าน : สมาชิกระดับ A")

elif age >= 18 and power >= 6:
    print(name, "ผ่าน : สมาชิกระดับ B")

elif age >= 18 and power >= 5:
    print(name, "ผ่าน : สมาชิกระดับ C")

elif age < 18:
    print(name, "ไม่ผ่าน : อายุน้อยเกินไป")

elif height < 150:
    print(name, "ไม่ผ่าน : ส่วนสูงไม่ถึงเกณฑ์")

elif money < 100:
    print(name, "ไม่ผ่าน : เงินติดตัวน้อยเกินไป")

else:
    print(name, "ไม่ผ่าน")