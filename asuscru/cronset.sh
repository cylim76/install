dbus set ss_basic_enable=0
sh /koolshare/ss/ssconfig.sh stop

/koolshare/scripts/ss_online_update.sh fancyss 3

dbus set ss_basic_enable=1
sh /koolshare/ss/ssconfig.sh restart

cru a ssgengxin "*/28 3,4,5,6,7,12,15,17,21 * * * /koolshare/scripts/ss_online_update.sh fancyss 3"
cru a pplusgengxin "3 6-21 * * * /koolshare/scripts/pushplus_check_task.sh"
cru a asusset "*/10  * * * /root/cronset.sh"
