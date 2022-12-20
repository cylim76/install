

# 1. 安装X-ui


1.在线安装
```
bash <(curl -Ls https://raw.githubusercontent.com/FranzKafukaYu/x-ui/master/install.sh)
```

2.或本地安装
```
git clone https://github.com/cylim76/x-ui
cd x-ui
bash install.sh
```

# 2. 安装acme.sh  申请证书(手动)

```
curl https://get.acme.sh | sh
```
做个快捷方式

```
ln -s  /root/.acme.sh/acme.sh /usr/local/bin/acme.sh
```

## 切换CA机构, 可选：
```
acme.sh --set-default-ca --server letsencrypt
```

## 注册证书.有变更会收到邮件
```
acme.sh --register-account -m    
```

## 申请证书
```
acme.sh --issue -d flush.gitoff.one --standalone
```

## 安装证书 安装目录为 x-ui 适配
```
acme.sh --installcert -d flush.gitoff.one --key-file /root/cert/flush.gitoff.one.key --fullchain-file /root/cert/fullchain.cer
```

### 备份的数据库， 启动失败时， 查看日志， 证书文件补全后启动面板



# 3. docker静态站
```
docker run -d -p 83:80  -v /root/sublinks/links:/usr/share/nginx/html --name subnginx --restart=always nginx
```
docker 镜像new
```
docker run -d -p 84:80 -p 443:443 -v /root/myroot/station:/usr/share/nginx/html  --name subnginx --restart=always nginx
docker run -d -p 84:80 -v /root/myroot/station:/usr/share/nginx/html  --name subnginx --restart=always nginx
```

定时任务设置， 运行命令，添加定时运行脚本
```
crontab -e
9,19,29,39,49,58 * * * * cd /root/sublinks/ && ./ugen.sh && sleep 5 && docker restart subnginx
```

# 4. 那匹马

apt install docker docker-compose

docker-compose.yml

docker-compose up -d

http://127.0.0.1:81

Email:    admin@example.com

Password: changeme



# v2ray

## 本地安装，代码复制到本地

```
git clone https://github.com/cylim76/v2ray-install.git
cd v2ray-install
bash v2ray-install.sh
```

## 远程安装
```
wget -N --no-check-certificate "https://raw.githubusercontent.com/仓库所在的githubID名称/v2ray/master/install.sh" && chmod +x install.sh && ./install.sh
```

```
wget -N --no-check-certificate "https://github.com/cylim76/v2ray-install/raw/main/v2ray2022.sh" && chmod +x v2ray2022.sh && ./v2ray2022.sh
wget -N --no-check-certificate "https://github.com/cylim76/v2ray-install/raw/main/v2ray2022.sh" && chmod +x v2ray2022.sh && ./v2ray2022en.sh
 #  v2ray2022en.sh 一键安装脚本部分英文界面 vnc用
```






 


