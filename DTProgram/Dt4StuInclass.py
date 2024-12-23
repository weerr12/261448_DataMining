from scipy import linalg
import numpy as np
from numpy import loadtxt
import math
from Dtreefunc import *
import re


f = open("D:/Grade3.2 CMU CPE/Data_Mining/DTProgram/buycom.txt", "r")
X=f.readlines()
#เตรียม พื้นที่เพื่อเก็บผลการคำนวณแยกตาม class
L=2 #col (2 class)
N=3 #col(3 class)
M=3 #row

age=np.zeros(3)
ageCI=[[0 for i in range(M)] for j in range(N)] # zero matrix 3 rows 3 columns (class and info gain of age)

# ให้นศ ทำ zero matrix 3 rows 3 columns (class and info gain of income)
income=np.zeros(3)
incomeCI=[[0 for i in range(M)] for j in range(N)] # zero matrix 3 rows 3 columns (class and info gain of income)

stu=np.zeros(2)
stuCI=[[0 for i in range(M)] for j in range(L)]# zero matrix 3 rows 2 columns (class and info gain of student)

# ให้นศ ทำ zero matrix 3 rows 3 columns (class and info gain of credit)
credit=np.zeros(2)
creditCI=[[0 for i in range(M)] for j in range(L)]# zero matrix 3 rows 2 columns (class and info gain of credit)
buy = np.zeros(2)

#วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
for i in range(0,15):
    # age 
    if ((X[i].count('<=30')==1)): 
        age[0]+=1 # total sample tha age <=30
        if ((X[i].count('<=30')==1)) and (X[i].count('No')==1):
            ageCI[0][0]+=1 #class no
        else:
            ageCI[0][1]+=1 #class yes
    elif(X[i].count('31-40')==1):
        age[1]+=1
        if ((X[i].count('31-40')==1)) and (X[i].count('No')==1):
            ageCI[1][0]+=1
        else:
            ageCI[1][1]+=1
    elif(X[i].count('>=40')==1):
        age[2]+=1
        if ((X[i].count('>=40')==1)) and (X[i].count('No')==1):
            ageCI[2][0]+=1
        else:
            ageCI[2][1]+=1
    #ให้นักศึกษาทำต่อจนครบทุก Attb ในห้องเรียน
    # income
    if (X[i].count('low')==1):
        income[0]+=1
        if ((X[i].count('low')==1)) and (X[i].count('No')==1):
            incomeCI[0][0]+=1
        else:
            incomeCI[0][1]+=1
    elif(X[i].count('medium')==1):
        income[1]+=1
        if ((X[i].count('medium')==1)) and (X[i].count('No')==1):
            incomeCI[1][0]+=1
        else:
            incomeCI[1][1]+=1
    elif(X[i].count('high')==1):
        income[2]+=1
        if ((X[i].count('high')==1)) and (X[i].count('No')==1):
            incomeCI[2][0]+=1
        else:
            incomeCI[2][1]+=1
    # student
    if (X[i].count('s_no')==1):
        stu[0]+=1
        if ((X[i].count('s_no')==1)) and (X[i].count('No')==1):
            stuCI[0][0]+=1
        else:
            stuCI[0][1]+=1
    elif(X[i].count('s_yes')==1):
        stu[1]+=1
        if ((X[i].count('s_yes')==1)) and (X[i].count('No')==1):
            stuCI[1][0]+=1
        else:
            stuCI[1][1]+=1
    # credit rating
    if (X[i].count('fair')==1):
        credit[0]+=1
        if ((X[i].count('fair')==1)) and (X[i].count('No')==1):
            creditCI[0][0]+=1
        else:
            creditCI[0][1]+=1
    elif(X[i].count('excellent')==1):
        credit[1]+=1
        if ((X[i].count('excellent')==1)) and (X[i].count('No')==1):
            creditCI[1][0]+=1
        else:
            creditCI[1][1]+=1

    if (X[i].count('No')==1):
        buy[0]+=1
    elif(X[i].count('Yes')==1):
        buy[1]+=1


# calculate information gain of dataset and attb
# info D,age,income,stu,credit
info = np.zeros(4)
InD=entropy(buy[1],buy[0])

ageCI[0][2]=entropy(ageCI[0][0],ageCI[0][1]) 
ageCI[1][2]=entropy(ageCI[1][0],ageCI[1][1])
ageCI[2][2]=entropy(ageCI[2][0],ageCI[2][1])

incomeCI[0][2]=entropy(incomeCI[0][0],incomeCI[0][1])
incomeCI[1][2]=entropy(incomeCI[1][0],incomeCI[1][1])
incomeCI[2][2]=entropy(incomeCI[2][0],incomeCI[2][1])

stuCI[0][2]= entropy(stuCI[0][0],stuCI[0][1])
stuCI[1][2]= entropy(stuCI[1][0],stuCI[1][1])

creditCI[0][2]= entropy(creditCI[0][0],creditCI[0][1])
creditCI[1][2]= entropy(creditCI[1][0],creditCI[1][1])

# หาค่า gain แบบไม่ใช้ และใช้ฟังก์ชัน
"""
การหาแบบไม่ใช้ฟังก์ชัน
Info_ageD = ((age[0]/14)*ageCI[0][2])+((age[1]/14)*ageCI[1][2])+((age[2]/14)*ageCI[2][2])
print("InfoD age is",Info_ageD)
print("Age Ci [:],[2] is",[ageCI[0][2],ageCI[1][2],ageCI[2][2]])
print("InfoD age is",Info_ageD)
"""
Info_ageD = inforD(age,[ageCI[0][2],ageCI[1][2],ageCI[2][2]])
Info_incomeD = inforD(income,[incomeCI[0][2],incomeCI[1][2],incomeCI[2][2]])
Info_studentD = inforD(stu,[stuCI[0][2],stuCI[1][2]])
Info_creditD = inforD(credit,[creditCI[0][2],creditCI[1][2]])

# แสดงผลการทำงานรอบแรก
"""
print("Age count is", age)
print("income count is",income)
print("student count is",stu)
print("credit rating count is",credit)
print("Buy computer count is",buy)
print("Age Info relate to class",ageCI)
print("Income Info relate to class",incomeCI)
print("Student Info relate to class",stuCI)
print("Credit rating Info relate to class",creditCI)

print("Info(D) is %5.3f" % InD)
print("Info(age <=30(2,3) is %5.3f" % ageCI[0][2])
print("Info(age 31...40(4,0) is %5.3f" % ageCI[1][2])
print("Info(age >40 (3,2) is %5.3f" % ageCI[2][2])

print("Info(income low(1,3) is %5.3f" % incomeCI[0][2])
print("Info(income medium(2,4) is %5.3f" % incomeCI[1][2])
print("Info(income high(2,2) is %5.3f" % incomeCI[2][2])

print("Info(student No (4,3) is %5.3f" % stuCI[0][2])
print("Info(student Yes (1,6) is %5.3f" % stuCI[1][2])

print("Info(credit fair(2,6) is %5.3f" % creditCI[0][2])
print("Info(credit excellent(3,3) is %5.3f" % creditCI[1][2])
print("Info age (D) is %5.3f" % Info_ageD)
print("Info income (D) is %5.3f" % Info_incomeD)
print("Info student (D) is %5.3f" % Info_studentD)
print("Info credit rating (D) is %5.3f" % Info_creditD)
"""
print("\n***Gain results of all dataset***")
gainAge=InD-Info_ageD
print("Gain (age) is %5.3f"% gainAge)
gainIn=InD-Info_incomeD
print("Gain (Income) is %5.3f"% gainIn)
gainStu=InD-Info_studentD
print("Gain (Student) is %5.3f"% gainStu)
gainCre=InD-Info_creditD
print("Gain (Credit rating) is %5.3f"% gainCre)

#rule of root node

# Result_All=[gainAge,gainIn,gainStu,gainCre]
# max_gain=max(Result_All)
# pos=np.argmax(Result_All)
# print("max gain of attb is %5.3f" % max_gain,"position is",pos)

#วน loop แยก dataset ตาม attb age
X2L=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age <=30
X2M=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age 31-40
X2R=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
f1=open("D:/Grade3.2 CMU CPE/Data_Mining/DTProgram/buycomL2left.txt","w")
f2=open("D:/Grade3.2 CMU CPE/Data_Mining/DTProgram/buycomL2middle.txt","w")
f3=open("D:/Grade3.2 CMU CPE/Data_Mining/DTProgram/buycomL2right.txt","w")

for i in range(0,15):
    if ((X[i].count('<=30')==1)): 
        f1.write(str(X[i]))
    
    elif(X[i].count('31-40')==1):
        f2.write(str(X[i]))
        
    elif(X[i].count('>=40')==1):
        f3.write(str(X[i]))

# dataset of layer 2 of dtree generate
f1=open("D:/Grade3.2 CMU CPE/Data_Mining/DTProgram/buycomL2left.txt","r")
f2=open("D:/Grade3.2 CMU CPE/Data_Mining/DTProgram/buycomL2middle.txt","r")
f3=open("D:/Grade3.2 CMU CPE/Data_Mining/DTProgram/buycomL2right.txt","r")
X2L=f1.readlines()
X2M=f2.readlines()
X2R=f3.readlines()

C2L = len(X2L) # size (rows) of X2L
C2M = len(X2M) # size (rows) of X2M
C2R = len(X2R) # size (rows) of X2R

# recursive line 14 สำหรับการสร้าง tree ชั้นที่ 2 สำหรับ dataset age<=30
income=np.zeros(3)
incomeCI=[[0 for i in range(M)] for j in range(N)]
stu=np.zeros(2)
stuCI=[[0 for i in range(M)] for j in range(L)]
credit=np.zeros(2)
creditCI=[[0 for i in range(M)] for j in range(L)]
buy = np.zeros(2)

# วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
# data ที่ age <=30
for i in range(0,C2L):
    # income
    if (X2L[i].count('low')==1):
        income[0]+=1
        if ((X2L[i].count('low')==1)) and (X2L[i].count('No')==1):
            incomeCI[0][0]+=1
        else:
            incomeCI[0][1]+=1
    elif(X2L[i].count('medium')==1):
        income[1]+=1
        if ((X2L[i].count('medium')==1)) and (X2L[i].count('No')==1):
            incomeCI[1][0]+=1
        else:
            incomeCI[1][1]+=1
    elif(X2L[i].count('high')==1):
        income[2]+=1
        if ((X2L[i].count('high')==1)) and (X2L[i].count('No')==1):
            incomeCI[2][0]+=1
        else:
            incomeCI[2][1]+=1
    # student
    if (X2L[i].count('s_no')==1):
        stu[0]+=1
        if ((X2L[i].count('s_no')==1)) and (X2L[i].count('No')==1):
            stuCI[0][0]+=1
        else:
            stuCI[0][1]+=1
    elif(X2L[i].count('s_yes')==1):
        stu[1]+=1
        if ((X2L[i].count('s_yes')==1)) and (X2L[i].count('No')==1):
            stuCI[1][0]+=1
        else:
            stuCI[1][1]+=1
    # credit rating
    if (X2L[i].count('fair')==1):
        credit[0]+=1
        if ((X2L[i].count('fair')==1)) and (X2L[i].count('No')==1):
            creditCI[0][0]+=1
        else:
            creditCI[0][1]+=1
    elif(X2L[i].count('excellent')==1):
        credit[1]+=1
        if ((X2L[i].count('excellent')==1)) and (X2L[i].count('No')==1):
            creditCI[1][0]+=1
        else:
            creditCI[1][1]+=1
    
    if (X2L[i].count('No')==1):
        buy[0]+=1
    elif(X2L[i].count('Yes')==1):
        buy[1]+=1
        
# calculate information gain of dataset and attb
# info D,age,income,stu,credit
info = np.zeros(3)
InD=entropy(buy[1],buy[0])

incomeCI[0][2]=entropy(incomeCI[0][0],incomeCI[0][1])
incomeCI[1][2]=entropy(incomeCI[1][0],incomeCI[1][1])
incomeCI[2][2]=entropy(incomeCI[2][0],incomeCI[2][1])

stuCI[0][2]= entropy(stuCI[0][0],stuCI[0][1])
stuCI[1][2]= entropy(stuCI[1][0],stuCI[1][1])

creditCI[0][2]= entropy(creditCI[0][0],creditCI[0][1])
creditCI[1][2]= entropy(creditCI[1][0],creditCI[1][1])

# หาค่า gain แบบใช้ฟังก์ชัน
Info_incomeD = inforD(income,[incomeCI[0][2],incomeCI[1][2],incomeCI[2][2]])
Info_studentD = inforD(stu,[stuCI[0][2],stuCI[1][2]])
Info_creditD = inforD(credit,[creditCI[0][2],creditCI[1][2]])

# แสดงผลการทำงาน รอบ2 ฝั่งซ้าย
print("\n***Gain results of all dataset on left branch***")

gainIn_left=InD-Info_incomeD
gainStu_left=InD-Info_studentD
gainCre_left=InD-Info_creditD

print("Gain (Income) is %5.3f"% gainIn_left)
print("Gain (Student) is %5.3f"% gainStu_left)
print("Gain (Credit rating) is %5.3f"% gainCre_left)

# recursive line 14 สำหรับการสร้าง tree ชั้นที่ 2 สำหรับ dataset age>40
income=np.zeros(3)
incomeCI=[[0 for i in range(M)] for j in range(N)]
stu=np.zeros(2)
stuCI=[[0 for i in range(M)] for j in range(L)]
credit=np.zeros(2)
creditCI=[[0 for i in range(M)] for j in range(L)]
buy = np.zeros(2)

# วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
# data ที่ age > 40
for i in range(0,C2R):
    # income
    if (X2R[i].count('low')==1):
        income[0]+=1
        if ((X2R[i].count('low')==1)) and (X2R[i].count('No')==1):
            incomeCI[0][0]+=1
        else:
            incomeCI[0][1]+=1
    elif(X2R[i].count('medium')==1):
        income[1]+=1
        if ((X2R[i].count('medium')==1)) and (X2R[i].count('No')==1):
            incomeCI[1][0]+=1
        else:
            incomeCI[1][1]+=1
    elif(X2R[i].count('high')==1):
        income[2]+=1
        if ((X2R[i].count('high')==1)) and (X2R[i].count('No')==1):
            incomeCI[2][0]+=1
        else:
            incomeCI[2][1]+=1
    # student
    if (X2R[i].count('s_no')==1):
        stu[0]+=1
        if ((X2R[i].count('s_no')==1)) and (X2R[i].count('No')==1):
            stuCI[0][0]+=1
        else:
            stuCI[0][1]+=1
    elif(X2R[i].count('s_yes')==1):
        stu[1]+=1
        if ((X2R[i].count('s_yes')==1)) and (X2R[i].count('No')==1):
            stuCI[1][0]+=1
        else:
            stuCI[1][1]+=1
    # credit rating
    if (X2R[i].count('fair')==1):
        credit[0]+=1
        if ((X2R[i].count('fair')==1)) and (X2R[i].count('No')==1):
            creditCI[0][0]+=1
        else:
            creditCI[0][1]+=1
    elif(X2R[i].count('excellent')==1):
        credit[1]+=1
        if ((X2R[i].count('excellent')==1)) and (X2R[i].count('No')==1):
            creditCI[1][0]+=1
        else:
            creditCI[1][1]+=1
    
    if (X2R[i].count('No')==1):
        buy[0]+=1
    elif(X2R[i].count('Yes')==1):
        buy[1]+=1
        
# calculate information gain of dataset and attb
# info D,age,income,stu,credit
info = np.zeros(3)
InD=entropy(buy[1],buy[0])

incomeCI[0][2]=entropy(incomeCI[0][0],incomeCI[0][1])
incomeCI[1][2]=entropy(incomeCI[1][0],incomeCI[1][1])
incomeCI[2][2]=entropy(incomeCI[2][0],incomeCI[2][1])

stuCI[0][2]= entropy(stuCI[0][0],stuCI[0][1])
stuCI[1][2]= entropy(stuCI[1][0],stuCI[1][1])

creditCI[0][2]= entropy(creditCI[0][0],creditCI[0][1])
creditCI[1][2]= entropy(creditCI[1][0],creditCI[1][1])

# หาค่า gain แบบใช้ฟังก์ชัน
Info_incomeD = inforD(income,[incomeCI[0][2],incomeCI[1][2],incomeCI[2][2]])
Info_studentD = inforD(stu,[stuCI[0][2],stuCI[1][2]])
Info_creditD = inforD(credit,[creditCI[0][2],creditCI[1][2]])

# แสดงผลการทำงานรอบสอง ฝั่งขวา
print("\n***Gain results of all dataset on right branch***")
gainIn_right = InD - Info_incomeD
gainStu_right = InD - Info_studentD
gainCre_right = InD - Info_creditD
print("Gain (Income) is %5.3f"% gainIn)
print("Gain (Student) is %5.3f"% gainStu)
print("Gain (Credit rating) is %5.3f"% gainCre)

#สร้าง tree
#rule extraction
Result_All = [gainAge, gainIn, gainStu, gainCre]
attributes = ["Age", "Income", "Student", "Credit Rating"]
max_gain = max(Result_All)
pos = Result_All.index(max_gain)

Result_Left = [gainIn_left, gainStu_left, gainCre_left]
max_gain_left = max(Result_Left)
pos_left = Result_Left.index(max_gain_left)

Result_Right = [gainIn_right, gainStu_right, gainCre_right]
max_gain_right = max(Result_Right)
pos_right = Result_Right.index(max_gain_right)

print("\n***Nodes on tree***")
print(f"max gain of root node attb is {max_gain:.3f} position is {attributes[pos]}")
print(f"max gain of left node attb is {max_gain_left:.3f} position is {attributes[1:][pos_left]}")
print(f"max gain of right node attb is {max_gain_right:.3f} position is {attributes[1:][pos_right]}")

#model evaluation
def read_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]  # ข้ามแถวหัวข้อ
    
    # แยกแต่ละแถวและตัดช่องว่าง (strip) ที่ไม่จำเป็นออก พร้อมแยกข้อมูลโดยใช้ช่องว่าง
    data = [re.split(r'\s+', line.strip()) for line in lines]
    return data

# อ่านข้อมูลการฝึกและทดสอบ
train_data = read_data("D:/Grade3.2 CMU CPE/Data_Mining/DTProgram/buycom.txt")
test_data = read_data("D:/Grade3.2 CMU CPE/Data_Mining/DTProgram/test.txt")

train_labels = [
    "No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", 
    "Yes", "Yes", "Yes", "Yes", "Yes", "No"
]

test_labels = ["Yes", "No", "Yes", "No", "Yes"]

# ฟังก์ชันทำนาย
def predict(data):
    data = [item.strip() for item in data]

    # การทำนายตามเงื่อนไขที่กำหนดจากตัวอย่างข้อมูล
    if "age<=30" in data:
        if "student=s_no" in data:
            return "No"
        elif "student=s_yes" in data:
            return "Yes"
    elif "age31-40" in data:
        return "Yes"
    elif "age>=40" in data:
        if "credit_rating=excellent" in data:
            return "No"
        elif "credit_rating=fair" in data:
            return "Yes"
    return "Yes"

correct_train = sum(
    1 for i in range(len(train_data))
    if predict(train_data[i]) == train_labels[i]
)
train_accuracy = (correct_train / len(train_data)) * 100

correct_test = sum(
    1 for i in range(len(test_data))
    if predict(test_data[i]) == test_labels[i]
)
test_accuracy = (correct_test / len(test_data)) * 100

print("\n***Model evaluation***")
print(f"training accuracy is {train_accuracy:.2f} %")
print(f"testing accuracy is {test_accuracy:.2f} %")
