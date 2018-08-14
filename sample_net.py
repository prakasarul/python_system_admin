##Filesystem
    currNet = subprocess.Popen(['netstat','-nr'], stdout=subprocess.PIPE)
    currNet_out = currNet.communicate()[0].strip().split("\n")
    current_Net =[line.split()[0]+line.split()[1]+line.split()[2] for line in currNet_out[1:]]
