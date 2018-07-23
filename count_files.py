# #coding:utf-8
# import os
# import shutil
# count = 0
# def rename(count=0): 
#     path = 'C:\\Users\\IT Power\\Desktop\\test\\'
#     fl = 100000
#     ac = 200000
#     #count_number = 6
#     name_1 = os.listdir(path)
#     for name_1 in name_1:
#         count+=1
#         name_left = 'img_'
#         name_middle_number = int('%06d' %count)+ac
        
#         name_now = name_left+str(name_middle_number)+'.txt'
#         os.rename(path+name_1,path+name_now)
#     return counts 
#         #直接用格式说明符不用zfill操作字符串
# def divided():
#     count = 0
#     path_origin_hc = 'C:\\Users\\IT Power\\Desktop\\test\\'
#     path_origin_fl = 'C:\\Users\\IT Power\\Desktop\\test\\'
#     path_origin_ac = 'C:\\Users\\IT Power\\Desktop\\test\\'
#     path_origin_cerebellum = 'C:\\Users\\IT Power\\Desktop\\test\\'
#     path_all=os.listdir(path_origin)
#     for files in path_all:
#         tmp_path = os.path.join(path,files)
#         shutil.copy(tmp_path,d_path_1)
#         count +=1

# divided()
# count_e=rename()

    
#         # log_1=open('yourpath','a')
#         # log_1.write(tmp_path)
#         # log_1.write('----->')
#         # log_1.write('destion path')
import os
import shutil
log_count=open('log_count.txt','a')
count_1 = 0
count_2 = 0
count_3 = 0
count_in_ac = 0
count_in_fl = 0
count_in_hc = 0
count_in_cerebellum =0 
path='G:\\ai_la\\'
path_a = os.listdir(path)
#print(path_a)
for path_b in path_a:
    
    path_c=os.listdir(path+path_b)
    #print(path_c)
    count_3 +=1
    count_5=0
    for  path_d in path_c:
        
        path_e=os.listdir(path+path_b+'\\'+path_d)
        #print(path_e)
        count_2 +=1
        count_5 +=1
        count_4=0
    
        for path_f in path_e:
            
            #print(path_f)
            count_1 +=1
            count_4 +=1
        if path_d =='ac':
            count_in_ac +=count_4
        elif path_d =='fl':
            count_in_fl +=count_4
        elif path_d == 'hc':
            count_in_hc +=count_4
        else:
            count_in_cerebellum +=count_4 
        print('count_picture',path_b,path_d,count_4)
        log_count.write(path_b+' '+path_d+' '+str(count_4))
        log_count.write('\n')
print('count_ac',count_in_ac)
print('count_fl',count_in_fl)
print('count_hc',count_in_hc)
print('count_cerebellum',count_in_cerebellum)
#把path改成你需要统计的路径
log_count.write('count_ac'+' ')
log_count.write(str(count_in_ac))
log_count.write('\n')
log_count.write('count_fl'+' ')
log_count.write(str(count_in_fl))
log_count.write('\n')
log_count.write('count_hc'+' ')
log_count.write(str(count_in_hc))
log_count.write('\n')
log_count.write('count_cerebellum'+' ')
log_count.write(str(count_in_cerebellum))
log_count.close()

