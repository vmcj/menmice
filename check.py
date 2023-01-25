#import iscpy
import json

conf = None
servicenow = None

storage = {}
devices = {}

cidevices = {}

with open('host_entries.txt','r') as f:
    for l in [x.strip('\n').split() for x in f.readlines()]:
        try:
            cl = l[1]
            mac = ':'.join(l[2].strip(';').split(':')[1:]).upper()
        except ValueError as e:
            print(l, e)
            exit()
        try:
            storage[cl].add(mac)
        except KeyError:
            storage[cl] = set([mac])
        try:
            devices[mac].add(cl)
        except KeyError:
            devices[mac] = set([cl])

# Here we can actually do proper parsing
#with open('proper_entries.txt','r') as f:
#    for l in [x.strip('\n').split() for x in f.readlines()]:
#        try:
#            mac = ':'.join(l[2].strip(';').split(':')[1:]).upper()
#        except ValueError as e:
#            print(l, e)
#            exit()
#        try:
#            storage[cl].add(mac)
#        except KeyError:
#            storage[cl] = set([mac])
#        try:
#            devices[mac].add(cl)
#        except KeyError:
#            devices[mac] = set([cl])

for k,v in storage.items():
    print(k,len(v))

for k,v in devices.items():
    if len(v)==1:
        continue
    print(k,len(v))

with open('cmdb_ci.json','r') as f:
    servicenow = json.load(f)['records']

for item in servicenow:
    mac = item['mac_address'].upper()
    cidevices[mac] = mac in devices.keys()

print(len([item for item in cidevices.keys() if item]))
print(len([item for item in cidevices.keys() if not item]))
print(len(set(devices.keys())-set(cidevices.keys())))
print(len(set(devices.keys()).intersection(set(cidevices.keys()))))

#print(json.dumps(servicenow[0], indent=2))
#print(servicenow.keys())

#print(storage)
#print(devices)
exit()
print(iscpy.ParseISCString(conf))

with open('dhcpd.conf','r') as f:
    conf = f.read()
    #iscpy.ParseISCString(f.read())

print(iscpy.ParseISCString(conf))
