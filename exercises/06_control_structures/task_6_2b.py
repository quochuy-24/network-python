# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

The message "Invalid IP address" should be printed only once,
even if several chacks are not passed.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
while True:
    # PHẢI CÓ "" ở trong input để sửa lỗi TypeError của bộ test
    ip_add = input("")
    
    if not ip_add:
        continue
        
    ip_parts = ip_add.split('.')
    is_valid = True

    # 1. Kiểm tra tính hợp lệ
    if len(ip_parts) != 4:
        is_valid = False
    else:
        for part in ip_parts:
            # Kiểm tra xem có phải là số và nằm trong dải 0-255 không
            if not (part.isdigit() and 0 <= int(part) <= 255):
                is_valid = False
                break

    # 2. Xử lý logic vòng lặp
    if is_valid:
        # Nếu đúng thì thoát ra ngay, KHÔNG in gì ở đây cả
        break
    else:
        # Nếu sai thì in thông báo (đúng chữ hoa/thường) rồi lặp lại
        print("Invalid IP address")

# 3. PHẦN PHÂN LOẠI (Nằm ngoài vòng lặp while)
# Lúc này chắc chắn ip_add đã hợp lệ
first_byte = int(ip_parts[0])

if ip_add == '255.255.255.255':
    print('local broadcast')
elif ip_add == '0.0.0.0':
    print('unassigned')
elif 1 <= first_byte <= 223:
    print('unicast')
elif 224 <= first_byte <= 239:
    print('multicast')
else:
    print('unused')