#####################################################
##  Content rewriting script for mitmproxy 4
##  Other versions of mitmproxy may not be compatible
#####################################################
#
# BEGIN LICENSE #
#
# CERT Tapioca
#
# Copyright 2018 Carnegie Mellon University. All Rights Reserved.
#
# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
# ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
# CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER
# EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED
# TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY,
# OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON
# UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO
# FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#
# Released under a BSD (SEI)-style license, please see license.txt or
# contact permission@sei.cmu.edu for full terms.
#
# [DISTRIBUTION STATEMENT A] This material has been approved for
# public release and unlimited distribution.  Please see Copyright
# notice for non-US Government use and distribution.
# CERT(R) is registered in the U.S. Patent and Trademark Office by
# Carnegie Mellon University.
#
# DM18-0637
#
# END LICENSE #

from mitmproxy import http

req_before = 'Content to find in intercepted requests'
req_after = 'Content to replace the above with'
resp_before = 'Content to find in intercepted responses'
resp_after = 'Content to replace the above with'

def response(flow: http.HTTPFlow) -> None:
    flow.response.replace(resp_before, resp_after)

def request(flow: http.HTTPFlow) -> None:
    flow.request.replace(req_before, req_after)
