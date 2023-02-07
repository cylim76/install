
#!/usr/bin/python3

# 备份的 x-ui 数据库,批量修改证书地址

import sqlite3
import datetime
import os
import json

current_time = datetime.datetime.now()
print(f"{current_time} :start to update cert file path ")
#01 5 * * * cd /root/myroot/ && python3 x-ui_sub_mgr.py

if os.path.isdir('/etc/x-ui/'):
    dbfile = '/etc/x-ui/x-ui.db'
else: dbfile = './x-ui.db'     #for local test




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

def get_streamsettings_json(db,id):
    # another way to get inbounds setting and link
    sql = 'select id,stream_settings  from inbounds where id ={};'.format(id)
    conn = sqlite3.connect(db)
    c = conn.cursor()
    slqresult = c.execute(sql).fetchall()
    inboundinfo = list(slqresult[0])
    conn.close()


    id =  inboundinfo[0]
    
    
    stream_settings = inboundinfo[1]
    stream_settings_json = json.loads(stream_settings)

    network = stream_settings_json["network"] # network_type
    serverName = stream_settings_json["tlsSettings"]["serverName"]   ######


    return id, stream_settings_json

def db_update_stream_settings(db,id,stream_settings):

    sql = 'Update inbounds set  stream_settings = ? where id =?;'
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(sql,(str(stream_settings), id))
    conn.commit()
    conn.close()

def db_settings_inquiry(db): 

    sql = f"select *  from settings where key = 'webKeyFile';"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    slqresult = c.execute(sql).fetchall()
    # conn.close()
    inboundinfo = list(slqresult[0])

    id = inboundinfo[0]
    key = inboundinfo[1]
    value = inboundinfo[2]

    return id, key, value

def xui_certfile_inquiry(dbfile):
    id, key, value = db_settings_inquiry(dbfile)
    print(id, key, value)

def xui_certfile_update(dbfile):

    sql = 'Update settings set  value = ? where key =?;'
    new_webKeyFile = f'/root/cert/{new_servername}.key'
    conn = sqlite3.connect(dbfile)
    # conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(sql,(str(new_webKeyFile), 'webKeyFile'))
    conn.commit()
    conn.close()



def init_inbounds_cert_path():
    ids = make_id_list(dbfile)
    for id in ids:
        id, stream_settings_json = get_streamsettings_json(dbfile,id)
        servername = stream_settings_json["tlsSettings"]["serverName"]
        keyfilepath = stream_settings_json["tlsSettings"]["certificates"][0]["keyFile"]
        print(servername, keyfilepath)

        stream_settings_json["tlsSettings"]["serverName"] = new_servername
        stream_settings_json["tlsSettings"]["certificates"][0]["keyFile"] = f'/root/cert/{new_servername}.key'
        # print(stream_settings_json)
        new_stream_settings_json = json.dumps(stream_settings_json)
        db_update_stream_settings(dbfile,id,new_stream_settings_json)
        print(new_stream_settings_json)





new_servername = input('Please input current server domain name: ') # 输入新服务器的域名(需要提前申请号证书)


init_inbounds_cert_path()
xui_certfile_inquiry(dbfile)
xui_certfile_update(dbfile)
xui_certfile_inquiry(dbfile)

 
        

