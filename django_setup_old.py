#!/usr/bin/python
# Script to set up basic Django structure

import subprocess
import os


def get_subprocess(cmdList):

    ps1 = subprocess.Popen(cmd, executable='bash', shell=False,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    return ps1.communicate()[0]

def main():

    ps1 = subprocess.Popen(
          ['which', 'virtualenvwrapper.sh'], shell=False,
          stdout=subprocess.PIPE)

    pathStr = ps1.communicate()[0]

    pathStr = pathStr.decode('ascii').strip()

    cmdStr = 'source ' + pathStr

    ps1 = subprocess.Popen(['which', 'python3'], shell=False,
                           stdout=subprocess.PIPE)
    print (ps1)
    pyStr = ps1.communicate()[0]

    pyStr = pyStr.decode('ascii').strip()

    cmdStr = cmdStr + ' && mkvirtualenv --python=' + pyStr + \
                      ' %s --no-site-packages'%('testname')

    print (cmdStr)

    head = subprocess.Popen(
           cmdStr, shell=True,
           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    test1 = head.communicate()[0]
    print (test1.decode('ascii'))
    for line in head.stdout.readlines():
            print (line)

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
