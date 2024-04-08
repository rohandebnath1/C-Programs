#File Handling

def Record_di():
    while c == ("Yy"):
        f = open("E:\Python Files\direct.txt","w")
        f_name = input("Enter the first name: ")
        l_name = input("Enter the last name: ")
        reg_no = int(input("Enter the registration numeber: "))
        doj = input("Enter Date of joining: ")
        rec = [f_name,l_name,reg_no,doj]
        f.write(rec)
        c = input("Do you want to continue (y/n): ")
Record_di()
        
    
    
    
