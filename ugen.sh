#!/bin/bash




echo "make dir links"
rm -r -f links
mkdir links

 



split -l 1  --numeric-suffixes=1   inbounds.sh ulink

echo 'start to make groupfiles'
sleep 2


echo ‘添加节点到分组’
echo '添加到组： 01-02-Mine.TXT'
cat ulink01 >> ugroup01
cat ulink02 >> ugroup01

echo '添加到组： 03-03-eessgg.TXT'
cat ulink03 >> ugroup03

echo '添加到组： 00-01-us-router-04-09.TXT'
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


echo 'start to encode files'
sleep 2

base64 ugroup01 > ugroup01_encoded
base64 ugroup03 > ugroup03_encoded
base64 ugroup04 > ugroup04_encoded
base64 ugroup10 > ugroup10_encoded
base64 ugroup12 > ugroup12_encoded
base64 ugroup14 > ugroup14_encoded
base64 ugroup16 > ugroup16_encoded
base64 ugroup18 > ugroup18_encoded
base64 ugroup19 > ugroup19_encoded
base64 ugroup21 > ugroup21_encoded

echo 'start to move files'
sleep 2

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





echo 'delete all links and group files'
sleep 2

rm  -rf ./ulink*
rm  -rf ./ugroup*
