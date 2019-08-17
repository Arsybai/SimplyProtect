"""Made by arsybai"""
from linepy import LINE, OEPoll, Filters
import sys, requests, json, os

ars = LINE("EHgjs44uMOn2yrF9Tka0.IVHnuwLwofRntI40OTeoma.jv92Tt5Typy9VleiyGLkLztZixF8Oa1dVm4oYR7kYJ4=")
route = OEPoll(ars)
print("logged")

# DATABASE
db = {
	'set':{
	'kick':[],
	'invite':[],
	'update':[]
	},
	'user':[]
}

@route.handler(26, Filters.text & Filters.group)
#use Filters.both for use in privatechat too
def linke_Starto(op):
	msg = op.message
	to = msg.to if msg.toType == 2 else msg._from
	text = msg.text.lower()
	if text == 'hi':ars.reply(msg,'hello')
	if text == 'me':ars.reply(msg,str(msg._from))
	if text == ".exit":ars.sendMessage(to,'Shuting Down...');sys.exit("bye")
	if text == '.reboot':ars.sendMessage(to,'Done Qmack');python = sys.executable;os.execl(python, python, *sys.argv)
	if text == '.set':db['set']['kick'].append(to) if to not in db['set']['kick'] else print('yep');db['set']['invite'].append(to) if to not in db['set']['invite'] else print('yep');db['set']['update'].append(to) if to not in db['set']['update'] else print('yep');ars.reply(msg,'OK')
	if text == '.unset':db['set']['kick'].remove(to) if to in db['set']['kick'] else print('yep');db['set']['invite'].remove(to) if to in db['set']['invite'] else print('yep');db['set']['update'].remove(to) if to in db['set']['update'] else print('yep');ars.reply(msg,'OK')
	

@route.handler(13)
def someoneInvited(op):
	try: ars.acceptGroupInvitation(op.param1)
	except:
		if op.param1 in db['set']['invite']:
			ars.kickoutFromGroup(op.param1,[op.param2]) if op.param2 not in db['user'] else print('Nope')

@route.handler(19)
def someoneKicked(op):
	if op.param2 in db['user']:
		try:ars.kickoutFromGroup(op.param1,[op.param2]);ars.inviteIntoGroup(op.param1,[op.param3])
		except:ars.findAndAddContactByMid(op.param3);ars.inviteIntoGroup(op.param1,[op.param3])
		finally:pass
	if op.param1 in db['set']['kick']:
		try:ars.kickoutFromGroup(op.param1,[op.param2]) if op.param2 not in db['user'] else print('nope');ars.inviteIntoGroup(op.param1,[op.param3])
		except:ars.findAndAddContactByMid(op.param3);ars.inviteIntoGroup(op.param1,[op.param3])
		finally:pass

@route.handler(11)
def updateGroup(op):
	if op.param1 in db['set']['update']:
		try:ars.kickoutFromGroup(op.param1,[op.param2]) if op.param2 not in db['user'] else print('nope');G = ars.getGroup(op.param1);G.preventedJoinByTicket = True;ars.updateGroup(G)
		except:G = ars.getGroup(op.param1);G.preventedJoinByTicket = True;ars.updateGroup(G)
		finally:pass

route.start()
