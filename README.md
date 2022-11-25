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






