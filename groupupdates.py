#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:03:54 2020

@author: Andres
"""

#!/usr/bin/env python
import os
import datetime
import shutil
import send2trash

dt = str(datetime.datetime.now())

Students = []

Students = ['Wade', 'Suzanne', 'Sanjeev', 'Coleman', 'Parisa', 'Sanjeev', 'Kimmie', 'Emmy', 'RAS', 'JZ']

path = "/Users/Andres/Box Sync/Group_Updates"
archive = "/Users/Andres/Box Sync/Archive"

for x in Students:
        if os.path.isfile(path + '/' + 'Last_Weeks_Updates' + '/' + x + '.pdf'):     
            shutil.copy(path + '/' + 'Last_Weeks_Updates' + '/' + x + '.pdf', archive + '/' + x + '/' + x + '.pdf')
            newname = archive + '/' + x + '/' + x + dt + '.pdf'
            os.rename(archive + '/' + x + '/' + x + '.pdf', newname)
            send2trash.send2trash(path + '/' + 'Last_Weeks_Updates' + '/' + x + '.pdf')        
    
        if os.path.isfile(path + '/' + x + '.pdf'):  
            shutil.copy(path + '/' + x + '.pdf', path + '/' + 'Last_Weeks_Updates' + '/' + x + '.pdf')
            send2trash.send2trash(path + '/' + x + '.pdf')           
            
