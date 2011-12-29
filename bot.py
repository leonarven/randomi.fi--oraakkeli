#-*- coding: UTF-8 -*-
import connection
import oraakkeli
import time

class Botti:
	def __init__(self):
		self.chat = connection.Connection()
		self.oraakkeli = oraakkeli.Oraakkeli()

	def initChat(self):
		self.chat.setUserId("0")
		self.chat.setStrangerId("0")

		print "Get userId..."
		while(self.chat.getUserId() == "0"):
			self.chat.startChat()
			time.sleep(1)
		print "UserId: "+str(self.chat.getUserId())

		print "Get strangerId..."
		while(self.chat.getStrangerId() == "0"):
			self.chat.randomChat()
			time.sleep(1)

		print "StrangerId: "+str(self.chat.getStrangerId())
		self.chat.receiveMsg = ""

		self.startTime = int(time.clock())

	def run(self):
		while(True):
			self.chat.listenToReceive()
			msg = self.chat.getReceiveMsg()
			msg = msg.replace("&auml;", "ä")
			msg = msg.replace("&ouml;", "ö")
			msg = msg.replace("&Auml;", "Ä")
			msg = msg.replace("&Ouml;", "Ö")
			if(msg == "||--noResult--||"):
				print "Stranger leaved"
				self.initChat()
			elif (msg != ""):
				responseMsg = self.oraakkeli.getMsg(msg)
				self.chat.sendMsg(responseMsg)
				print "Stranger: "+msg
				print "You: "+responseMsg

			if self.startTime+60 < int(time.clock()):
				print "Get new stranger"
				self.initChat()

			time.sleep(1)
				

if __name__ == "__main__":
	b = Botti()
	b.initChat()
	b.run()
