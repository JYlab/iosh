#-*- coding: utf-8 -*-
import os, sys
import argparse
import socket, struct
import random, string
import hashlib, binascii, time
import json

from Operator import *
from Util import *
from Injector import *

PORT = 36003

class OPCode(object):
    def __init__(self, op, data1, data2):
        self.opcode = op
        self.data1 = data1
        self.data2 = data2

# I Will convert to GUI TOOL
class Iosh(object):
    def __init__(self, args, op):
        self.util = Util()
        self.AGENT_NAME = "./iosh_agent.dylib"
        self.PLIST_NAME = "./iosh_agent.plist"
        self.TARGET_PLIST_NAME = "./iosh_target.plist"
        self.args = args
        self.op = op

    def inject_agent(self):
        self.util.make_substrate_plist(self.PLIST_NAME)
        self.util.make_target_plist(self.TARGET_PLIST_NAME, self.args.package)
        self.injector = Injector(self.AGENT_NAME, self.PLIST_NAME ,self.TARGET_PLIST_NAME, self.args.ip, "root", "alpine")
        self.injector.inject()

    def operate(self):
        operator = Operator(str(self.args.ip), PORT)
        operator.doProcess(self.op)


if __name__ == '__main__' :
    arg_parser     = argparse.ArgumentParser()
    op_argv_parser = argparse.ArgumentParser()
    arg_parser.operation = None
    op = None
    
    arg_parser.add_argument('--package'   , required=False, help='target package name')
    arg_parser.add_argument('--ip'        , required=True , help='ip address for injection target')
    arg_parser.add_argument('--operation' , required=False, help='Iosh Operation')
    arg_parser.add_argument('--data1'     , required=False, help='data1')
    arg_parser.add_argument('--data2'     , required=False, help='data1')
    args = arg_parser.parse_args()

    if args.operation != None and args.data1 != None and args.data2 != None:
        op = OPCode(args.operation, args.data1, args.data2)
        
    iosh = Iosh(args, op)
    if op == None:
        print("INJECT START")
        iosh.inject_agent()
    else:
        print("OPERATE START")
        iosh.operate()
        

