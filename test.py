import pandas as pd
from sklearn.decomposition import PCA

data = '<782>Jun 23 16:13:58 WAF_2 WAG: SerialNum=0123201707109999 GenTime=""2020-06-23 16:13:58"" Module=全局访问控制白名单 SrcIP=100.79.160.41 DstIP=10.160.201.37 SrcPort=63889 DstPort=8848 In=tvi1 Out= Action=pass Content=""全局访问控制:  白名单:(负载下联口白名单);"" EvtCount=1 Evt_level=30 Evt_type=安全审计 Evt_log_level=6 Host= Evt_response=0 BeforeNat= Method='

res = {}
for l in data.split(' '):
    c = l.split('=')
    if len(c)==2:
        res[c[0]]=c[1]
print(res['Protocol'])