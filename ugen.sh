#!/bin/bash




echo "make dir links"
rm -r -f links
mkdir links


split -l 1  --numeric-suffixes=1   uinbounds.sh ulink
split -l 1  --numeric-suffixes=1   sinbounds.sh slink


echo 'start to make groupfiles'
sleep 1


echo ‘添加节点到监测分组’
cat uinbounds.sh >> ugroup00
cat sinbounds.sh >> ugroup00


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

echo '添加到组： 10-11-mamamia.TXT'
cat ulink10 >> ugroup10
cat ulink11 >> ugroup10

echo '添加到组： 12-13-padre.TXT'
cat ulink12 >> ugroup12
cat ulink13 >> ugroup12

echo '添加到组： 14-15-wxqqq.TXT'
cat ulink14 >> ugroup14
cat ulink15 >> ugroup14


echo '添加到组： 16-17-kimss.TXT'
cat ulink16 >> ugroup16
cat ulink17 >> ugroup16

echo '添加到组： 18-18-kongdd.TXT'
cat ulink18 >> ugroup18

echo '添加到组： 19-20-Kris.TX'
cat ulink19 >> ugroup19
cat ulink20 >> ugroup19

echo '添加到组： 21-22park66.TXT'
cat ulink21 >> ugroup21
cat ulink22 >> ugroup21


echo 'sg添加到组： 04-09-us-router'
cat slink08 >> ugroup01
cat slink09 >> ugroup01

echo 'sg添加到组： 04-09-us-router'
cat slink01 >> ugroup04
cat slink02 >> ugroup04
cat slink03 >> ugroup04
cat slink04 >> ugroup04

echo 'sg添加到组： 21-22park66'
cat slink05 >> ugroup21
cat slink06 >> ugroup21
cat slink07 >> ugroup21
cat slink08 >> ugroup21
cat slink09 >> ugroup21

cat slink08 >> ugroup14
cat slink09 >> ugroup14

echo 'start to encode files'
#sleep 1

base64 ugroup00 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/00-00-allmonitor.TXT
base64 ugroup01 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/01-02-hydroxides.TXT
base64 ugroup03 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/03-03-eshareagen.TXT
base64 ugroup04 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/04-09-us-router.TXT
base64 ugroup10 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/10-11-molecular.TXT
base64 ugroup12 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/12-13-patriotic.TXT
base64 ugroup14 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/14-15-equation.TXT
base64 ugroup16 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/16-17-kovalence.TXT
base64 ugroup18 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/18-18-kongdd.TXT
base64 ugroup19 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/19-20-crisis.TXT
base64 ugroup21 -w 0 > ugroup_encoded && mv ugroup_encoded ./links/21-22park66.TXT


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
mv 50x.html ./links/index.html


echo 'delete all links and group files'
 

rm  -rf ./ulink*
rm  -rf ./slink*
rm  -rf ./ugroup*







echo 'docker restart subnginx'
docker restart subnginx
