print("nguyễn như cường")   
print("MSSV: 235752020710047") 
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam (Nguoi):
    def getGender(self):
        return"nam"
class Nu(Nguoi):
    def getGender( self):
        return"Nu"

aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())
print("nguyễn như cường")   
print("MSSV: 235752020710047") 