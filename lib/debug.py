#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.server import Server 
from models.user import User
import ipdb

User.create("ffffffffff","fffffffffffff")
ipdb.set_trace()
