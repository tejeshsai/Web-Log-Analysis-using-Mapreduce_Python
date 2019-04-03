python time_in.py >reducer2.py
bin/hadoop fs -rm -r /k18
bin/hadoop jar /root/hadoop-2.7.2/share/hadoop/mapreduce/hadoop-streaming-2.6.0.jar -file /root/hadoop-2.7.2/mapper1.py    -mapper /root/hadoop-2.7.2/mapper1.py -file /root/hadoop-2.7.2/reducer2.py   -reducer /root/hadoop-2.7.2/reducer2.py -input /in/* -output /k18
rm output/time/part-00000
bin/hadoop fs -get /k18/part-00000 /root/hadoop-2.7.2/output/time/part-00000
python time_out.py


