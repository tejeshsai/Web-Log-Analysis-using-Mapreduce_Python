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

For running 1st functionality ie IP address, mapper.py and reducer2.py is used. reducer1.py is used as a base reducer to which the input is appended and stored in reducer2.py. run_ip.sh is the shell command to automatically run the 1st functionality. ip_in is the input gui, ip_out is the output gui 
