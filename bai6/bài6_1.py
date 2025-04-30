print("nguyễn như cường")   
print("MSSV: 235752020710047") 
class Circle(object): 
# Đây là khai báo một lớp (class) tên là Circle.
# object là lớp cơ sở mà tất cả các lớp khác trong Python đều kế thừa (mặc định).
# Lớp này sẽ được dùng để tạo các hình tròn.


   def __init__(self, r): 
# Đây là hàm khởi tạo. Nó được gọi tự động khi bạn tạo một đối tượng mới từ lớp.
# self là cách Python dùng để tham chiếu đến đối tượng hiện tại.
# r là tham số đầu vào, tức là bán kính của hình tròn. 
      self.radius = r 
############################### 
   def area(self): 
      return self.radius**2*3.14 
aCircle = Circle(2) 
print (aCircle.area())
print("nguyễn như cường")   
print("MSSV: 235752020710047") 