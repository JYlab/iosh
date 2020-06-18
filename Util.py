#-*- coding: utf-8 -*-

import os, sys
import subprocess

class Util(object):

    def rename(self, src, changed):
        rename = "mv {src} {changed}".format(src=src, changed=changed)
        subprocess.call ( rename , shell=True)

    def make_substrate_plist(self, plist_path):
        plist_value = "{ Filter = { Bundles = (\"com.apple.UIKit\",); }; }"
        with open(plist_path, "w") as f:
            f.write(plist_value)

    def make_target_plist(self, plist_path, target_name):
        
        plist_value = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>{target_name}</key>
	<true/>
	<key>enabled</key>
	<true/>
    </dict>
</plist>""".format(target_name=target_name)

        with open(plist_path, "w") as f:
            f.write(plist_value)
        
