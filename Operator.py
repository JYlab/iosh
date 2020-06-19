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
        print("packet :  "+packet)
        
        recv = s.recv(4)
        print("recv data : %s" % recv)


    # TODO
    # opcode : 0x00 
    def memory_write(self, offset, change):
        opcode = 0
        packet_size = 9

        packet = struct.pack(">BBII", packet_size, opcode, int(offset), int(change) )
        self.send_message(packet)
    
    # TODO
    def message_hooking(self, data):
        print("")

    # TODO
    def api_hooking(self, data):
        print("")

    def doProcess(self, operation):
        if operation.opcode == 'memory_write' and (operation.data1 != None) and (operation.data2 != None):
            print("call memory_write")
            self.memory_write(operation.data1, operation.data2)