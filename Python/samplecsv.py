import csv
data=[]
def getrecord(x):
	for k in range(len(data)):
		if int(data[k][0])==x:
			return([k,data[k]])
	print("Invalid admission number")
	return(-2)
def newstud(n):
		for i in range(n):
			L=[]
			L.append(int(input("Enter admission number: ")))
			L.append(input("Enter Name: "))
			L.append(int(input("Enter Class: " )))
			L.append(input("Enter Section: " ))
			L.append(int(input("Enter roll number: " )))
			L.append(int(input("Enter percentages: ")))
			data.append(L)
try:
	file=open("StudentDatabase.csv","r")
	r=csv.reader(file)
	for j in r:
		if j!=[]:
			data.append(j)
	file.close()
except:
	n=int(input("Enter number of students"))
	
	newstud(n)
while True:
	print("Enter 1 to view data ")
	print("Enter 2 for adding more student data")
	print("Enter 3 for  updating particular student data")
	print("Enter 4 for enquiry ")
	print("Enter 5  if no operation ")
	print()
	print()
	flag1=int(input("Enter choice"))
	print()
	def show():
		print("Admission No.,Name,Class,Section,roll number,Percentage ")
		print()
		for i in data:
			for j in i:
				print(j,end="  ")
			print()
		print()
	if flag1==1:
	
		show()
	if flag1==5:
		file=open("StudentDatabase.csv","w")
		w=csv.writer(file)
		w.writerows(data)
		file.close()
		break
	if flag1==2:
		n=int(input("Enter number of students data to be added"))
		newstud(n)
	if flag1==3:
		print("Press 1 to view Students data and then update")
		print("Press 2 to directly update data")
		flag2=int(input("Enter Choice"))
		if flag2==1:
			show()
		temp=int(input("Enter admission number of student whose data to be updated"))
		temp=getrecord(temp)
		if temp!= -2:
			print(temp[1])
			print()
			print()
			while True:
				print("Press 1 to update Class")
				print("Press 2 to update Section")
				print("Press 3 to update Roll number ")
				print("Press 4 to update percentage ")
				print("Press 5 if nothing more to update")
				print()
				flag2=int(input("Enter Choice"))
				if flag2==5:
					break
				if flag2==2:
					y=input("Enter Section")
					temp[1][3]=y
				if flag2==3:
					y=int(input("Enter Roll number"))
					temp[1][4]=y
				if flag2==1:
					y=int(input("Enter Class"))
					temp[1][2]=y
				if flag2==4:
					y=int(input("Enter Percentage"))
					temp[1][5]=y
			data[temp[0]]=temp[1]
	if flag1==4:
		temp=int(input("Enter the admission number of the student "))
		temp=getrecord(temp)
		pmer=temp[1]
		print()
		print("____________")
		print("Name: ",pmer[1])
		print("Admission Number: ",pmer[0])
		print("Class: ",int(pmer[2]))
		print("Section: ",pmer[3])
		print("Roll number: ",int(pmer[4]))
		print("Percentage: ",int(pmer[5]))
    			
print()
print(" Database Successfully Saved and Closed")