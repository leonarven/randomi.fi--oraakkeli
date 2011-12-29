import pycurl
import oraakkeli

class Connection:
	def __init__(self):
		self.responseData = ""
		self.userId = 0

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


	def getNumberOfOnlineUsers(self):
		try:
			self._initCurl()
			self.curl.setopt(pycurl.URL, "randomi.fi/getNumberOfUsers.php")
			self.curl.perform()
			self.curl.close()
			return self.responseData
		except:
			print "Error Curl: numberOfOnlineUsers"

	def startChat(self):
		try:
			self._initCurl()
			self.curl.setopt(pycurl.URL, "randomi.fi/startChat.php")
			self.curl.perform()
			self.curl.close()
			self.userId = self.responseData
		except:
			print "Error Curl: startChat"		

	def leaveChat(self):
		try:
			self._initCurl()
			self.curl.setopt(pycurl.URL, "randomi.fi/leaveChat.php?userId="+self.userId)
			self.curl.perform()
			self.curl.close()
		except:
			print "Error Curl: leaveChat"

	def randomChat(self):
		try:
			self._initCurl()
			self.curl.setopt(pycurl.URL, "randomi.fi/randomChat.php?userId="+self.userId)
			self.curl.perform()
			self.curl.close()
			self.strangerId = self.responseData
		except:
			print "Error Curl: randomChat"	

	def getStrangerId(self):
		return self.strangerId

	def setStrangerId(self, strangerId):
		self.strangerId = strangerId

	def getUserId(self):
		return self.userId

	def setUserId(self, userId):
		self.userId = userId

	def listenToReceive(self):
		try:
			self._initCurl()
			self.curl.setopt(pycurl.URL, "randomi.fi/listenToReceive.php?userId="+self.userId)
			self.curl.perform()
			self.curl.close()
			self.receiveMsg = self.responseData
		except:
			print "Error Curl: listenToReceive"	

	def getReceiveMsg(self):
		return self.receiveMsg

	def sendMsg(self, msg):
		try:
			self._initCurl()
			self.curl.setopt(pycurl.URL, "randomi.fi/sendMsg.php?userId="+self.userId+"&strangerId="+self.strangerId+"&msg="+msg)
			self.curl.perform()
			self.curl.close()
		except:
			print "Error Curl"		

	def typing(self):
		try:
			self._initCurl()
			self.curl.setopt(pycurl.URL, "randomi.fi/typing.php?userId="+self.userId)
			self.curl.perform()
			self.curl.close()
		except:
			print "Error Curl"	

	def stopTyping(self):
		try:
			self._initCurl()
			self.curl.setopt(pycurl.URL, "randomi.fi/stopTyping.php?userId="+self.userId)
			self.curl.perform()
			self.curl.close()
		except:
			print "Error Curl"

	def isStyping(self):
		try:
			self._initCurl()
			self.curl.setopt(pycurl.URL, "randomi.fi/isTyping.php?strangerId="+self.strangerId)
			self.curl.perform()
			self.curl.close()
			self.strangerTyping = self.responseData
		except:
			print "Error Curl"

def test():
	import time
	c = Connection()
	o = oraakkeli.Oraakkeli()
	c.startChat()
	c.randomChat()	
	print c.getUserId()
	print c.getStrangerId()

	c.listenToReceive()
	c.sendMsg("moro")
	while(c.getReceiveMsg() != "||--noResult--||"):
		c.listenToReceive()
		if (c.getReceiveMsg() != ""):
			print "Outo:"+c.getReceiveMsg()
			oraakkeliVastaus = o.getMsg(c.getReceiveMsg())
			print "Sina:"+oraakkeliVastaus
			c.sendMsg(oraakkeliVastaus)
		time.sleep(1)
		

if __name__ == "__main__":
	test()
