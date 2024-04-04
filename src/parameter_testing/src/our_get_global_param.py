#! /usr/bin/python3

import rospy

rospy.init_node('our_set_global_param.py')

our_global_param = rospy.get_param('/this_is_global_starts_with_slash', 'started from rospy')
print(our_global_param)