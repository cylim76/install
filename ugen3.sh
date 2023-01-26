#!/bin/bash



mkdir -p /root/myroot/station/sublinks/
#mkdir -p /root/myroot/station/iprklinks/
rm -rf /root/myroot/station/sublinks/*

server1=''
server2=''


#静态站路径
htmlpath='/root/myroot/station/sublinks'

split -l 1  --numeric-suffixes=1   $server1 sg
split -l 1  --numeric-suffixes=1   $server2 us

#订阅文件名及给添加的 节点
sublink00="$server1 $server2" 
destsublink00='00-00-allmonitor.TXT'

sublink01='sg01 sg02                           us01 us02'
destsublink01='01-02-hydroxides.TXT'

sublink03='sg03 sg04                           us03 us04'
destsublink03='03-03-eshareagen.TXT'

sublink04='sg05 sg06 sg07 sg08 sg09            us05 us06 us07 us08 us09'
destsublink04='04-09-us-router.TXT'

sublink10='sg10 sg11                           us10 us11'
destsublink10='10-11-molecula.TXT'

sublink12='sg12 sg13                           us12 us13'
destsublink12='12-13-patriotic.TXT'

sublink14='sg14 sg15                           us14 us15'
destsublink14='14-15-equation.TXT'

sublink16='sg16 sg17                           us16 us17'
destsublink16='16-17-kovalence.TXT'

sublink18='sg18                                us18'
destsublink18='18-18-kongdd.TXT'

sublink19='sg19 sg20                           us19 us20'
destsublink19='19-20-crisis.TXT'


sublink21='sg18 sg19 sg20 sg21 sg22 sg23 sg24  us21 us22'
destsublink21='21-22-park66.TXT'

# 循环生成订阅文件
groupno=0
while [ $groupno -le 30 ] #数字大于订阅链接需要
do
    if [ $groupno -le 9 ]
    then
        eval "srcfile=\${sublink0$groupno}"
        eval "destfile=\${destsublink0$groupno}"
    else
        eval "srcfile=\${sublink$groupno}"
        eval "destfile=\${destsublink$groupno}"
    fi

    if [[ ! -z "$srcfile"  ]]
    then
        cat $srcfile | base64 -w 0 > $htmlpath/$destfile
        echo 生成订阅文件 $htmlpath/$destfile
    fi
    ((groupno++))

done




tee index.html<<EOF
<!DOCTYPE html>
<html>
<head>
<title>Error</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>An error occurred.</h1>
<p>Sorry, the page you are looking for is currently unavailable.<br/>
Please try again later.</p>
<p>If you are the system administrator of this resource then you should check
the error log for details.</p>
<p><em>Faithfully yours, nginx.</em></p>
</body>
</html>
EOF

cp index.html $htmlpath/index.html
cp index.html ./station/iprklinks/index.html
mv index.html ./station/index.html


rm  -rf ./us* ./sg*
#rm  -rf ./sublinksg*
#rm  -rf ./sublinkgroup*




# wget https://github.com/cylim76/install/raw/main/iptv/100hd.m3u
#mv ./100hd.m3u /root/myroot/station/iprklinks/100hd.m3u

#git clone http:/github.com/YanG-1989/m3u /root/myroot/station/iprklinks/YanG-1989
#git clone https://github.com/gjwj666/jichang /root/myroot/station/iprklinks/gjwj666

docker restart subnginx
