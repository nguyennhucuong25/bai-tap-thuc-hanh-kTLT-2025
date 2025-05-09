# Đọc toàn bộ tệp văn bản
file_path = r"bài 7/haha.txt"  # Đường dẫn của tệp văn bản

try:
    # Mở tệp với chế độ đọc ('r')
    with open(file_path, 'r', encoding='utf-8') as file:
        # Đọc nội dung tệp vào biến content
        content = file.read()

    # In ra nội dung của tệp
    print(content)

except FileNotFoundError:
    print(f"Không thể tìm thấy tệp tại đường dẫn: {file_path}.")
except Exception as e:
    print(f"Đã có lỗi xảy ra: {e}")
print("nguyễn như cường")   
print("MSSV: 235752020710047") 