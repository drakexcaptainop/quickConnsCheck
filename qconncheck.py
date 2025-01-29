import psutil
import ipinfo

handler = ipinfo.getHandler("" )
def get_ip_info(ip):
    details = handler.getDetails(ip)
    return {
        'Org': details.all.get('org', None),
        'Host': details.all.get('hostname',None),
        'Country': details.all.get('country_name', None),
        'Loc': details.all.get('loc', None)
    }



def get_netstat_info():
    connections = []
    
    for conn in psutil.net_connections(kind='inet'):
       # laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else None
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else None
       # pid = conn.pid if conn.pid else "N/A"
        #status = conn.status
        if raddr != None:
            if (w:=get_ip_info(raddr.split(':')[0])):
                print('\n'.join( f'{k}:{v}' for k,v in w.items()))
                print('\n')


        
        

get_netstat_info()
