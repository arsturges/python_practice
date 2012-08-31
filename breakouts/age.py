#!/usr/bin/env python
import datetime
date_of_birth = datetime.datetime(1983,06,26)
print("date_of_birth:",date_of_birth.ctime())
now = datetime.datetime.now()
print("now:",now.ctime())
duration_of_life = now - date_of_birth
print("duration_of_life:", duration_of_life)
print("Days alive:", duration_of_life.days)
print("Hours alive:", duration_of_life.days*24)
