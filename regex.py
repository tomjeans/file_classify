#coding:utf-8
# import re
# name = ['IMG_011_1.jpg','IMG_01871_2.jpg','IMG_01176565_3.jpg','IMG_675765_1.jpg']
# name_a={}
# for na in name:
#     m=re.findall(r'(_\d+)\.',na)   
#     for m_1 in m:
#         for m_2 in m_1:
#             name_a[m_2]=na

# print(name_a)


# import re
# m_1=0
# m_2=0
# m_3=0
# f = ['img_32fds3_1.jpg','img_32rdf4_2.jpg','img_243fdf423_3.jpg','img_243332_3.jpg']
# for i in f:
#     m = re.search(r'(_\d+(?=\.jpg))',i)
#     print(m.group())
#     # print(type(m.group()))
#     if m.group()=='_1':
#         # print('1')
#         m_1 +=1
#     elif m.group()=='_2':
#         # print('2')
#         m_2 +=1
#     else:
#         # print('3')
#         m_3 +=1
# print('_1has:',m_1)
# print('_2has:',m_2)
# print('_3has:',m_3)

# import os
# def mkdir(path):
    
#     path=path.strip()
#     path=path.rstrip("\\")
#     isexists=os.path.exists(path)
#     if not isexists:
#         os.makedirs(path)
#         print('path bulided success!')
#     else:
#         print('path has existed!')
# path_1="g:\\ai_label_new\\p_1\\"
# path_2="g:\\ai_label_new\\p_2\\"
# path_3="g:\\ai_label_new\\p_3\\"
# mkdir(path_1)
# mkdir(path_2)
# mkdir(path_3)



import os
import shutil 
import re

def traverse(f,d_path):
    count_1=0
    count_2=0
    count_3=0
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f,f1)
        # if os.path.isfile(path):
        m = re.search(r'(_\d+(?=\.jpg))',tmp_path)
        if m.group()=='_1':
            print('%s'%tmp_path)
            shutil.copy(tmp_path,d_path_1)
            print('copy success!')
            count_1 +=1
        elif m.group()=='_2':
            print('%s'%tmp_path)
            shutil.copy(tmp_path,d_path_2)
            print('copy success!')
            count_2 +=1
        else:
            print('%s'%tmp_path)
            shutil.copy(tmp_path,d_path_3)
            print('copy success!')
            count_3 +=1
    
    print('count_1:',count_1)
    print('count_2:',count_2)
    print('count_3:',count_3)            
path = 'D://ai_lable//00000011_3_8-13//00000012_HPH - 副本'
#your origin path
d_path_1 = 'D://ai_lable//00000011_3_8-13//00000012_HPH_label//abdominal circumference'
d_path_2 = 'D://ai_lable//00000011_3_8-13//00000012_HPH_label//femur'
d_path_3 = 'D://ai_lable//00000011_3_8-13//00000012_HPH_label//head circumference'
#destion 
traverse(path,d_path_1)
traverse(path,d_path_2)
traverse(path,d_path_3)