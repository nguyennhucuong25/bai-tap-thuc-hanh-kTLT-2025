from itertools import islice

def file_read_from_head(fname, nlines):
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            for line in islice(f, nlines):
                print(line.strip())  # .strip() để bỏ ký tự xuống dòng
    except FileNotFoundError:
        print(f"Không tìm thấy file: {fname}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Gọi hàm và truyền vào tên file + số dòng muốn đọc
file_read_from_head("D:\'test.txt'",1)
print("nguyễn như cường")   
print("MSSV: 235752020710047") 