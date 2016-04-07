s = raw_input()
n,m = s.split(' ')
n = int(n)
m = int(m)
rules = []
ips = []
allow_rules = []
deny_rules = []
for i in range(n):
    rule = raw_input()
    rules.append(rule)
for j in range(m):
    ip = raw_input()
    ips.append(ip)


def handle_rule(rawrules):
    for z in rawrules:
        tmp = z.split(' ')
        if tmp[0] == 'allow':
            ma = handle_netmask(tmp[1])
            ipt = handle_ip(tmp[1])
            if ma == 0:
                result = ipt
            else:
                result = ipt[0:ma]
            allow_rules.append(result)
        elif tmp[0] == 'deny':
            ma = handle_netmask(tmp[1])
            ipt = handle_ip(tmp[1])
            if ma == 0:
                result = ipt
            else:
                result = ipt[0:ma]
            deny_rules.append(result)

def handle_netmask(ru):
    t = ru.split('/')
    if len(t) == 2:
        return int(t[1])
    else:
        return 0

def handle_ip(Ip):
    Ip_list = Ip.split('/')
    Ip_l = Ip_list[0].split('.')
    Ip_bin = ''
    for h in Ip_l:
        htmp = int(h)
        ss = bin(htmp)[2:].zfill(8)
        Ip_bin += ss
    return Ip_bin


def main():
    handle_rule(rules)
    for p in ips:
        flag = 0
        # p = handle_ip(p)
        # for k in allow_rules:
        #     com = p[0:len(k)]
        #     if com == k:
        #         print 'YES'

        for x in deny_rules:
            cc = handle_ip(p)[0:len(x)]
            if cc == x:
                flag = 1
                break
        if flag == 1:
            print 'NO'
        else:
            print 'YES'

if __name__ == '__main__':
    main()
