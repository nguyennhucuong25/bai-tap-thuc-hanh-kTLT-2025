full_name = input('Nhập tên người: ')
parts = full_name.split()

if len(parts) >= 2:
    last_name = parts[0]           # Họ (từ đầu tiên)
    first_name = parts[-1]         # Tên riêng (từ cuối cùng)
else:
    last_name = full_name
    first_name = ''

print('Họ:', last_name)
print('Tên riêng:', first_name)
print("nguyễn như cường")   
print("MSSV: 235752020710047")
