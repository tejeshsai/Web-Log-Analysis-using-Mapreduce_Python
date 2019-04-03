./run_ip.sh
./run_time.sh
./run_web.sh
cat ~/output/ip/part-00000 ~/output/time/part-00000 ~/output/website/part-00000 > merged-file
xdg-open merged-file.txt


