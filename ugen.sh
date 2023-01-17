#!/bin/bash



mkdir -p /root/myroot/station/sublinks/
mkdir -p /root/myroot/station/iprklinks/
rm -rf /root/myroot/station/sublinks/*



split -l 1  --numeric-suffixes=1   kinder.tltk.xyz.sh sublinkus
split -l 1  --numeric-suffixes=1   sega.gitoff.one.sh sublinksg


echo 'start to make groupfiles'
sleep 1


echo ‘添加节点到监测组 00-00-allmonitor’
cat kinder.tltk.xyz.sh sega.gitoff.one.sh >> sublinkgroup00

echo '**********us添加到各组**************'
echo '添加到组： 01-02-hydroxides'
cat sublinkus01 sublinkus02 >> sublinkgroup01
cat sublinksg01 sublinksg02 >> sublinkgroup01

echo '添加到组： 03-03-eshareagen'
cat sublinkus03 sublinkus04  >> sublinkgroup03
cat sublinksg03 sublinksg04  >> sublinkgroup03

echo '添加到组： 04-09-us-router'
cat sublinkus05 sublinkus06 sublinkus07 sublinkus08 sublinkus09 >> sublinkgroup04
cat sublinksg05 sublinksg06 sublinksg07 sublinksg08 sublinksg09 >> sublinkgroup04

echo '添加到组： 10-11-molecular'
cat sublinkus10 sublinkus11 >> sublinkgroup10
cat sublinksg10 sublinksg11 >> sublinkgroup10

echo '添加到组： 12-13-patriotic'
cat sublinkus12 sublinkus13 >> sublinkgroup12
cat sublinksg12 sublinksg13 >> sublinkgroup12

echo '添加到组： 14-15-equation'
cat sublinkus14 sublinkus15 >> sublinkgroup14
cat sublinksg14 sublinksg15 >> sublinkgroup14

echo '添加到组： 16-17-kovalence'
cat sublinkus16 sublinkus17 >> sublinkgroup16
cat sublinksg16 sublinksg17 >> sublinkgroup16

echo '添加到组： 18-18-kongdd'
cat sublinkus18 >> sublinkgroup18
#cat sublinksg18 >> sublinkgroup18

echo '添加到组： 19-20-crisis'
cat sublinkus19 sublinkus20 >> sublinkgroup19
cat sublinksg19 sublinksg20 >> sublinkgroup19

echo '添加到组： 21-22park66'
cat sublinkus21 sublinkus22 >> sublinkgroup21
cat sublinksg21 sublinksg22 sublinksg18 >> sublinkgroup21


echo 'start to encode files'

base64 sublinkgroup00 -w 0 > ./station/sublinks/00-00-allmonitor.TXT
base64 sublinkgroup01 -w 0 > ./station/sublinks/01-02-hydroxides.TXT
base64 sublinkgroup03 -w 0 > ./station/sublinks/03-03-eshareagen.TXT
base64 sublinkgroup04 -w 0 > ./station/sublinks/04-09-us-router.TXT
base64 sublinkgroup10 -w 0 > ./station/sublinks/10-11-molecular.TXT
base64 sublinkgroup12 -w 0 > ./station/sublinks/12-13-patriotic.TXT
base64 sublinkgroup14 -w 0 > ./station/sublinks/14-15-equation.TXT
base64 sublinkgroup16 -w 0 > ./station/sublinks/16-17-kovalence.TXT
base64 sublinkgroup18 -w 0 > ./station/sublinks/18-18-kongdd.TXT
base64 sublinkgroup19 -w 0 > ./station/sublinks/19-20-crisis.TXT
base64 sublinkgroup21 -w 0 > ./station/sublinks/21-22-park66.TXT


echo '<!DOCTYPE html>' > index.html
echo '<html>' >> index.html
echo '<head>' >> index.html
echo '<title>Error</title>' >> index.html
echo '<style>' >> index.html
echo 'html { color-scheme: light dark; }' >> index.html
echo 'body { width: 35em; margin: 0 auto;' >> index.html
echo 'font-family: Tahoma, Verdana, Arial, sans-serif; }' >> index.html
echo '</style>' >> index.html
echo '</head>' >> index.html
echo '<body>' >> index.html
echo '<h1>An error occurred.</h1>' >> index.html
echo '<p>Sorry, the page you are looking for is currently unavailable.<br/>' >> index.html
echo 'Please try again later.</p>' >> index.html
echo '<p>If you are the system administrator of this resource then you should check' >> index.html
echo 'the error log for details.</p>' >> index.html
echo '<p><em>Faithfully yours, nginx.</em></p>' >> index.html
echo '</body>' >> index.html
echo '</html>' >> index.html

cp index.html ./station/sublinks/index.html
#cp index.html ./station/iprklinks/index.html
mv index.html ./station/index.html



echo 'delete all links and group files'
#sleep 1

rm  -rf ./sublink*
#rm  -rf ./sublinksg*
#rm  -rf ./sublinkgroup*




# wget https://github.com/cylim76/install/raw/main/iptv/100hd.m3u
#mv ./100hd.m3u /root/myroot/station/iprklinks/100hd.m3u

#git clone http:/github.com/YanG-1989/m3u /root/myroot/station/iprklinks/YanG-1989
#git clone https://github.com/gjwj666/jichang /root/myroot/station/iprklinks/gjwj666

docker restart subnginx
