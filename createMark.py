#!/usr/bin/env python3

import dbm
import os

file = dbm.open("account", 'c')
file['root'] = 'password=wozuishuai;access=CustomNavigate];'
file.close()

if not os.path.exists('accountDataCollect'):
    os.mkdir('./accountDataCollect')
    pass
