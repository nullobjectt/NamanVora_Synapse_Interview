input_into_list=[]
str1=input("Enter runes:")
for i in range(0,len(str1)):
    input_into_list.append(str1[i])
count_l=0
count_s=0
count_o=0
count_m=0
count_u=0
l_index_list=[]
s_index_list=[]
m_index_list=[]
o_index_list=[]
u_index_list=[]
i=0
while i<len(input_into_list):
    if input_into_list[i]=="l" or input_into_list[i]=="L":
        count_l+=1
        l_index_list.append(i)
        i+=1
    elif input_into_list[i]=="s" or input_into_list[i]=="S":
        count_s+=1
        s_index_list.append(i)
        i+=1
    elif input_into_list[i]=="m" or input_into_list[i]=="M":
        count_m+=1
        m_index_list.append(i)
        i+=1
    elif input_into_list[i]=="o" or input_into_list[i]=="O":
        count_o+=1
        o_index_list.append(i)
        i+=1
    elif input_into_list[i]=="u" or input_into_list[i]=="U":
        count_u+=1
        u_index_list.append(i)
        i+=1
    else:
        i+=1

if count_l==0 or count_m==0 or count_o==0 or count_s==0 or count_u==0:
    print("-1")
else:
    p=[l_index_list[0],o_index_list[0],s_index_list[0],m_index_list[0],u_index_list[0]]
    m=max(p)
    print("LUMOS spell created!")
    print(f"Earliest step to create LUMOS is {m+1}")