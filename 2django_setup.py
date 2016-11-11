#!/usr/bin/python
# Script to set up basic Django structure

import subprocess
import os
import django

def get_subprocess(cmd):

    ps = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)

    return ps.communicate()[0]

    psid = ps.pid

    os.kill(psid, 9)


def get_venv(case):

    return {
        0: 'development',
        1: 'testing',
        2: 'production',
        3: 'staging',
    }.get(case, 0)


def main():

    tempStr = 'taskbuster2'

    rootStr = tempStr + '_project'

    pathStr = get_subprocess(['which', 'virtualenvwrapper.sh'])

    pathStr = pathStr.decode('ascii').strip()

    prefixStr = 'source ' + pathStr

    pyStr = get_subprocess(['which', 'python3'])

    pyStr = pyStr.decode('ascii').strip()

    for venv in range(4):

        projectStr = 've_' + get_venv(venv)[:3]

        cmdStr = prefixStr + ' && mkvirtualenv --python=' + pyStr + \
                             ' %s --no-site-packages' % (projectStr)

        print ('Final cmd: ', cmdStr)

        venvStr = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)

        print (venvStr.communicate()[0])

        get_subprocess(['workon', projectStr])

        get_subprocess(['pip', 'install', pathStr])

        get_subprocess(['deactivate'])


        os.chdir('/Users/GSW/Documents/Sites/')

    get_subprocess(['mkdir', rootStr])

    os.chdir(rootStr)

    get_subprocess(['mkdir', 'functional_tests'])

    get_subprocess(['touch', 'functional_tests/tests_all_users.py'])

    get_subprocess(['django-admin.py', 'startproject', tempStr])

    get_subprocess(['mv', tempStr + '/manage.py', 'manage.py'])

    get_subprocess(['mv', tempStr + '/' + tempStr + '/settings.py',
                    './' + tempStr + '/settings.py'])

    get_subprocess(['mv', tempStr + '/' + tempStr + '/urls.py',
                    './' + tempStr + '/urls.py'])

    get_subprocess(['mv', tempStr + '/' + tempStr + '/wsgi.py',
                    './' + tempStr + '/wsgi.py'])

    get_subprocess(['mv', tempStr + '/' + tempStr + '/__init__.py',
                    './' + tempStr + '/__init__.py'])

    get_subprocess(['rm', '-r', tempStr + '/' + tempStr])

    get_subprocess(['mkdir', 'requirements'])

    get_subprocess(['touch', 'requirements/base.txt'])

    f_settings = open('requirements/base.txt', 'a')

    f_settings.write('Django==' + django.get_version())

    f_settings.write('selenium==2.48.0')

    f_settings.flush()

    f_settings.close()

    for venv in range(4):

        pathStr = 'requirements/' + get_venv(venv) + '.txt'

        get_subprocess(['touch', pathStr])

        ps = subprocess.Popen(['echo', '-r base.txt'], shell=False,
                              stdout=subprocess.PIPE)

        output = subprocess.Popen(['tee', '-a', pathStr], shell=False,
                                  stdin=ps.stdout)

        ps.wait()

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
