# 系统更新
```
apt update
apt upgrade
apt autoremove
```

# 安装系统依赖包

```	
apt install     apt-transport-https     ca-certificates     gnupg-agent     software-properties-common
```

# 加入Docker信息库密钥
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
# key确认
```
apt-key list
```
9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBFCD88

# 最后8位作为fingerprint参数
```
apt-key fingerprint  0EBFCD88  #key的后8位
```
# 将Docker信息库加入本地信息库当中
```
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```
   
# 查看OS采用核心号
lsb_release -cs

# 查看信息库加入的位置和内容
```
cat /etc/apt/sources.list|grep docker
```

# 系统再更新
```
sudo apt update
sudo apt upgrade
```

# Docker安装
```
apt show docker-ce
apt install docker-ce docker-ce-cli containerd.io
```

# 校验安装
```
docker help
docker version
```
