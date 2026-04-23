def reply_customer(message):
    if "ราคา" in message:
        return "ราคาสินค้าเริ่มต้นที่ 100 บาทครับ "
    else:
        return "สวัสดีครับ ผมคือ AI ผู้ช่วยจาก CA-GO  มีอะไรให้ช่วยเหลือครับ? "
 print(reply_customer("สอบถามราคาครับ"))  # Output: ราคาสินค้าเริ่มต้นที่ 100 บาทครับ
