# -*- coding: utf-8 -*-

from ogn.client import AprsClient
from ogn.parser import parse, ParseError


# create OGN client
client = AprsClient(aprs_user='N0CALL')
client.connect()
