#-*- coding: utf-8 -*-

import os, sys
import argparse
import socket, struct
import random, string
import hashlib, binascii, time
import json
from Util import *

class Operator(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def send_message(self, packet):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip , self.port))
        print("connected")

        s.send(packet)
        print("packet : ")
        print(packet)
        
        recv = s.recv(4)
        print("recv data : %s" % recv)


    def memory_write(self, opcode, offset, change):
        # 1 + 8 + 8 => sizeof(opcode) + sizeof(offset) + sizeof(change) 
        packet_size = 17

        packet = struct.pack("<BBQQ", packet_size, opcode, int(offset, 16), int(change, 16) )
        self.send_message(packet)


    def memory_scan(self, opcode, target, resetFlag):
        # 1 + 8 + 1 => sizeof(opcode) + sizeof(target) + sizeof(resetFlag) 
        packet_size = 10

        # print("opcode :" + opcode )
        # print("target :" + target )
        # print("resetFlag :" + resetFlag )

        packet = struct.pack("<BBQB", packet_size, opcode, int(target, 16), int(resetFlag, 16) )
        self.send_message(packet)


    def memory_write_by_raw(self, opcode, raw_address, change):
        # 1 + 8 + 8 => sizeof(opcode) + sizeof(raw_address) + sizeof(change) 
        packet_size = 17

        packet = struct.pack("<BBQQ", packet_size, opcode, int(raw_address, 16), int(change, 16) )
        self.send_message(packet)
    

    def doProcess(self, operation):

        # operation.data1 : offset
        # operation.data2 : payload
        if operation.opcode == 'memory_write' and (operation.data1 != None) and (operation.data2 != None):
            print("call memory_write")
            opcode = 0
            self.memory_write(opcode, operation.data1, operation.data2)

        # operation.data1 : The data we're looking for
        if operation.opcode == 'memory_scan' and (operation.data1 != None) and (operation.data2 != None):
            opcode = 1
            print("call memory_scan")
            self.memory_scan(opcode, operation.data1, operation.data2)

        # operation.data1 : raw_address (get it to "memory_scan" operation)
        # operation.data2 : payload
        if operation.opcode == 'memory_write_by_raw' and (operation.data1 != None) and (operation.data2 != None):
            print("call memory_write_by_raw")
            opcode = 2
            self.memory_write_by_raw(opcode, operation.data1, operation.data2)