#!/bin/bash



mkdir -p /root/myroot/station/sublinks/
mkdir -p /root/myroot/station/iprklinks/




split -l 1  --numeric-suffixes=1   uinbounds.sh ulink
split -l 1  --numeric-suffixes=1   sinbounds.sh slink


echo 'start to make groupfiles'
sleep 1


echo ‘添加节点到监测组 00-00-allmonitor’
cat uinbounds.sh >> ugroup00
cat sinbounds.sh >> ugroup00

echo '**********us添加到各组**************'
echo '添加到组： 01-02-hydroxides'
cat ulink01 >> ugroup01
cat ulink02 >> ugroup01

echo '添加到组： 03-03-eshareagen'
cat ulink03 >> ugroup03

echo '添加到组： 04-09-us-router'
cat ulink04 >> ugroup04
cat ulink05 >> ugroup04
cat ulink06 >> ugroup04
cat ulink07 >> ugroup04
cat ulink08 >> ugroup04
cat ulink09 >> ugroup04

echo '添加到组： 10-11-molecular'
cat ulink10 >> ugroup10
cat ulink11 >> ugroup10

echo '添加到组： 12-13-patriotic'
cat ulink12 >> ugroup12
cat ulink13 >> ugroup12

echo '添加到组： 14-15-equation'
cat ulink14 >> ugroup14
cat ulink15 >> ugroup14


echo '添加到组： 16-17-kovalence'
cat ulink16 >> ugroup16
cat ulink17 >> ugroup16

echo '添加到组： 18-18-kongdd'
cat ulink18 >> ugroup18

echo '添加到组： 19-20-crisis'
cat ulink19 >> ugroup19
cat ulink20 >> ugroup19

echo '添加到组： 21-22park66'
cat ulink21 >> ugroup21
cat ulink22 >> ugroup21

echo '**********sg添加到各组**************'
echo 'sg添加到组： 01-02-hydroxides'
cat slink08 >> ugroup01
cat slink09 >> ugroup01

echo 'sg添加到组： 03-03-eshareagen'
cat slink08 >> ugroup03

echo 'sg添加到组： 04-09-us-router'

cat slink03 >> ugroup04
cat slink04 >> ugroup04
cat slink05 >> ugroup04
cat slink06 >> ugroup04
cat slink07 >> ugroup04

echo '添加到组： 10-11-molecular'
cat slink01 >> ugroup10
cat slink02 >> ugroup10

echo 'sg添加到组： 21-22park66'
cat slink10 >> ugroup21
cat slink11 >> ugroup21
cat slink12 >> ugroup21
cat slink13 >> ugroup21
cat slink14 >> ugroup21
cat slink15 >> ugroup21
cat slink16 >> ugroup21

echo 'sg添加到组： 14-15-equation'
cat slink09 >> ugroup14

echo 'start to encode files'
#sleep 1

base64 ugroup00 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/00-00-allmonitor.TXT
base64 ugroup01 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/01-02-hydroxides.TXT
base64 ugroup03 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/03-03-eshareagen.TXT
base64 ugroup04 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/04-09-us-router.TXT
base64 ugroup10 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/10-11-molecular.TXT
base64 ugroup12 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/12-13-patriotic.TXT
base64 ugroup14 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/14-15-equation.TXT
base64 ugroup16 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/16-17-kovalence.TXT
base64 ugroup18 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/18-18-kongdd.TXT
base64 ugroup19 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/19-20-crisis.TXT
base64 ugroup21 -w 0 > ugroup_encoded && mv ugroup_encoded ./station/sublinks/21-22park66.TXT


echo '<!DOCTYPE html>' > 50x.html
echo '<html>' >> 50x.html
echo '<head>' >> 50x.html
echo '<title>Error</title>' >> 50x.html
echo '<style>' >> 50x.html
echo 'html { color-scheme: light dark; }' >> 50x.html
echo 'body { width: 35em; margin: 0 auto;' >> 50x.html
echo 'font-family: Tahoma, Verdana, Arial, sans-serif; }' >> 50x.html
echo '</style>' >> 50x.html
echo '</head>' >> 50x.html
echo '<body>' >> 50x.html
echo '<h1>An error occurred.</h1>' >> 50x.html
echo '<p>Sorry, the page you are looking for is currently unavailable.<br/>' >> 50x.html
echo 'Please try again later.</p>' >> 50x.html
echo '<p>If you are the system administrator of this resource then you should check' >> 50x.html
echo 'the error log for details.</p>' >> 50x.html
echo '<p><em>Faithfully yours, nginx.</em></p>' >> 50x.html
echo '</body>' >> 50x.html
echo '</html>' >> 50x.html

mv 50x.html ./station/index.html
cp ./station/index.html ./station/sublinks/index.html


echo 'delete all links and group files'
#sleep 1

rm  -rf ./ulink*
rm  -rf ./slink*
rm  -rf ./ugroup*




wget https://github.com/cylim76/install/raw/main/iptv/100hd.m3u
mv ./100hd.m3u /root/myroot/station/iprklinks/100hd.m3u

#git clone http:/github.com/YanG-1989/m3u /root/myroot/station/iprklinks/YanG-1989
#git clone https://github.com/gjwj666/jichang /root/myroot/station/iprklinks/gjwj666

docker restart subnginx
