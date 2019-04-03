python web_in.py >reducer2.py
bin/hadoop fs -rm -r /k19
bin/hadoop jar /root/hadoop-2.7.2/share/hadoop/mapreduce/hadoop-streaming-2.6.0.jar -file /root/hadoop-2.7.2/mapper4.py    -mapper /root/hadoop-2.7.2/mapper4.py -file /root/hadoop-2.7.2/reducer2.py   -reducer /root/hadoop-2.7.2/reducer2.py -input /in/* -output /k19
rm output/website/part-00000
bin/hadoop fs -get /k19/part-00000 /root/hadoop-2.7.2/output/website
python web_out.py


