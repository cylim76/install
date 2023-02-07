
#!/usr/bin/python3
# 这个脚本配合订阅管理脚本, 定时自动更换端口号
# crontab -e 添加一行:  55 2 * * * cd <脚本所在路径> && python3 x-ui_port_changer.py


import sqlite3
import datetime
import os
import random


current_time = datetime.datetime.now()
dayevenodd = current_time.day % 2
print(f"port changer is running {current_time}")


if os.path.isdir('/etc/x-ui/'):
    dbfile = '/etc/x-ui/x-ui.db'
else: dbfile = './x-ui.db'    #for local test

datamax = 1000  #(MB)
step = 1 # the step of port number daily changed for

def get_remark_date():

    current_time = datetime.datetime.now()
    remark_date = f'_{current_time.day}_{current_time.hour}:{current_time.minute}' # real time

    hrand = random.randint(1,6)
    mrand = random.randint(1,60)
    remark_date = f'_{current_time.day}_{hrand}:{mrand}' # make fake time
    return remark_date

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

    sql = f'select id,port,up,down,total,remark,tag from inbounds where id ={id};'
    conn = sqlite3.connect(db)
    c = conn.cursor()
    slqresult = c.execute(sql).fetchall()
    # conn.close()
    inboundinfo = list(slqresult[0])

    id = inboundinfo[0]
    port = inboundinfo[1]
    up_data = int(inboundinfo[2] / 1000000)
    down_data = int(inboundinfo[3] / 1000000)
    datasum = up_data + down_data
    remark = inboundinfo[5]
    tag = inboundinfo[6]
    # print(f' id: {id},  port : {port}, data: {datasum}, remark : {remark}, tag : {tag}')
    return id, port, datasum,remark

def db_update_portadd(db,id,port,remark):
    port = int(port) + step
    tag = 'inbound-' + str(port)
    sql = 'Update inbounds set port = ?, tag = ?, remark = ?, up = 0, down = 0 where id =?;'
    remark_date = get_remark_date()
    remark = remark.split('_')[0] + remark_date #
    conn = sqlite3.connect(db)
    # conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(sql,(port, tag, remark, id))
    conn.commit()
    conn.close()
    # print(f'id: {id} 的端口号变更！ new port: {port}, new tag: {tag}')


# # 执行凌晨4点多运行,流量大于datamax的或按单双号更改端口
def care_port():
    ids = make_id_list(dbfile)
    for id in ids :
        id,port, datasum,remark = db_inquiry(dbfile,id) 
        if '_' not in remark: remark = remark + '_0'
        if id % 2 == dayevenodd : 
            if remark.split('_')[1] != str(current_time.day) :
                db_update_portadd(dbfile,id,port,remark)
                id,mewport, newdatasum,newremark = db_inquiry(dbfile,id)
                print('even odd : ',id, port, datasum,remark, 'changed to:', mewport, newdatasum,newremark)
            else:
                id,port, datasum,remark = db_inquiry(dbfile,id)
                print('unchanged  ', id,port,datasum,remark)                

        elif  datasum >= datamax :#and remark.split('_')[1] != str(current_time.day) : 
            db_update_portadd(dbfile,id,port,remark) 
            id, datasum,port,remark = db_inquiry(dbfile,id)
            id,mewport, newdatasum,newremark = db_inquiry(dbfile,id)
            print('maxdata  : ',id, port, datasum,remark, 'changed to:', mewport, newdatasum,newremark)

        else: 
            id,mewport, newdatasum,newremark = db_inquiry(dbfile,id)
            print('unchanged  ', id,mewport,newdatasum,newremark)

    if os.path.isdir('/etc/x-ui/'):
        print('x-ui restarting ')
        os.system('x-ui restart') 

# if current_time.hour == 2:
#     care_port()

care_port()
