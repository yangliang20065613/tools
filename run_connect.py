#!/usr/bin/python

import sys
import os
import commands
import shutil
import signal
import time

def main():

    for i in range(1,25):
        cmd = "sudo nvme connect -t rdma -a 192.168.219.3 -s 4521 -n nqn.2016-06.io.spdk:cnode" + str(i)
#        cmd = "sudo nvme disconnect -d /dev/nvme" + str(i) + "n1"
        os.system(cmd)


if __name__  == '__main__':
    main()
