print("nguyễn như cường")   
print("MSSV: 235752020710047") 
def find_longest_words(text):
#Định nghĩa một hàm tên là find_longest_words với một đối số đầu vào text (là chuỗi chứa các từ).
    words = text.split()
    #Dùng phương thức .split() để tách text thành danh sách các từ, dựa trên dấu cách (mặc định).
    max_length = len(max(words, key=len))
    #max(words, key=len) tìm ra từ dài nhất trong danh sách words (dựa vào độ dài).
    #len(...) lấy độ dài (số ký tự) của từ đó.
    #Kết quả được gán vào biến max_length.
    longest_words = [word for word in words if len(word) == max_length]
    # list comprehension để tạo danh sách longest_words, chứa tất cả các từ có độ dài bằng max_length
    return longest_words
    #Trả về danh sách các từ dài nhất.
text = """Nguyễn Như Cường """
#Khai báo biến text chứa một đoạn văn bản để kiểm tra.
print(find_longest_words(text))
#Gọi hàm find_longest_words với tham số là chuỗi text, sau đó in kết quả ra màn hình.s