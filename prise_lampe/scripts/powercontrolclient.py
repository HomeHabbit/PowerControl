#!/usr/bin/env python
 
import sys
import rospy
from prise_lampe.srv import *
 
def add_two_ints_client(ids, state, dimming):
	print"test"
	rospy.wait_for_service('add_two_ints')
	try:
		add_two_ints = rospy.ServiceProxy('add_two_ints', prise_lampe)
		resp1 = add_two_ints(ids, state, dimming)
		return resp1.state
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def usage():
	return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
	if len(sys.argv) == 4:
		ids = int(sys.argv[1])
		state = sys.argv[2]
		dimming = int(sys.argv[3])
	else:
		print usage()
		sys.exit(1)
	print "Requesting %s+%s"%(ids, state)
	add_two_ints_client(ids, state, dimming)
