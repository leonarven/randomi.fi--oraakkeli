import pycurl, sys

class Oraakkeli:
	def __init__(self):
		self.get = ""
		self.send = ""

	def _initCurl(self):
		self.responseData = ""
		self.curl = pycurl.Curl()
		self.curl.setopt(pycurl.USERAGENT,'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.102011-10-16 20:23:50')
		self.curl.setopt(pycurl.TIMEOUT, 5)
		self.curl.setopt(pycurl.SSL_VERIFYHOST, 0)
		self.curl.setopt(pycurl.SSL_VERIFYPEER, False)
		self.curl.setopt(pycurl.WRITEFUNCTION, self._response)

	def _response(self, data):
		self.responseData = data

	def getMsg(self, msg):
		try:
			self._initCurl()
			self.curl.setopt(pycurl.URL, "http://leonarven.info/code/randomi.fi/oraakkeli.php?q="+msg)
			self.curl.perform()
			self.curl.close()
			return self.responseData
		except:
			print "Error Curl"

if __name__ == "__main__":
	import time
	c = Oraakkeli()
	if len(sys.argv) == 2: 
		print c.getMsg(sys.argv[1])
	else: 
		print "Anna kysymys!"
