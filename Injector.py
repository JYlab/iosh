#-*- coding: utf-8 -*-
import os, sys
import subprocess

class Injector(object):
    def __init__(self, dylibPath, plistPath, target_plist,ip, usr, pw):
        self.dylib = dylibPath
        self.plist = plistPath
        self.target_plist = target_plist
        self.ip = ip
        self.usr = usr
        self.pw = pw

    def inject(self):
        # scp = "scp {src} {dst}"
        injectCommand = """expect <<EOF\n 
                        spawn scp -oStrictHostKeyChecking=no -P 22 {dylib} {plist} {target_plist} {usr}@{ip}:/Library/MobileSubstrate/DynamicLibraries/\n 
                        expect \"password:\"\n
                               send \"{pw}\r\"\n 
                        expect eof\n
                        EOF""".format( dylib=self.dylib, plist=self.plist, target_plist=self.target_plist ,usr=self.usr, ip=self.ip, pw=self.pw)

        subprocess.call (injectCommand, shell=True)