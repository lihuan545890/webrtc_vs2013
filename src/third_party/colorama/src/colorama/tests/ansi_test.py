# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
import sys
try:
    from unittest2 import TestCase, main
except ImportError:
    from unittest import TestCase, main

from ..ansi import Fore, Back, Style
from ..ansitowin32 import AnsiToWin32


stdout_orig = sys.stdout
stderr_orig = sys.stderr


class AnsiTest(TestCase):
    
    def setUp(self):
        # sanity check: stdout should be a file or StringIO object.
        # It will only be AnsiToWin32 if init() has previously wrapped it
        self.assertNotEqual(type(sys.stdout), AnsiToWin32)
        self.assertNotEqual(type(sys.stderr), AnsiToWin32)

    def tearDown(self):
        sys.stdout = stdout_orig
        sys.stderr = stderr_orig


    def testForeAttributes(self):
        self.assertEqual(Fore.BLACK, '\033[30m')
        self.assertEqual(Fore.RED, '\033[31m')
        self.assertEqual(Fore.GREEN, '\033[32m')
        self.assertEqual(Fore.YELLOW, '\033[33m')
        self.assertEqual(Fore.BLUE, '\033[34m')
        self.assertEqual(Fore.MAGENTA, '\033[35m')
        self.assertEqual(Fore.CYAN, '\033[36m')
        self.assertEqual(Fore.WHITE, '\033[37m')
        self.assertEqual(Fore.RESET, '\033[39m')


    def testBackAttributes(self):
        self.assertEqual(Back.BLACK, '\033[40m')
        self.assertEqual(Back.RED, '\033[41m')
        self.assertEqual(Back.GREEN, '\033[42m')
        self.assertEqual(Back.YELLOW, '\033[43m')
        self.assertEqual(Back.BLUE, '\033[44m')
        self.assertEqual(Back.MAGENTA, '\033[45m')
        self.assertEqual(Back.CYAN, '\033[46m')
        self.assertEqual(Back.WHITE, '\033[47m')
        self.assertEqual(Back.RESET, '\033[49m')


    def testStyleAttributes(self):
        self.assertEqual(Style.DIM, '\033[2m')
        self.assertEqual(Style.NORMAL, '\033[22m')
        self.assertEqual(Style.BRIGHT, '\033[1m')


if __name__ == '__main__':
    main()

