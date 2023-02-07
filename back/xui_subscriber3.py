
#!/usr/bin/python3

import sqlite3
import base64
# import shutil
import paramiko
from scp import SCPClient
import os
import json
# import time

# 生成脚本, 没有实现写入文件: index.html 




servers = [
# 服务器信息 
    ["xui.google.com","username" ,"password", "sega"], #服务器域名, 服务器用户名,服务器密码,服务器昵称
    ["xui.google.com","user" ,"password", "kinder"] # domain, username, password, nickname
    ]


subscribtion_list =[
# 订阅节点信息， 文件名，节点1，节点2。。。
# every [sub list] is information of one subscribe file
# 1st one is file name of subscribtion ,the others are inbounds name --generated with nickname + inbound's ID No-- 
# that added to each subscribtion file
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
temphtmlpath = './station/sublinks/' #website root folder

temphtmlpath = './temp/x-ui/htmlfile/' #for test
# install docker(using: apt install docker) manually and run command below:
# docker run -d -p 84:80 -p 443:443 -v /root/myroot/station:/usr/share/nginx/html  --name subnginx --restart=always nginx
# folder considered above is website root path.
# subscribe url will be: http://yourdomain:84/sublinks/00-00-allmonitor.TXT

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
    
    sql = 'select id,user_id,up,down,total,remark,enable,expiry_time,autoreset,ip_alert\
        ,listen,port,protocol,settings,stream_settings,tag,sniffing,ip_limit from inbounds where id ={};'.format(id)
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
   
    add = inboundinfo[14].split('"serverName": "')[1].split('"')[0]
    if add =='': 
        print(f'{id}# id的入口: serverName 信息空缺,生成链接失败!! ')
        return

    port = inboundinfo[11]

    # print(inboundinfo[14])
    if protocol == 'trojan':  userid =  inboundinfo[13].split('"password": "')[1].split('"')[0]
    else :  userid = inboundinfo[13].split('"id": "')[1].split('"')[0]

    if protocol == 'vmess':
        alterid = inboundinfo[13].split('"alterId": ')[1].split(' ')[0]
    else : alterid = 0

    network = inboundinfo[14].split('"network": "')[-1].split('"')[0]
    type1 = 'None'
    # host = ''
    host = inboundinfo[14].split('"host": "')[-1].split('"')[0]
    if len(host) <= 5 : host = ''

    if network == 'ws':
        path = inboundinfo[14].split('"path": "')[1].split('"')[0]
    else:  path = '/' 
        
    tls =  inboundinfo[14].split('"security": "')[1].split('"')[0]

    sniffing = ""
    alpn =  inboundinfo[14].split('"alpn": ')[1].split(']')[0].replace('\n','').replace('[','').replace(' ','').replace('"','')
    


    if protocol == 'vmess':
        link_text = '{'+ f'"v": "2",  "ps": "{ps}",  "add": "{add}",  "port": "{port}",  "id": "{userid}", \
                "aid": "{alterid}",  "net": "{network}",  "type": "{type1}",  "host": "{host}",  "path": "{path}",  "tls": "{tls}"' +'}'
        encoded_link_text = link_text.encode("utf-8")
        sublink = 'vmess://' + str(base64.b64encode(encoded_link_text)).split("'")[1]
        # print(sublink)

        
    elif protocol == 'vless' :
        sublink = 'vless://' + f'{userid}@{add}:{port}?type={network}&headerType=none&host={host}&security={tls}&path={path}&sni={add}&flow=#{ps}'
    # elif protocol == 'vless' and network =='tcp':
    #     sublink = 'vless://' + f'{userid}@{add}:{port}?type={network}&headerType=none&host={host}&security={tls}&path={path}&sni={add}&flow=#{ps}'

    elif protocol == 'trojan' :
        sublink = 'trojan://' + f'{userid}@{add}:{port}?type={network}&security={tls}&path={path}&headerType=none#{ps}'
    # elif protocol == 'trojan' and network =='ws':
    #     sublink = 'trojan://' + f'{userid}@{add}:{port}?type={network}&security={tls}&path={path}&headerType=none#{ps}'
    else:
        print(" unsupported protocol")
    # print("type: ",protocol, v,ps,add, port,alterid,network,type1,host,path,tls,sniffing,alpn ) #,userid
    print(sublink)

    return sublink


def get_inbound_link_by_json(db,id):
    # another way to get inbounds setting and link
    sql = 'select id,user_id,up,down,total,remark,enable,expiry_time,autoreset,ip_alert,ip_limit,listen,port\
        ,protocol,settings,stream_settings,tag,sniffing from inbounds where id ={};'.format(id)
    conn = sqlite3.connect(db)
    c = conn.cursor()
    slqresult = c.execute(sql).fetchall()
    inboundinfo = list(slqresult[0])
    conn.close()
    # print (inboundinfo)
    # return inboundinfo

    # inboundinfo = get_inbound_info_by_json(dbfile,1)
    id =  inboundinfo[0]
    user_id =inboundinfo[1]
    up = inboundinfo[2]
    down = inboundinfo[3]
    total =inboundinfo[4]
    remark = inboundinfo[5]
    enable =inboundinfo[6]
    expiry_time = inboundinfo[7]
    autoreset = inboundinfo[8]
    ip_alert = inboundinfo[9]
    ip_limit = inboundinfo[10]
    listen = inboundinfo[11]
    port = inboundinfo[12]
    protocol = inboundinfo[13]
    ''' settings
    {
    "clients": [
        {
        "id": "8b820943-1131-491a-abfb-7b4346e83ad8",
        "email": "xCvi.love@xray.com",
        "flow": ""
        }
    ],
    "decryption": "none",
    "fallbacks": []
    }'''
    settings = inboundinfo[14]
    settings_json = json.loads(settings)
    if protocol =='trojan': clients_id = settings_json["clients"][0]["password"]
    else: clients_id = settings_json["clients"][0]["id"]
    
    clients_email = settings_json["clients"][0]["email"]

    if protocol == 'vless':  
        clients_flow = settings_json["clients"][0]["flow"] 
        decryption = settings_json["decryption"]
        fallbacks = settings_json["fallbacks"]
    elif protocol == 'vmess': 
        clients_alterId = settings_json["clients"][0]["alterId"]
        disableInsecureEncryption = settings_json["disableInsecureEncryption"]

    ''' stream_settings
    {
    "network": "tcp",
    "security": "tls",
    "tlsSettings": {
        "serverName": "sega.gitoff.one",
        "minVersion": "1.2",
        "maxVersion": "1.3",
        "cipherSuites": "",
        "certificates": [
        {
            "certificateFile": "/root/cert/fullchain.cer",
            "keyFile": "/root/cert/sega.gitoff.one.key"
        }
        ],

        "alpn": [
        "h2",
        "http/1.1"
        ]
    },
    "tcpSettings": {
        "header": {
        "type": "none"
        },
        "acceptProxyProtocol": false
    }'''
    stream_settings = inboundinfo[15]
    stream_settings_json = json.loads(stream_settings)
    network = stream_settings_json["network"] # network_type
    security = stream_settings_json["security"]
    tlsSettings = stream_settings_json["tlsSettings"]
    serverName = stream_settings_json["tlsSettings"]["serverName"]
    minVersion = stream_settings_json["tlsSettings"]["minVersion"]
    maxVersion = stream_settings_json["tlsSettings"]["maxVersion"]
    cipherSuites = stream_settings_json["tlsSettings"]["cipherSuites"]
    certificates = stream_settings_json["tlsSettings"]["certificates"]
    certificateFile = stream_settings_json["tlsSettings"]["certificates"][0]["certificateFile"]
    keyFile = stream_settings_json["tlsSettings"]["certificates"][0]["keyFile"]
    alpn = stream_settings_json["tlsSettings"]["alpn"]
    path = '/' # set default 
    header_type = 'None' # set default 
    if network == 'tcp':
        tcpSettings = stream_settings_json["tcpSettings"]
        header = stream_settings_json["tcpSettings"]["header"]
        header_type = stream_settings_json["tcpSettings"]["header"]["type"]
        acceptProxyProtocol = stream_settings_json["tcpSettings"]["acceptProxyProtocol"]
        
    elif network == 'ws':
        wsSettings = stream_settings_json["wsSettings"]
        path = stream_settings_json["wsSettings"]["path"]
        headers = stream_settings_json["wsSettings"]["headers"]    
        acceptProxyProtocol =  stream_settings_json["wsSettings"]["acceptProxyProtocol"]
        


    tag = inboundinfo[16]
    sniffing = inboundinfo[17]
    sniffing_json = json.loads(sniffing)
    enabled = sniffing_json["enabled"]
    destOverride = sniffing_json["destOverride"]
    '''sniffing
    {
    "enabled": true,
    "destOverride": [
        "http",
        "tls"
    ]
    }'''

  
    # print(settings_json)



    if protocol == 'vmess':
        link_text = '{'+ f'"v": "2",  "ps": "{remark}",  "add": "{serverName}",  "port": "{port}",  "id": "{clients_id}", \
                "aid": "{clients_alterId}",  "net": "{network}",  "type": "{header_type}",  "host": "{serverName}",  "path": "{path}",  "tls": "{security}"' +'}'
        encoded_link_text = link_text.encode("utf-8")
        sublink = 'vmess://' + str(base64.b64encode(encoded_link_text)).split("'")[1]
        # print(sublink)
        
    elif protocol == 'vless' :
        sublink = 'vless://' + f'{clients_id}@{serverName}:{port}?type={network}&headerType=none&host={serverName}&security={security}&path={path}&sni={serverName}&flow=#{remark}'

    elif protocol == 'trojan' :
        sublink = 'trojan://' + f'{clients_id}@{serverName}:{port}?type={network}&security={security}&path={path}&headerType=none#{remark}'

    else:
        print(" unsupported protocol")

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
            # link = get_inbound_link_by_json(db,id) # another way to get link

            # save links to each file named with nickname + Id
            # linkfile = linkfilepath + server[0] +"/" + server[3] + str(id)
            # with open(linkfile,'w') as f:
            #     f.write(link + '\n')
            # print(f'{server[0]}的{id}号节点链接成功保存到 {linkfile}')    

            # add links to a dictionary
            dictkey = server[3] + str(id)
            linkdict[dictkey]= link
            
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

# for id in range(1,25):
#     sublink = get_inbound_info_by_json(dbfile,id)
#     print(sublink)


#执行3： 各id 分别保存到字典返回，生成订阅文件
download_xui_db_file()  #下载服务器数据库文件到本地
linkdict = save_inbounds_to_eachfile()
make_sub_file(subscribtion_list,linkdict)


