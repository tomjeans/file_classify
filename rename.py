# import os
# path = 'C://Users//IT Power//Desktop//test//'
# name_test = os.listdir(path)
# for name in name_test:
#     print(name)
#     newname = 'DDD' + name
#     print(newname)
#     os.rename(path+name,path+newname)
# #rename code
import os
def first_step(path):
    #path = 'D://ai_lable//00000001_7 -label//00000007_xp_label - 副本//head circumference//'
    name_test = os.listdir(path)
    for name in name_test:
        position = name.rfind('Inked',0,5)
        newname=name[position+5:]
        print(newname)
        os.rename(path+name,path+newname)

def second_step(path):
    #path = 'D://ai_lable//00000001_7 -label//00000007_xp_label - 副本//head circumference//'
    name_test = os.listdir(path)
    for name in name_test:
        position = name.rfind('IM',0,5)
        newname=name[:position+7]+'.jpg'
        print(newname)
        os.rename(path+name,path+newname)
path_femur = 'D://ai_lable//00000001_7 -label//修正//修正00000002_lz//修正00000002_lz//femur//'
path_head_circumference = 'D://ai_lable//00000001_7 -label//修正//修正00000002_lz//修正00000002_lz//head circumference//'
path_abdominial_circumference = 'D://ai_lable//00000001_7 -label//修正//修正00000002_lz//修正00000002_lz//abdominal circumference//'
def process(path_1):
    first_step(path_1)
    second_step(path_1)
process(path_femur)
process(path_head_circumference)
process(path_abdominial_circumference)