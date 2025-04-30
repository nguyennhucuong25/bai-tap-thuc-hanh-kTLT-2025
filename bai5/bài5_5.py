# main.py
import my_module

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập giá trị các phần tử của danh sách
lst = []
for i in range(n):
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Sử dụng các hàm từ module mymodule
max_value = my_module.find_max(lst)
# Trả về ptử lớn nhất
min_value = my_module.find_min(lst)
# Trả về ptử nhỏ nhất
sorted_list = my_module.sort_list(lst)
# trả về danh sách đã được sắp xếp
# In kết quả
print(f"Phần tử lớn nhất trong danh sách: {max_value}")
print(f"Phần tử nhỏ nhất trong danh sách: {min_value}")
print(f"Danh sách sau khi sắp xếp: {sorted_list}")
print("nguyễn như cường")   
print("MSSV: 235752020710047") 