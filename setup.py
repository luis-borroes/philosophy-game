from distutils.core import setup
import os, shutil, glob, fnmatch, py2exe, sys

sys.argv.append("py2exe")

if os.path.isdir("Silogismos"):
	shutil.rmtree("Silogismos")

origIsSystemDLL = py2exe.build_exe.isSystemDLL

def isSystemDLL(pathname):
	if os.path.basename(pathname).lower() in ("sdl_ttf.dll", "libfreetype-6.dll", "libogg-0.dll"):
		return False
	return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

dist_dir = os.path.join("Silogismos")
data_dir = dist_dir

class Game:
	name = "Silogismos"
	script = "main.pyw"
	dest_base = "silogismos"
	icon_resources = [(0, os.path.join("assets", "icon.ico"))]

setup(
	options = {"py2exe": {"dist_dir": dist_dir, "optimize": 2, "bundle_files": 1, "compressed": 1, "dll_excludes": ["w9xpopen.exe"]}},
	zipfile = None,
	windows = [Game],
)

data = []
for dirpath, dirnames, filenames in os.walk("assets"):
	data.extend(os.path.join(dirpath, fn) for fn in filenames)

dest = data_dir
for fname in data:
	dname = os.path.join(dest, fname)
	if not os.path.exists(os.path.dirname(dname)):
		os.makedirs(os.path.dirname(dname))
	if not os.path.isdir(fname):
		shutil.copy(fname, dname)
