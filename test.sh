#! /bin/sh
for ((i==0;i<10;i++))
do
	tracert google.com >> tracefile.txt
	echo "****************************************" >> tracefile.txt
	sleep 30
done 
