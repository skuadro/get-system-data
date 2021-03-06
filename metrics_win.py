import psutil, sys

if len(sys.argv) != 2 :
    print "Usage: 'metrics_win mem' or 'metrics_win cpu'"
    sys.exit (1)
option=(sys.argv[1])
if option=='cpu':
	cptimes = psutil.cpu_times()
	#print cptimes
	print 'system.cpu.idle '+ str(cptimes[2])
	print 'system.cpu.user '+ str(cptimes[0])
	#print 'system.cpu.guest '+ str(cptimes[8])
	#print 'system.cpu.iowait '+ str(cptimes[4])
	#print 'system.cpu.steal '+ str(cptimes[7])
	print 'system.cpu.system '+ str(cptimes[1])
elif option=='mem':
	memory = psutil.virtual_memory()
	swap = psutil.swap_memory()
	#print memory
	#print swap
	print 'virtual total '+ str(memory[0])
	print 'virtual used '+ str(memory[3])
	print 'virtual free '+ str(memory[4])
	#print 'virtual shared '+ str(memory[9])
	print 'swap total '+ str(swap[0])
	print 'swap used '+ str(swap[1])
	print 'swap free '+ str(swap[2])
else:
	print "incorrect option"
