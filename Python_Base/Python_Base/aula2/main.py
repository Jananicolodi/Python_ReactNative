from Email import Email #ok
from Sistema import Sistema #ok
from Idade import Idade #ok
from Par import Par #ok

import platform
import sys
import glob

for f in glob.glob("*.*"):
    print(f)
p = Par(len(f))

e = Email("naa@gmail.com")
e = Email("a@b.com")
i = Idade([1,2,3,40,50])

s = Sistema(platform.machine())

