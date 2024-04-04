#! /usr/bin/python3

import rospy

rospy.init_node('our_get_private_param')

our_global_param = rospy.get_param('~private_example')
print(our_global_param)
