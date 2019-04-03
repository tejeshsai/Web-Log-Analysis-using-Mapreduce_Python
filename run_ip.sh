python ip_in.py >reducer2.py
bin/hadoop fs -rm -r /k17
bin/hadoop jar /root/hadoop-2.7.2/share/hadoop/mapreduce/hadoop-streaming-2.6.0.jar -file /root/hadoop-2.7.2/mapper.py    -mapper /root/hadoop-2.7.2/mapper.py -file /root/hadoop-2.7.2/reducer2.py   -reducer /root/hadoop-2.7.2/reducer2.py -input /in/* -output /k17
rm output/ip/part-00000
bin/hadoop fs -get /k17/part-00000 /root/hadoop-2.7.2/output/ip
python ip_out.py


