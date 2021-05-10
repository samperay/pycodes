# find out the valid ip address.

# "1.2.3.4" => True
# "1.2.3" => False
# "1.2.3.4.5" => False
# "123.45.67.89" => True
# "123.456.78.90" => False
# "123.045.067.089" => False

ips = ["1.2.3.4", "1.2.3", "1.2.3.4.5", "123.45.67.89", "123.456.78.90", "123.045.067.089"]
valid_ip=[]
for ip in ips:
    n4=ip.split('.')
    # condition to check for length
    if len(n4) ==4:
        valid_count=0
        for n in n4:
            if n[0] != '0' and int(n) < 256:
                valid_count+=1
        if valid_count == 4:
            valid_ip.append(ip)
print(valid_ip)
