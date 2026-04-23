def check_stock(product_name):
    # ปรับข้อความให้เป็นตัวเล็กทั้งหมดเพื่อให้เช็คง่ายขึ้น
    product_name = product_name.lower() 

    if "endmill" in product_name:
        return "Endmill ของเรามีของพร้อมส่งครับ รุ่น Carbide 3 ฟัน มีสต็อกเยอะเลย"
    elif "drill" in product_name:
        return "สว่าน (Drill) ตอนนี้ต้องเช็คสต็อกหน้าร้านให้นะครับ"
    else:
        return "ขออภัยครับ รบกวนระบุชื่อสินค้าที่ต้องการให้ชัดเจนหน่อยครับ"

# ลองเรียกใช้งาน
print(check_stock("ขอราคา Endmill ครับ"))
print(check_stock("มี Drill ไหม"))