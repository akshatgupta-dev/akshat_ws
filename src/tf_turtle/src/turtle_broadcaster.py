#! /usr/bin/python3

import rospy
from turtlesim.msg import Pose
import tf2_ros
from geometry_msgs.msg import TransformStamped
import tf_conversions

def callback(msg, turtle_name):
    broadcaster = tf2_ros.StaticTransformBroadcaster()
    t = TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = turtle_name
    t.transform.translation.x = msg.x
    t.transform.translation.y = msg.y
    t.transform.translation.z = 0.0
    
    quaternions = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t.transform.rotation.x = quaternions[0]
    t.transform.rotation.y = quaternions[1]
    t.transform.rotation.z = quaternions[2]
    t.transform.rotation.w = quaternions[3]
    broadcaster.sendTransform(t)
    
    

if __name__ == '__main__':
    
    rospy.init_node(f'broadcaster')
    turtle_name = rospy.get_param('~turtle')
    rospy.Subscriber(f'/{turtle_name}/pose', 
                     Pose, 
                     callback, 
                     turtle_name)
    rospy.spin()