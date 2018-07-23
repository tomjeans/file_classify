import os 
import shutil
log_out_put = open('log_path.txt','a')
fl = 100000
ac = 200000
count_ac=1
count_hc=1
count_fl=1
path='G:\\ai_la\\'
path_a = os.listdir(path)
#print(path_a)
for path_b in path_a:
    
    path_c=os.listdir(path+path_b)
    #print(path_c)
    #count_3 +=1
    count_5=0
    for  path_d in path_c:
        path_file=path+path_b+'\\'+path_d
        path_e=os.listdir(path+path_b+'\\'+path_d)
        #print(path_e)
        #count_2 +=1
        #count_5 +=1
        count_4=0
    
        for files in path_e:
            
            #print(path_f)
            tmp_path = os.path.join(path_file,files)
            print(tmp_path)
            count_4 += 1
            if tmp_path[-15] == 'c':
                if tmp_path[-16] == 'h':
                    #shutil.copy(tmp_path,'G:\\result\\hc\\str('%06d' %count_hc)'+'.jpg')
                    log_out_put.write(tmp_path+'---------> '+'G:\\result\\hc\\'+str('%06d' %count_hc)+'.jpg')
                    log_out_put.write('\n')
                    path_d_hc = 'G:\\result\\hc\\'+str('%06d' %count_hc)+'.jpg'
                    shutil.copy(tmp_path,path_d_hc)
                    count_hc +=1
                else:
                    #shutil.copy(tmp_path,'G:\\result\\ac\\str(int('%06d' %count_ac)+ac)'+'.jpg')
                    log_out_put.write(tmp_path+'---------> '+'G:\\result\\ac\\'+str(int('%06d' %count_ac)+ac)+'.jpg')
                    log_out_put.write('\n')
                    path_d_ac = 'G:\\result\\ac\\'+str('%06d' %count_ac)+'.jpg'
                    shutil.copy(tmp_path,path_d_ac)
                    count_ac +=1
            elif tmp_path[-15] == 'l':
                #shutil.copy(tmp_path,'G:\\result\\fl\\str(int('%06d' %count_fl)+fl)'+'.jpg')
                log_out_put.write(tmp_path+'---------> '+'G:\\result\\fl\\'+str(int('%06d' %count_fl)+fl)+'.jpg')
                log_out_put.write('\n')
                path_d_fl = 'G:\\result\\fl\\'+str('%06d' %count_fl)+'.jpg'
                shutil.copy(tmp_path,path_d_fl)
                count_fl += 1
            else: 
                print('this is an cerebellum picture!')
log_out_put.close()
            # if  == 'ac': 
            #     shutil.copy(tmp_path,)