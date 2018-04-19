import os
from capirca_rcmo import capirca_rcmo_wrapper
with open("./malicious_ips","rb") as f:
    malicious_ip=f.read()

wrap=capirca_rcmo_wrapper(malicious_ip,"")
os.system("python aclgen.py")