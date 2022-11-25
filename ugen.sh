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
sleep 1

base64 ugroup00 -w 0 > ugroup00_encoded
base64 ugroup01 -w 0 > ugroup01_encoded
base64 ugroup03 -w 0 > ugroup03_encoded
base64 ugroup04 -w 0 > ugroup04_encoded
base64 ugroup10 -w 0 > ugroup10_encoded
base64 ugroup12 -w 0 > ugroup12_encoded
base64 ugroup14 -w 0 > ugroup14_encoded
base64 ugroup16 -w 0 > ugroup16_encoded
base64 ugroup18 -w 0 > ugroup18_encoded
base64 ugroup19 -w 0 > ugroup19_encoded
base64 ugroup21 -w 0 > ugroup21_encoded

echo 'start to move files'
sleep 1

mv ugroup00_encoded ./links/00-00-allmonitor.TXT
mv ugroup01_encoded ./links/01-02-hydroxides.TXT
mv ugroup03_encoded ./links/03-03-eshareagen.TXT
mv ugroup04_encoded ./links/04-09-us-router.TXT
mv ugroup10_encoded ./links/10-11-molecular.TXT
mv ugroup12_encoded ./links/12-13-patriotic.TXT
mv ugroup14_encoded ./links/14-15-equation.TXT
mv ugroup16_encoded ./links/16-17-kovalence.TXT
mv ugroup18_encoded ./links/18-18-kongdd.TXT
mv ugroup19_encoded ./links/19-20-crisis.TXT
mv ugroup21_encoded ./links/21-22park66.TXT


echo '<!DOCTYPE html>' > index.html
echo '<html>' >> index.html
echo '<head>' >> index.html
echo '<title>Welcome to nginx!</title>' >> index.html
echo '<style>' >> index.html
echo 'html { color-scheme: light dark; }' >> index.html
echo 'body { width: 35em; margin: 0 auto;' >> index.html
echo 'font-family: Tahoma, Verdana, Arial, sans-serif; }' >> index.html
echo '</style>' >> index.html
echo '</head>' >> index.html
echo '<body>' >> index.html
echo '<h1>Welcome to nginx!</h1>' >> index.html
echo '<p>If you see this page, the nginx web server is successfully installed and' >> index.html
echo 'working. Further configuration is required.</p>' >> index.html
echo '' >> index.html
echo '<p>For online documentation and support please refer to' >> index.html
echo '<a href='http://nginx.org/'>nginx.org</a>.<br/>' >> index.html
echo 'Commercial support is available at' >> index.html
echo '<a href='http://nginx.com/'>nginx.com</a>.</p>' >> index.html
echo '' >> index.html
echo '<p><em>Thank you for using nginx.</em></p>' >> index.html
echo '</body>' >> index.html
echo '</html>' >> index.html
mv index.html ./links/index.html


echo 'delete all links and group files'
sleep 1

rm  -rf ./ulink*
rm  -rf ./slink*
rm  -rf ./ugroup*








docker restart subnginx
