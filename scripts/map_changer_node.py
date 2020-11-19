#!/usr/bin/python

import rospy
import rospkg
from node_handler import *
from map_sample.srv import *

class map_changer:
    def __init__(self):
        rospy.init_node('map_changer')
        self.r = rospkg.RosPack()
        self.path = self.r.get_path('map_sample')
        self.srv_server_handler = rospy.Service('~change_map', MapChange, self.service_callback)
    
    def service_callback(self, req):
        rospy.loginfo('receive id:%d' % req.id)
        resp = MapChangeResponse()
        if req.id in {0,1}:
            kill_node('map_server')
            kill_node('pcd_to_pointcloud')
            if req.id == 0:
               call_node('map_server','map_server',args=[self.path + '/maps' + '/1F_2d/map0.yaml'])
               call_node('pcl_ros','pcd_to_pointcloud',args=[self.path + '/maps' + '/1F_3d/cloudGlobal.pcd','_latch:=true','_frame_id:=map','/cloud_pcd:=/mapcloud'])
               resp.message = '1F_2d loaded'
            if req.id == 1:
               call_node('map_server','map_server',args=[self.path + '/maps' + '/18F_2d/map0.yaml'])
               call_node('pcl_ros','pcd_to_pointcloud',args=[self.path + '/maps' + '/18F_3d/cloudGlobal.pcd','_latch:=true','_frame_id:=map','/cloud_pcd:=/mapcloud'])
               resp.message = '1F_18d loaded'
        else:
            resp.success = False
            resp.message = 'out of range ID'
            return resp

        resp.success = True
        return resp

if __name__ == "__main__":

    try:
        mc = map_changer()
        rospy.spin()
    except rospy.ROSInterruptException: pass