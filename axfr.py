#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################################
# axfr.py:	Attempts zone transfers (axfr queries) on multiple domains in a list against
#		a single name server.
# Example:	$ axfr.py -n nameserver.target.com -d list_of_domains.txt
# Author:	VIVI | <Website: thevivi.net> | <Email: gabriel@thevivi.net> | <Twitter: @_V1VI>
################################################################################################

import argparse
from subprocess import Popen, PIPE, STDOUT
import time
import sys

# Console colors
W = '\033[0m'     #white (normal)
R = '\033[31m'    #red
T = '\033[93m'    #tan
LG = '\033[1;32m' #light green

class Logger:

    def __init__(self, stdout, filename):
        self.stdout = stdout
        self.logfile = file(filename, 'w')

    def write(self, text):
        self.stdout.write(text)
        self.logfile.write(text)

    def close(self):
        self.stdout.close()
        self.logfile.close()

def parse_args():

    # Arguments

    parser = argparse.ArgumentParser(description="Attempts zone transfers on " +
    	"a list of domain names against a single name server")

    parser.add_argument(
        "-n",
        "--nameserver",
        help="Name server e.g. ns1.target.com",
        required=True
    )
    parser.add_argument(
        "-d",
        "--domains",
        help="Path to list of domain names",
        required=True,
    )

    parser.add_argument(
    	"-o",
    	"--output",
    	help='Destination output file')

    return parser.parse_args()

def shutdown():

	 print '\n[' + R + '!' + W + '] Closing'
	 sys.exit()

def zoneTransfer():

	start = time.time()
	count = 0

	nameServer = "@" + args.nameserver
	domainList = open(args.domains, 'r')
	
	for line in domainList.readlines():
		
		line = line.strip('\n')
		count +=1

		print '[' + T + str(count) + W + '] Domain Name:  ' + LG + line +W
		p = Popen(['dig', 'axfr', str(nameServer), str(line)], stdin=PIPE, \
			stdout=PIPE, stderr=STDOUT, close_fds=True)
		output = p.stdout.read()
		print output
		print "---------------------------------------------------------------------\n"

	print 'Finished. \nScript runtime: '+ T , time.time()-start, 'seconds.'


# Main section
if __name__ == "__main__":

	print """
                ▄▄                     
               ▐▛▀                     
     ▟██▖▝█ █▘▐███  █▟█▌     ▐▙█▙ ▝█ █▌
     ▘▄▟▌ ▐█▌  ▐▌   █▘       ▐▛ ▜▌ █▖█ 
    ▗█▀▜▌ ▗█▖  ▐▌   █        ▐▌ ▐▌ ▐█▛ 
    ▐▙▄█▌ ▟▀▙  ▐▌   █     █  ▐█▄█▘  █▌ 
     ▀▀▝▘▝▀ ▀▘ ▝▘   ▀     ▀  ▐▌▀▘   █  
                             ▐▌    █▌  
	"""

	# Parse args
	args = parse_args()

	if args.output != None:
		logger = Logger(sys.stdout, args.output)
		sys.stdout = logger

	try:
		zoneTransfer()
	except KeyboardInterrupt:
		shutdown()