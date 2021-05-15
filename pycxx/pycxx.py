
import os
import ctypes
import json
import subprocess

class loadCtypes:
	def __init__(self,projectName):
		thisFileDir = os.path.dirname(__file__)
		LFile = "{}/cxxprojects/lib/{}".format(thisFileDir,projectName)
		self.cxxfuncs = ctypes.CDLL(LFile)
		self.cxxfuncs.passBytes.astypes = [ctypes.POINTER(ctypes.c_char),ctypes.c_size_t]
		self.cxxfuncs.passBytes.restype = ctypes.POINTER(ctypes.c_char)
		self.cxxfuncs.passBytesSize.restype = ctypes.c_size_t;
		print("LoadCtypes [CxxProject:{}] Successfully ".format(projectName))
	
	
	def bytesIO(self,i):
		ptr = self.cxxfuncs.passBytes(i,len(i))
		return ptr[0:self.cxxfuncs.passBytesSize()]

	def strIO(self,s):
		i = s.encode("utf8")
		o = self.bytesIO(i)
		return o.decode("utf8")

	def jsonIO(self,d):
		i = json.dumps(d)
		o = self.strIO(i)
		return json.loads(o)

	def clear(self):
		self.cxxfuncs.clear()



def compileCtypes(projectName):
	thisFileDir = os.path.dirname(__file__)
	cmds = [
		"g++",
		"-std=c++11",
		"-shared",
		"-fPIC",
		"-O3",
		"-o{}/cxxprojects/lib/{}".format(thisFileDir,projectName),
		"{}/pycxxInterface.cpp".format(thisFileDir),
		"-I{}/".format(thisFileDir),
		"-I{}/cxxprojects/src/{}/".format(thisFileDir,projectName),
		"-DcxxProjects_{}".format(projectName)
	]
	print("CompileCtypes [CxxProject:{}]".format(projectName))
	print("=============================================")
	print(" ".join(cmds))
	print("=============================================")
	print()
	subprocess.run(cmds)



def compilerunCXX(projectName):
	thisFileDir = os.path.dirname(__file__)
	cmds = [
		"g++",
		"-std=c++11",
		"-O3",
		"-o{}/cxxprojects/bin/{}".format(thisFileDir,projectName),
		"{}/pycxxInterface.cpp".format(thisFileDir),
		"-I{}/".format(thisFileDir),
		"-I{}/cxxprojects/src/{}/".format(thisFileDir,projectName),
		"-D__PYCXX_PURECXX_DEBUG__",
		"-DcxxProjects_{}".format(projectName)
	]
	print("compileCXX [CxxProject:{}]".format(projectName))
	print("=============================================")
	print(" ".join(cmds))
	print("=============================================")
	subprocess.run(cmds)
	print("run ...")
	print()
	subprocess.run("{}/cxxprojects/bin/{}".format(thisFileDir,projectName))




def compileCtypesAll():
	thisFileDir = os.path.dirname(__file__)
	for name in os.listdir("{}/cxxprojects/src/".format(thisFileDir)):
		if os.path.isfile(name) == False:
			try:
				compileCtypes(name)
			except Exception as e:
				print(e)


	