#!/usr/bin/python

import sys
import os
import commands
import shutil
import signal
import time

def main():

    for j in range(15, 39):
        cmd1 = "sudo parted -s /dev/nvme" + str(j) + "n1 mklabel gpt"
        os.system(cmd1)
#        print(cmd1)
        for i in range(1,129):
#        cmd = "sudo nvme connect -t rdma -a 192.168.219.3 -s 4520 -n nqn.2016-06.io.spdk:cnode" + str(i)
            cmd = "sudo parted -s /dev/nvme" + str(j) + "n1 mkpart extended " + str(i) + "MB " + str(i + 1) + "MB"
#            print(cmd)
            os.system(cmd)


if __name__  == '__main__':
    main()
