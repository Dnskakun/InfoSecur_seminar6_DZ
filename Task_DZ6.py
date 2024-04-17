import nmap
import pprint

check_ip = input('Введите ip-адрес, на котором требуется проверить открытые порты: ')

nm = nmap.PortScanner()
scan_result = nm.scan(check_ip, arguments = '-sO')
state_value = ''
name_value = ''

print('%2s %16s %15s' % ('PROTOCOL', 'STATE', 'SERVICE'))
for item in scan_result['scan'][check_ip]['ip'].items():
    for subitem in item[1]:
        if subitem == 'state': state_value = item[1][subitem]
        if subitem == 'name': name_value = item[1][subitem]
    #print(f'{item[0]}{name_value}{state_value}')
    print('%4d %20s %15s' % (item[0], state_value, name_value))


