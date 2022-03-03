# -*- coding: iso-8859-1 -*-
import subprocess, sys

p = subprocess.Popen(["powershell.exe",
              "[System.IO.Ports.SerialPort]::getportnames()"],
              stdout=sys.stdout)
masno = p.communicate()

