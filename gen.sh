#!/bin/bash




echo "make dir links"
rm -r -f links
mkdir links

 



split -l 1  --numeric-suffixes=1   inbounds.sh ulink


echo ‘添加节点到分组’
echo '添加到组： 01-02-Mine.TXT'
cat ulink01 >> ./links/ugroup01
cat ulink02 >> ./links/ugroup01

echo '添加到组： 03-03-eessgg.TXT'
cat ulink03 >> ./links/ugroup03

echo '添加到组： 00-01-us-router-04-09.TXT'
cat ulink04 >> ./links/ugroup04
cat ulink05 >> ./links/ugroup04
cat ulink06 >> ./links/ugroup04
cat ulink07 >> ./links/ugroup04
cat ulink08 >> ./links/ugroup04
cat ulink09 >> ./links/ugroup04

echo '添加到组： 10-11-mamamia.TXT'
cat ulink10 >> ./links/ugroup10
cat ulink11 >> ./links/ugroup10

echo '添加到组： 12-13-padre.TXT'
cat ulink12 >> ./links/ugroup12
cat ulink13 >> ./links/ugroup12

echo '添加到组： 14-15-wxqqq.TXT'
cat ulink14 >> ./links/ugroup14
cat ulink15 >> ./links/ugroup14

echo '添加到组： 16-17-kimss.TXT'
cat ulink16 >> ./links/ugroup16
cat ulink17 >> ./links/ugroup16

echo '添加到组： 18-18-kongdd.TXT'
cat ulink18 >> ./links/ugroup18

echo '添加到组： 19-20-Kris.TX'
cat ulink19 >> ./links/ugroup19
cat ulink20 >> ./links/ugroup19

echo '添加到组： 21-22park66.TXT'
cat ulink21 >> ./links/ugroup21
cat ulink22 >> ./links/ugroup21




base64 ./links/ugroup01 > ./links/usub_encoded | mv ./links/usub_encoded ./links/01-02-Mine.TXT
base64 ./links/ugroup03 > ./links/usub_encoded | mv ./links/usub_encoded ./links/03-03-eessgg.TXT
base64 ./links/ugroup04 > ./links/usub_encoded | mv ./links/usub_encoded ./links/00-01-us-router-04-09.TXT
base64 ./links/ugroup10 > ./links/usub_encoded | mv ./links/usub_encoded ./links/10-11-mamamia.TXT
base64 ./links/ugroup12 > ./links/usub_encoded | mv ./links/usub_encoded ./links/12-13-padre.TXT
base64 ./links/ugroup14 > ./links/usub_encoded | mv ./links/usub_encoded ./links/14-15-wxqqq.TXT
base64 ./links/ugroup16 > ./links/usub_encoded | mv ./links/usub_encoded ./links/16-17-kimss.TXT
base64 ./links/ugroup18 > ./links/usub_encoded | mv ./links/usub_encoded ./links/18-18-kongdd.TXT
base64 ./links/ugroup19 > ./links/usub_encoded | mv ./links/usub_encoded ./links/19-20-Kris.TXT
base64 ./links/ugroup21 > ./links/usub_encoded | mv ./links/usub_encoded ./links/21-22park66.TXT

rm  ./ulink*
rm  ./links/ugroup*
