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
    services = ["SSH","NTP","DNS"]
    context = {
        'services': services
    }
    #
    with open(fname, 'w') as f:
        access_list = render_template('test.pol', context)
        f.write(access_list)

def create_network(destination_ip):
    fname="def/NETWORK.net"
    dst_ip= {
        "destination_ip":destination_ip
    }
    with open(fname, 'w') as f:
        networking = render_template('NETWORK.net.jinja', dst_ip)
        f.write(networking)
def main():
    ip=sys.argv[1]
    create_network(ip)
    create_access_control(ip)

########################################

if __name__ == "__main__":
    main()