import connection
import oraakkeli
import time

c = connection.Connection()
o = oraakkeli.Oraakkeli()
c.startChat()
c.randomChat()	
print "outo: "+c.getUserId()
print "sina: "+c.getStrangerId()

c.sendMsg("moro")
c.listenToReceive()
while(c.getReceiveMsg() != "||--noResult--||"):
	c.listenToReceive()
	if (c.getReceiveMsg() != ""):
		print ">>: "+c.getReceiveMsg()
		oraakkeliVastaus = o.getMsg(c.getReceiveMsg())
		time.sleep(1)
		c.sendMsg(oraakkeliVastaus)
		print "<<: "+oraakkeliVastaus
	else:
		time.sleep(1)

