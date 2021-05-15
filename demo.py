import os
import sys
import numpy
import json
import pandas as pd

sys.path.append("{}/pycxx/".format(os.path.dirname(__file__)))
import pycxx


if __name__ == '__main__':
	
	

	
	
	pycxx.compileCtypes("passDataFrame")
	passDF = pycxx.loadCtypes("passDataFrame")
	
	#======== Python ========#
	d = {"fruit":["apple",None,"banana"],"number":[1,2,3]}
	df = pd.DataFrame(d)
	j = df.to_json(force_ascii=False,orient='records')
	print(passDF.strIO(j))
	
	
	
	pycxx.compilerunCXX("passDataFrame")
	#============================

	
	