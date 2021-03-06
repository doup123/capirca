import os
import sys
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_access_control(ip):
    fname = "policies/pol/"+str(ip)+".pol"
    services = {"SSH":{"source":"172.16.85.128","dest":""}}
    context = {
        'services': services
    }
    #
    with open(fname, 'w') as f:
        access_list = render_template('test.pol', context)
        f.write(access_list)

def create_network(source_ip,destination_ip):
    fname="def/NETWORK.net"
    ips= {
        "source_ip":source_ip,
        "destination_ip":destination_ip
    }
    with open(fname, 'w') as f:
        networking = render_template('NETWORK.net.jinja', ips)
        f.write(networking)
def main():
    src_ip=sys.argv[1]
    dst_ip=sys.argv[2]
    create_network(src_ip,dst_ip)
    create_access_control(dst_ip)

########################################

if __name__ == "__main__":
    main()