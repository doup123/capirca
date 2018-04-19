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


def create_network(source_ip,destination_ip):
    fname="def/NETWORK.net"
    ips= {
        "source_ip":source_ip,
        "destination_ip":destination_ip
    }
    with open(fname, 'w') as f:
        networking = render_template('ddos_ip_sources', ips)
        f.write(networking)

def create_access_control():
    fname = "policies/pol/victim.pol"
    services = "HTTP_SLOWLORIS"
    context = {
        'service': services
    }
    #
    with open(fname, 'w') as f:
        access_list = render_template('victim.pol', context)
        f.write(access_list)

def capirca_rcmo_wrapper(src_ip,dst_ip):
    # src_ip=sys.argv[1]
    # dst_ip=sys.argv[2]
    create_network(src_ip,dst_ip)
    create_access_control()

########################################

