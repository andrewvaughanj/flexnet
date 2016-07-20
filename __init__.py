#!/usr/bin/env python

""" License utility for FlexNet-based license managers"""

import sys
import flexnet.client
import flexnet.file

def get_license_file(srv):
    c = flexnet.client.FlexNetClient(srv)
    c.connect()
    c.hello()
    c.query_license_file_contents()
    return c.server_params["license_file_text"]

def main(args):
    if len(args) == 2:
        port_at_server = args[1]
        c = flexnet.client.ManagerClient(port_at_server)
        #c.verbose = True
        c.report_everything()

if __name__ == "__main__":
    main(sys.argv)
