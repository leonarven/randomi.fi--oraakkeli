#-*- coding: UTF-8 -*-
import connection
import oraakkeli
import time

class Botti:
	def __init__(self):
		self.chat = connection.Connection()
		self.oraakkeli = oraakkeli.Oraakkeli()
		self.chat.errorCount = 0
		self.lastMessage = 0

	def initChat(self):
		self.chat.setUserId("0")
		self.chat.setStrangerId("0")

		print time.strftime("%X")+" <@bot> Get userId..."
		while(self.chat.getUserId() == "0"):
			self.chat.startChat()
			time.sleep(1)
		print time.strftime("%X")+" <@bot> UserId: "+str(self.chat.getUserId())

		print time.strftime("%X")+" <@bot> Get strangerId..."
		while(self.chat.getStrangerId() == "0"):
			self.chat.randomChat()
			time.sleep(1)
		print time.strftime("%X")+" <@bot> StrangerId: "+str(self.chat.getStrangerId())

		self.chat.receiveMsg = ""
		self.startTime = int(time.clock())

	def startConversation(self):
		responseMsg = self.oraakkeli.getMsg("moi")
		self.chat.sendMsg(responseMsg)
		print time.strftime("%X")+" <+Oracle> "+responseMsg
		self.chat.errorCount = 0
		self.lastMessage = int(time.clock())

	def run(self):
		self.startConversation()
		self.runningTime = int(time.clock()) - self.startTime
		while(self.chat.errorCount < 5):
			self.chat.listenToReceive()
			msg = self.chat.getReceiveMsg()
			msg = msg.replace("&auml;", "ä")
			msg = msg.replace("&ouml;", "ö")
			msg = msg.replace("&Auml;", "Ä")
			msg = msg.replace("&Ouml;", "Ö")
			if(msg == "||--noResult--||"):
				print time.strftime("%X")+" <@bot> Stranger leaved"
				self.initChat()
				self.startConversation()
			elif (msg != ""):
				responseMsg = self.oraakkeli.getMsg(msg)
				self.chat.sendMsg(responseMsg)
				print time.strftime("%X")+" <+Stranger> "+msg
				print time.strftime("%X")+" <+Oracle> "+responseMsg
				self.chat.errorCount = 0
				self.lastMessage = int(time.clock())

			if (int(time.clock())-self.lastMessage) > 30:
				responseMsg = "Ei sitten, jos niin hiljaista ollaan";
				self.chat.sendMsg(responseMsg)
				print time.strftime("%X")+" <+Oracle> "+responseMsg
				print time.strftime("%X")+" <@bot> Getting new stranger"
				self.initChat()

			time.sleep(1)
				

if __name__ == "__main__":
	b = Botti()
	b.initChat()
	b.run()
