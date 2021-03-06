#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.BaseIotData import BaseIotData

class SystemPerformanceData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 0.0
	
	def __init__(self, d = None):
		super(SystemPerformanceData, self).__init__(d = d)
		pass
	
	def getCpuUtilization(self):
		pass
	
	def getDiskUtilization(self):
		pass
	
	def getMemoryUtilization(self):
		pass
	
	def setCpuUtilization(self, cpuUtil):
		pass
	
	def setDiskUtilization(self, diskUtil):
		pass
	
	def setMemoryUtilization(self, memUtil):
		pass
	
	def _handleUpdateData(self, data):
		pass
