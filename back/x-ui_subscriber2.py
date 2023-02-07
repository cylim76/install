
#!/usr/bin/python3

import sqlite3
import base64
# import shutil
import paramiko
from scp import SCPClient
import os
import time





servers = [
# 服务器信息 
    ["xui.github.com","root" ,"88888888.", "sega"], #服务器域名, 服务器用户名,服务器密码,服务器昵称
    ["xui.google.com","root" ,"88888888.", "kinder"]    
    ]


subscribtion =[
# 订阅节点信息， 文件名，节点1，节点2。。。
['00-00-allmonitor.TXT', 'sega1', 'sega2', 'kinder1', 'kinder2'],
['01-02-hydroxides.TXT', 'sega1', 'sega2', 'kinder1', 'kinder2'],
['03-03-eshareagen.TXT', 'sega3', 'sega4', 'kinder3', 'kinder4'],
['04-09-us-router.TXT', 'sega5', 'sega6', 'sega7', 'sega8', 'sega9', 'kinder5', 'kinder6', 'kinder7', 'kinder8', 'kinder9'],
['10-11-molecular.TXT', 'sega10', 'sega11', 'kinder10', 'kinder11'],
['12-13-patriotic.TXT', 'sega12', 'sega13', 'kinder12', 'kinder13'],
['14-15-equation.TXT', 'sega14', 'sega15', 'kinder14', 'kinder15'],
['16-17-kovalence.TXT', 'sega16', 'sega17', 'kinder16', 'kinder17'],
['18-18-kongdd.TXT', 'sega18'                                     ],
['19-20-crisis.TXT', 'sega19', 'sega20', 'kinder19', 'kinder20'],
['21-22-park66.TXT', 'sega18', 'sega21', 'sega22', 'sega23', 'sega24', 'kinder21', 'kinder22']

]

dbfilepath = './temp/x-ui/x-ui_db/'
linkfilepath = './temp/x-ui/x-ui_links/'
temphtmlpath = './station/sublinks/'


def createSSHClient(server, port, user, password):
    # 建立 ssh链接的函数
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


def download_xui_db_file():
    # 下载 x-ui 的数据库文件
    for server in servers:
        if not os.path.isdir(dbfilepath + server[0]):
            os.makedirs(dbfilepath + server[0])
        dbfile = dbfilepath + server[0] + "/x-ui.db"

        ssh = createSSHClient(server[0], 22, server[1], server[2])
        scp = SCPClient(ssh.get_transport())  
        scp.get('/etc/x-ui/x-ui.db',dbfile)
        print(f"成功从{server[0]}下载数据库文件保存到: {dbfile}" )
        ssh.close()
    return 


def make_id_list(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    # conn.row_factory = lambda cursor, row:[row[0], row[5]] # 特定的列加入到列表
    c.row_factory = lambda cursor, row:row[0]   # 特定的列加入到列表
    sql = 'select * from inbounds ;'
    ids_list = c.execute(sql).fetchall()
    conn.close()
    return ids_list


def get_inbound_link(db,id):
    
    sql = 'select id,user_id,up,down,total,remark,enable,expiry_time,autoreset,ip_alert,listen,port\
        ,protocol,settings,stream_settings,tag,sniffing,ip_limit from inbounds where id ={};'.format(id)
    # db_inquiry_for_test(sql)
    # conn.row_factory = sqlite3.Row
    conn = sqlite3.connect(db)
    c = conn.cursor()
    slqresult = c.execute(sql).fetchall()
    inboundinfo = list(slqresult[0])
    conn.close()
    # for i, info in enumerate(inboundinfo):
    #     print(i, info)
    # print(inboundinfo)
    protocol = inboundinfo[12]
    v = 2
    ps = inboundinfo[5]
   
    # print(inboundinfo[14].split('"serverName": '))
    add = inboundinfo[14].split('"serverName": "')[1].split('"')[0]
    if add =='': 
        print(f'{id}# id的入口: serverName 信息空缺,生成链接失败!! ')
        return

    port = inboundinfo[11]
    userid = inboundinfo[13].split('"id": "')[1].split('"')[0]

    if protocol == 'vmess':
        alterid = inboundinfo[13].split('"alterId": ')[1].split(' ')[0]
    else : alterid = 0

    network = inboundinfo[14].split('"network": "')[-1].split('"')[0]
    type1 = 'None'
    host =''

    if network == 'ws':
        path = inboundinfo[14].split('"path": "')[1].split('"')[0]
    else: path = '/' 
    tls =  inboundinfo[14].split('"security": "')[1].split('"')[0]

    sniffing = ""
    alpn =  inboundinfo[14].split('"alpn": ')[1].split(']')[0].replace('\n','').replace('[','').replace(' ','').replace('"','')
    


    if protocol == 'vmess'and network =='ws':
        link_text = '{'+ f'"v": "2",  "ps": "{ps}",  "add": "{add}",  "port": {port},  "id": "{userid}", \
                "aid": {alterid},  "net": "{network}",  "type": "none",  "host": "",  "path": "{path}",  "tls": "{tls}"' +'}'
        encoded_link_text = link_text.encode("utf-8")
        sublink = 'vmess://' + str(base64.b64encode(encoded_link_text)).split("'")[1]
        # sublink = str(base64.b64encode(encoded_link_text)).split("'")[1]
        # print(sublink)
    elif protocol == 'vmess'and network =='tcp':
        link_text = '{'+ f'"v": "2",  "ps": "{ps}",  "add": "{add}",  "port": {port},  "id": "{userid}", \
                "aid": {alterid},  "net": "{network}",  "type": "none",  "host": "",  "path": "/",  "tls": "{tls}"' +'}'
        encoded_link_text = link_text.encode("utf-8")
        sublink = 'vmess://' + str(base64.b64encode(encoded_link_text)).split("'")[1]
        # sublink = str(base64.b64encode(encoded_link_text)).split("'")[1]
        # print(sublink)
        
    elif protocol == 'vless' and network =='ws':
        sublink = 'vless://' + f'{userid}@{add}:{port}?type={network}&security={tls}&path={path}&sni={add}&flow=#{ps}'
    elif protocol == 'vless' and network =='tcp':
        sublink = 'vless://' + f'{userid}@{add}:{port}?type={network}&security={tls}&sni={add}&flow=#{ps}'

    # print("type: ",protocol, v,ps,add, port,alterid,network,type1,host,path,tls,sniffing,alpn ) #,userid
    # print(sublink)

    return sublink


def db_inquiry(db,sql): 
    # 测试用的
    # sql = 'select * from inbounds where id ={};'.format(id) # inbound's ID
    # sql = 'select id,user_id,up,down,total,remark,enable,expiry_time,autoreset,ip_alert,listen,port\
    #     ,protocol,settings,stream_settings,tag,sniffing,ip_limit from inbounds where id ={};'.format(id)
    # conn.row_factory = sqlite3.Row
    conn = sqlite3.connect(db)
    c = conn.cursor()
    slqresult = c.execute(sql).fetchall()
    inboundinfo = list(slqresult[0])
    for i, info in enumerate(inboundinfo):
        print(i, info)


def save_inbounds_all_in_onefile():
    for server in servers:
        db = dbfilepath + server[0] + "/x-ui.db"
        if not os.path.isdir(linkfilepath + server[0]):
            os.makedirs(linkfilepath + server[0])
        linkfile = linkfilepath + server[0] + f"/{server[0]}.sh"
        ids = make_id_list(db)
        sublinklist = []
        for id in ids:
            sublinklist.append(get_inbound_link(db,id))
        with open(linkfile,'w') as f:
            for link in sublinklist:
                f.write(link + '\n')
            print(f'{server[0]}的节点链接成功保存到:  {linkfile}')
            # os.remove(server[3])

def save_inbounds_to_eachfile():
    linkdict = {}
    for server in servers:
        db = dbfilepath + server[0] + "/x-ui.db"
        if not os.path.isdir(linkfilepath + server[0]):
            os.makedirs(linkfilepath + server[0])
        ids = make_id_list(db)
        for id in ids:
            link = get_inbound_link(db,id)
            linkfile = linkfilepath + server[0] +"/" + server[3] + str(id)
            dictkey = server[3] + str(id)
            with open(linkfile,'w') as f:
                f.write(link + '\n')

            linkdict[dictkey]= link
            # print(f'{server[0]}的{id}号节点链接成功保存到 {linkfile}')
            # os.remove(server[3])
    return linkdict


def make_sub_file(subscribtion,linkdict):
    
    if not os.path.isdir(temphtmlpath ):
        os.makedirs(temphtmlpath )

    #首个监控用的全节点集合
    for sub in subscribtion[0:1]:
        tempsubstr = ''
        # inboun_all = [x for x in linkdict.keys()]
        for value in linkdict.values():
            tempsubstr = tempsubstr + value + '\n'
        encoded_tempsubstr = str(base64.b64encode(tempsubstr.encode("utf-8"))).split("'")[1]
        with open(temphtmlpath + sub[0],'w') as f:
                f.write(encoded_tempsubstr)


    # 正常订阅节点
    for sub in subscribtion[1:]:
        tempsubstr = ''
        
        for inboun in sub[1:]:
            tempsubstr = tempsubstr + linkdict.get(inboun) + '\n'
        
        encoded_tempsubstr = str(base64.b64encode(tempsubstr.encode("utf-8"))).split("'")[1]
        with open(temphtmlpath + sub[0],'w') as f:
                f.write(encoded_tempsubstr)

        # print(encoded_tempsubstr)
        pass


#执行1 保存成一个文件
# download_xui_db_file()  #下载服务器数据库文件到本地
# save_inbounds_all_in_onefile() #从数据库读取节点链接地址保存到文件

#执行2： 各id 分别保存
# download_xui_db_file()  #下载服务器数据库文件到本地
# save_inbounds_to_eachfile()

#执行3： 生成订阅源文件
download_xui_db_file()  #下载服务器数据库文件到本地
linkdict = save_inbounds_to_eachfile()
make_sub_file(subscribtion,linkdict)
