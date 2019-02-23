# -*- coding: utf-8 -*-

from ogn.client import AprsClient
from ogn.parser import parse, ParseError
from core import Competitor, Task

# Set up Competitors
competitors = []


# create OGN client
client = AprsClient(aprs_user='N0CALL')
client.connect()
