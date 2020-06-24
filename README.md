## [iOSH]

Dynamic iOS Hacking tool

## [How To Use]

### [+]Inject Agent first
python3 iosh.py --ip=[jailbroken iPhone IP]  --package=[target's package name]

### [+]Select Operation
#### 1. memory_write
- python3 iosh.py --ip=[jailbroken iPhone IP] --operation=="memory_write" --data1=[target's offset] --data2=[change data (4byte) ] 
- TODO: I will patch it so that I can specify the data2 size
- Sample Screenshot [https://github.com/JYlab/iosh/tree/master/screenshot/memory_write]

#### 2. memory_scan (like 'cheat engine') : TODO


#### 3. TODO TODO!  :)
