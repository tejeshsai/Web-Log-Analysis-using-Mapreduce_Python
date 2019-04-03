# Web-Log-Analysis
Web Log Analysis using Hadoop and Python ( Shell Programming for Automating )

My project is analysing web log file with the help of hadoop and python.
Here, Python is used for GUI, for writing mapper and reducer functions.
Hadoop is used for Data processing. Shell programs are for automating all bash commands for removing frequent manual intervention.

All my files are under /root/hadoop-2.7.2 folder. The output is written to /root/hadoop-2.7.2/output folder.

I have included three functionalities as of now. 
1) Getting top n list of frequent ip addresses requesting sites
2) Getting top n list of peak hours
3) Getting top n list of frequent websites requested
(The n can be given as an input in the gui)

First of all : Run hadoop {commands: service ssh restart, sbin/start-all.sh with hadoop as current folder}
Place the Dataset.txt into the 'in' folder of HDFS. The programs are written in such a way that the ouputs ie part-00000 files are directly stored into local storage from HDFS at /root/hadoop-2.7.2/output/{ip/peak_hours/website folder}
*The outputs files are directly read into output gui of respective functionality*

For running 1st functionality ie IP address, mapper.py and reducer2.py is used. reducer1.py is used as a base reducer to which the input(from input gui) is appended and stored in reducer2.py. run_ip.sh is the shell command to automatically run the 1st functionality. ip_in is the input gui, ip_out is the output gui. 

For running 1st functionality ie IP address, mapper2.py and reducer2.py is used. reducer1.py is used as a base reducer to which the input(from input gui) is appended and stored in reducer2.py. run_time.sh is the shell command to automatically run the 1st functionality. time_in is the input gui, ip_out is the output gui.* Not properly shown ouput. Ex: Ouput is shown as [('21':4672)] For 4672 hits in between 21:00 to 22:00*

For running 1st functionality ie IP address, mapper4.py and reducer2.py is used. reducer1.py is used as a base reducer to which the input(from input gui) is appended and stored in reducer2.py. run_web.sh is the shell command to automatically run the 1st functionality. web_in is the input gui, web_out is the output gui. 

Must read:
If sh file is denied permission, try chmod 777 filename.sh in the terminal to give permission.
Running sh file : ./filename.sh
