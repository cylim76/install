
#!/usr/bin/python3

import sqlite3
import datetime
import os

current_time = datetime.datetime.now()
print(f"port changer was run {current_time}")
#01 5 * * * cd /root/myroot/ && python3 x-ui_sub_mgr.py


# dbfile = '/etc/x-ui/x-ui.db'
dbfile = './x-ui.db'


def make_id_list(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    # conn.row_factory = lambda cursor, row:[row[0], row[5]] # 特定的列加入到列表
    c.row_factory = lambda cursor, row:row[0]   # 特定的列加入到列表
    sql = 'select * from inbounds ;'
    ids_list = c.execute(sql).fetchall()
    conn.close()
    return ids_list


def db_inquiry(db,id,datasum): 

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
    sum = up_data + down_data
    remark = inboundinfo[5]
    tag = inboundinfo[6]
    # print(f' id: {id},  port : {port}, data: {sum}, remark : {remark}, tag : {tag}')


    if sum >= datasum :
        port = int(port) + 1
        tag = 'inbound-' + str(port)
        sql = 'Update inbounds set port = ?, tag = ?, up = 0, down = 0 where id =?;'
        
        conn = sqlite3.connect(db)
        # conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(sql,(port, tag, id))
        conn.commit()
        conn.close()
        print(f'id: {id} 的端口号变更！ new port: {port}, remark : {remark},   new tag: {tag}')
    else:
        print(f' id: {id},  port : {port}, data: {sum},  流量小于{datasum} 不做处理')
    return 

 

if current_time.hour == 4 and current_time.minute <30 : # 凌晨4点多运行,流量大于3000MB的更改端口号
    ids = make_id_list(dbfile)
    for id in ids:
        db_inquiry(dbfile,id,3000)  


os.system('x-ui restart') # this line only works on linux server that running x-ui

