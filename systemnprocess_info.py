import psutil
import datetime
import os

print "CPU Times of OS:"
print psutil.cpu_times()

print ""

print "CPU Count of OS:"
print " Including Logical CPUs : "
print psutil.cpu_count()
print " Excluding Logical CPUs : "
print psutil.cpu_count(logical=False)

print ""

print "Virtual Memory of OS:"
print psutil.virtual_memory()


print "Swap Memory of OS:"
print psutil.swap_memory()

print ""

print "Disk Partitions of OS:"
print psutil.disk_partitions()

print ""

print "Process Information of OS:"
print "Process Id List of OS:"
print psutil.pids()
for proc in psutil.process_iter():
	try:
		pinfo = proc.as_dict(attrs=['pid','name'])
	except psutil.NoSuchProcess:
		pass
	else:
		print(pinfo)
