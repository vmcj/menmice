grep subclass dhcpd.conf | grep -v 'subclass "vendor-classes"' > host_entries.txt
grep "hardware ethernet" dhcpd.conf > proper_entries.txt
