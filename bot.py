#-*- coding: UTF-8 -*-
import connection
import oraakkeli
import time
import atexit

class Botti:
	def __init__(self):
		self.chat = connection.Connection()
		self.oraakkeli = oraakkeli.Oraakkeli()
		self.chat.errorCount = 0
		self.lastMessage = 0
		self.marksPerMinute = 430.0

	def initChat(self):
		self.chat.setUserId("0")
		self.chat.setStrangerId("0")

		print time.strftime("%X")+" <@bot> #####################################"
		print time.strftime("%X")+" <@bot> "+str(self.chat.getNumberOfOnlineUsers())+" users online"
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

	def startConversation(self):
		say(self.oraakkeli.getMsg("moi"))
		self.messagesCount	= 0
		self.chat.errorCount	= 0
		self.startTime			= int(time.time())

	def say(self,msg):
		time.sleep((60.0/self.marksPerMinute)*msg.__len__())
		self.chat.sendMsg(msg)
		print time.strftime("%X")+" <+Oracle> "+msg
		self.lastMessage		= int(time.time())
		self.messagesCount	+= 1
		

	def run(self):
		self.startConversation()
		self.messagesCount	= 0
		self.lastMessage		= int(time.time())

		while(self.chat.errorCount < 5):
			self.runningTime = int(time.time()) - self.startTime
			self.chat.listenToReceive()
			msg = self.chat.getReceiveMsg()


			if(msg == "||--noResult--||"):
				print time.strftime("%X")+" <@bot> Stranger leaved"
				print time.strftime("%X")+" <@debug> messagesCount: "+str(self.messagesCount)
				print time.strftime("%X")+" <@debug> lastMessage: "+str(self.lastMessage)
				print time.strftime("%X")+" <@debug> runningTime: "+str(self.runningTime)
				self.initChat()
				self.startConversation()
			elif (msg != ""):
				msg = msg.replace("&auml;", "ä")
				msg = msg.replace("&ouml;", "ö")
				msg = msg.replace("&Auml;", "Ä")
				msg = msg.replace("&Ouml;", "Ö")
				print time.strftime("%X")+" <+Stranger> "+msg
				self.say(self.oraakkeli.getMsg(msg))


			if ((self.lastMessage+20) < int(time.time()) and self.messagesCount != 0):
				say (self.oraakkeli.getMsg("millainen olen?"))


			if ((self.messagesCount == 0 and self.runningTime > 30) or ((self.lastMessage+50) < int(time.time()))):
				self.say("Ei sitten, jos niin hiljaista ollaan")
				print time.strftime("%X")+" <@bot> Getting new stranger"
				self.initChat()
				self.startConversation()


			time.sleep(1)
				

if __name__ == "__main__":
	b = Botti()
	b.initChat()
	b.run()
	atexit.register(b.chat.leaveChat())
