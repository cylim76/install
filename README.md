# v2ray
 v2Ray 一键安装脚本 &amp; 管理脚本

本地安装

```
#安装 git
apt install git

#代码复制到本地
git clone https://github.com/cylim76/v2ray-install.git

# 进入目录及运行
cd v2ray-install
bash xxx.sh
```

远程安装
```
wget -N --no-check-certificate "https://raw.githubusercontent.com/仓库所在的githubID名称/v2ray/master/install.sh" && chmod +x install.sh && ./install.sh
```

# 文件目录

## 1.11-docker-install.md 
- docker 安装方法

## v2ray2022.sh
- v2ray 一键安装脚本,远程安装命令

```
wget -N --no-check-certificate "https://github.com/cylim76/v2ray-install/raw/main/v2ray2022.sh" && chmod +x v2ray2022.sh && ./v2ray2022.sh

```

## v2ray2022en.sh
- 22ray 一键安装脚本部分英文界面 vnc用


# docker静态站
```
docker run -d -p 83:80  -v /root/sublinks/links:/usr/share/nginx/html --name subnginx --restart=always nginx
```
crontab -e
```
9,19,29,39,49,58 * * * * cd /root/sublinks/ && ./ugen.sh && sleep 5 && docker restart subnginx
```


# x-ui 手动安装方法

apt update
apt install socat
apt install git

#安装acme.sh
curl https://get.acme.sh | sh

ln -s  /root/.acme.sh/acme.sh /usr/local/bin/acme.sh

#切换CA机构, 可选： 
acme.sh --set-default-ca --server letsencrypt

#注册证书.有变更会收到邮件
acme.sh --register-account -m    

#申请证书
acme.sh --issue -d flush.gitoff.one --standalone

#安装证书 安装目录为 x-ui 适配
acme.sh --installcert -d flush.gitoff.one --key-file /root/cert/flush.gitoff.one.key --fullchain-file /root/cert/fullchain.cer

# 安装X-ui
1.在线安装
bash <(curl -Ls https://raw.githubusercontent.com/FranzKafukaYu/x-ui/master/install.sh)

2.或本地安装
git clone https://github.com/cylim76/x-ui
cd x-ui
bash install.sh

#面板设置

设置 证书和密钥的路径,登录x-ui面板的时候 不再提示网站不安全
/root/cert.crt
/root/private.key

建立入口(代理服务口)
- 备注
- 选择协议
-设置端口



