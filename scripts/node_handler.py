#!/usr/bin/python

import subprocess

def kill_node(nodename):
    process=subprocess.Popen(['rosnode','list'],stdout=subprocess.PIPE)
    process.wait()
    nodelist=process.communicate()[0].split("\n")

    for i in range(len(nodelist)):
        tmp = nodelist[i]

        if nodename in tmp:
            subprocess.call(['rosnode','kill',nodelist[i]])
            break

def call_node(pkgname,nodename,args=[]):
    command = ['rosrun',pkgname,nodename]
    command.extend(args)
    process = subprocess.Popen(command)

def call_launch(pkgname,launchname,args=[]):
    command = ['roslaunch',pkgname,launchname]
    command.extend(args)
    process = subprocess.Popen(command)

if __name__ == "__main__":
    #call_node('rviz','rviz',args=['-h'])
    #kill_node('rosout')
    pass
    