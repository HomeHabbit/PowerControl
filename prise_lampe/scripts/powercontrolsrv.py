#!/usr/bin/env python
 
from prise_lampe.srv import *
import rospy
import commands
 
def handle_add_two_ints(req):
	print "Returning [%s  %s = %s]"%(req.ids, req.state, req.state)
	if req.ids>=0 and req.ids<50000 :
		if req.state == "on" or req.state == "off":
			u=commands.getoutput("/var/www/html/radioEmission 0 %s 17613 %s"%(req.ids,req.state))
			print "lampe %s est mise en position %s"%(req.ids,req.state)
		else:
			print "state incorrect"
	else:
		print "id incorrecte"
	return prise_lampeResponse(req.state)

def add_two_ints_server():
	rospy.init_node('add_two_ints_server')
	s = rospy.Service('add_two_ints', prise_lampe, handle_add_two_ints)
	print "Ready to control lamp"
	rospy.spin()

if __name__ == "__main__":
	add_two_ints_server()
