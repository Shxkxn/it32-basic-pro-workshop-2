x = int(input("จำนวนปืนที่รับมาขาย: "))
y = float(input("ต้นทุนปืนที่รับมา: "))
z = float(input("ราคาขาย: "))
n = int(input("จำนวนลูกน้อง: "))

cost = x * y
income = x * z
profit = income - cost
five = profit * 0.2
each = (profit - five) / n

print("ต้นทุนทั้งหมด =", cost)
print("รายได้ทั้งหมด =", income)
print("กำไรทั้งหมด =", profit)
print("บอสใหญ่ได้ =", five)
print("ลูกน้องได้คนละ =", each)