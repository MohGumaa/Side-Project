#! python3
# pw.py - An insecure password locker program.

PASSWORD = {'email': 'kljaglajlgjaghakj21',
            'facebook': 'gk2k332@#4322lk23',
            'twitter': 'nvnxv,x#@#42sfl'
}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
