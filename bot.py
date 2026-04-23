def check_stock(product_name):
    # ปรับข้อความให้เป็นตัวเล็กทั้งหมดเพื่อให้เช็คง่ายขึ้น
    product_name = product_name.lower() 

    if "endmill" in product_name:
        return "Endmill ของเรามีของพร้อมส่งครับ รุ่น Carbide 3 ฟัน มีสต็อกเยอะเลย"
    elif "drill" in product_name:
        return "สว่าน (Drill) ตอนนี้ต้องเช็คสต็อกหน้าร้านให้นะครับ"
    elif "holder" in product_name:
        return "Holder ของเรามีหลายรุ่นครับ รุ่นที่นิยมคือ BT40 ใช้กับเครื่อง Machining Center มีสต็อกพร้อมส่งครับ"
    elif "insert" in product_name:
        return "Insert ของเรามีหลายรุ่นครับ ยี่ห้อ PILOT ยอดนิยามมากครับ มีหลากหลายเกรดให้เลือกครับ"
    else:
        return "ขออภัยครับ รบกวนระบุชื่อสินค้าที่ต้องการให้ชัดเจนหน่อยครับ"

# ลองเรียกใช้งานvvvvvv
print("---ระบบเช็คสต็อก CA-GO เริ่มทำงานแล้ว (พิมพ์ 'exit' เพื่อออก)---")
while True: # สั่งให้ระบบทำงานต่อเนื่องจนกว่าจะพิมพ์ 'exit'
    user_input = input("ลูกค้าพิมพ์ว่าอะไรคะ?: ")
   # ถ้าลูกค้าพิมพ์ 'exit' ให้หยุดการทำงานของระบบ ssssssvกกก
    if user_input.lower() == 'exit':# 1. ส่งสิ่งที่ลูกค้าพิมพ์ไปให้พนักงาน check_stock วิเคราะห์
        print("ขอบคุณที่ใช้บริการ CA-GO ครับ สวัสดีครับ!")
        break  
        answer = check_stock(user_input) # 2. รับคำตอบจาก check_stock แล้วเก็บไว้ในตัวแปร answer
        print("AI ตอบว่า: " + answer) # 3. แสดงคำตอบ
        print("_" * 30) # 4. แสดงข้อความเตือนให้ลูกค้าพิมพ์คำถามใหม่