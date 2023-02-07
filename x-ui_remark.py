
#!/usr/bin/python3
# 初始化remark,   remark 日期设置为0
#
import sqlite3
import datetime
import os

current_time = datetime.datetime.now()
print(f"port changer is running {current_time}")
#01 5 * * * cd /root/myroot/ && python3 x-ui_sub_mgr.py

if os.path.isdir('/etc/x-ui/'):
    dbfile = '/etc/x-ui/x-ui.db'
else: dbfile = './x-ui.db'    #for local test

srvtag = 'us'

remark_base = {
1:'ppmm',2:'smart',3:'esha',4:'taRT',5:'taRT',
6:'hxRT',7:'hxRT',8:'hlRT',9:'hlRT',10:'m서울',
11:'m제주',12:'p미나리',13:'p개나리',14:'seren',15:'seren',
16:'wagon',17:'wagon',18:'kongdd',19:'kris',20:'kris',
21:'park',22:'park',23:'park',24:'park'
}

def make_id_list(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    # conn.row_factory = lambda cursor, row:[row[0], row[5]] # 特定的列加入到列表
    c.row_factory = lambda cursor, row:row[0]   # 特定的列加入到列表
    sql = 'select * from inbounds ;'
    ids_list = c.execute(sql).fetchall()
    conn.close()
    return ids_list


def db_inquiry(db,id): 

    sql = f'select id, remark  from inbounds where id ={id};'
    conn = sqlite3.connect(db)
    c = conn.cursor()
    slqresult = c.execute(sql).fetchall()
    # conn.close()
    inboundinfo = list(slqresult[0])

    id = inboundinfo[0]
    remark = inboundinfo[1]

    return id, remark

def db_update_remark(db,id,remark):

    sql = 'Update inbounds set  remark = ? where id =?;'
    conn = sqlite3.connect(db)
    # conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(sql,(remark, id))
    conn.commit()
    conn.close()
    # print(f'id: {id} 的端口号变更！ new port: {port}, new tag: {tag}')


# # 执行凌晨4点多运行,流量大于datamax的或按单双号更改端口



ids = make_id_list(dbfile)
for id in ids:
    id, remark = db_inquiry(dbfile,id)
    # print('当前信息:', id, remark)
    remark2 = '_0'
    if '_' in remark:


        ###############################################################
        remark2 ='_' + remark.split('_', maxsplit = 1)[-1] # 保留原日期
        remark2 ='_' + '0' # for test 日期插入0 
        ###############################################################


    newremark = str(id) + srvtag + remark_base.get(id) + remark2
    db_update_remark(dbfile,id,newremark)
    id, remark = db_inquiry(dbfile,id)
    print(id, remark)
        

