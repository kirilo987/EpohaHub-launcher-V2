import webview
import modelfetch
import json
import os
import psutil
import humanize
import GPUtil
import platform
from portablemc.standard import Context, Version, Watcher
from pathlib import Path

# Global variables declaration
global lastaccount, firsttime, lastinstance, maximizedefault, winwidth, winheight
global demomode, multiplayer, gamechat, minmem, maxmem, javapath, jvmargs, customtheme, lastuuid

syshost = modelfetch.system.Model

print(r"""
 _   __                       _   __    _    
| | / /                      | | /  |  | |   
| |/ /  __  __  _   _   ___  | | `| |  | | __
|    \  \ \/ / | | | | / __| | |  | |  | |/ /
| |\  \  >  <  | |_| | \__ \ | | _| |_ |   < 
\_| \_/ /_/\_\  \__, | |___/ |_| \___/ |_|\_\
                 __/ |                       
                |___/                        
                                    Beta 1.1 -Launch Update-
                                    by Kxysl1k UwUwUwUwUwUwUwUwU                                  
		""")

def initialize_settings():
    global lastaccount, firsttime, lastinstance, maximizedefault
    global winwidth, winheight, demomode, multiplayer, gamechat, accounts
    global minmem, maxmem, javapath, jvmargs, customtheme, configjson, lastuuid

    config = {
        "lastaccount": "",
        "lastuuid": "",
        "firsttime": 1,
        "maximizedefault": False,
        "winwidth": 854,
        "winheight": 480,
        "demomode": False,
        "nomultiplayer": True,
        "nogamechat": True,
        "minmem": 512,
        "maxmem": 1024,
        "javapath": "javaw",
        "jvmargs": "",
        "customtheme": ""
    }

    accounts = {}

    # File/Folder Checking
    if not os.path.exists(".launcher"):
        print("Папки .launcher не існує, створено її щойно.")
        os.mkdir(".launcher")

    if not os.path.exists(".launcher\\settings.json"):
        print("Папки .launcher не існує, створено її щойно.Папки .launcher не існує, створено її щойно.")
        with open(".launcher\\settings.json", "w") as outfile:
            json.dump(config, outfile, indent=2)

    if not os.path.exists(".launcher\\accounts.json"):
        print("Файл облікових записів може бути відсутнім! `accounts.json` створено.")
        with open(".launcher\\accounts.json", "w") as outfile:
            json.dump(accounts, outfile, indent=2)

    if not os.path.exists(".launcher\\instances.json"):
        print("Файл екземплярів може бути відсутнім! `instances.json` створено.")
        with open(".launcher\\instances.json", "w") as outfile:
            json.dump(accounts, outfile, indent=2)

    if not os.path.exists(".launcher\\lastinstance.txt"):
        print("Останній відкритий файл екземпляра може бути відсутнім! `lastinstance.txt` створено.")
        with open(".launcher\\lastinstance.txt", 'w') as outfile:
            outfile.write('')



    try:
        with open('.launcher\\settings.json', 'r') as openfile:
            configjson = json.load(openfile)
            lastaccount = configjson['lastaccount']
            lastuuid = configjson['lastuuid']
            firsttime = configjson['firsttime']
            maximizedefault = configjson['maximizedefault']
            winwidth = configjson['winwidth']
            winheight = configjson['winheight']
            demomode = configjson['demomode']
            nomultiplayer = configjson['multiplayer']
            nogamechat = configjson['gamechat']
            minmem = configjson['minmem']
            maxmem = configjson['maxmem']
            javapath = configjson['javapath']
            jvmargs = configjson['jvmargs']
            customtheme = configjson['customtheme']
            print("Успішно імпортовано 'settings.json'")
            if lastaccount == "":
                print("Останній використаний обліковий запис: не ввійшли!")
            else:
                print("Останній використаний обліковий запис:", lastaccount)

    except KeyError:
        print("Файл налаштувань не оновлений, тепер файл налаштувань має бути оновлено (скидання інформації)")
        with open(".launcher\\settings.json", "w") as outfile:
            json.dump(config, outfile, indent=2)
        # Initialize global variables after resetting settings
        lastaccount = ""
        lastuuid = ""
        firsttime = 1
        maximizedefault = False
        winwidth = 854
        winheight = 480
        demomode = False
        nomultiplayer = True
        nogamechat = True
        minmem = 512
        maxmem = 1024
        javapath = "javaw"
        jvmargs = ""
        customtheme = ""


    with open('.launcher\\lastinstance.txt', 'r') as openfile:
        global lastinstance
        lastinstance = openfile.read();
        print('Остання версія: ' + lastinstance)



initialize_settings()

class Api:
    def get_host(self):
        print("Системний хост:", syshost)
        return syshost

    def get_username(self, uuid):
        print("UUID облікового запису:", uuid)
        if uuid == 'recent':
            return lastaccount

    def get_last_account(self):
        return lastaccount

    def save_account_change(self, name, uuid):
        print('Збереження деталей облікового запису, у який ви ввійшли.')
        print('Ім`я облікового запису: ' + name)
        print('UUID облікового запису: ' + uuid)
        # my brain hurt

    def get_settings(self):
        return configjson

    def get_mem(self):
        print("Всього RAM:", psutil.virtual_memory().total)
        print("Відформатовано RAM:", humanize.naturalsize(psutil.virtual_memory().total))
        return humanize.naturalsize(psutil.virtual_memory().total)

    def get_gpu(self):
        gpus = GPUtil.getGPUs()
        if not gpus:
            print('GPU не виявлено.')
            return 'Немає виділених графічних процесорів'
        else:
            print('GPU:', gpus[0].name)
            return gpus[0].name

    def get_cpu(self):
        cpu_info = platform.uname()
        print('CPU:', cpu_info.processor)
        return cpu_info.processor

    def write_settings(self, name, data):
        global maximizedefault, winwidth, winheight, demomode, multiplayer, gamechat
        global minmem, maxmem, javapath, jvmargs, customtheme, lastaccount, lastuuid

        if name == 'maximizedefault':
            maximizedefault = data
        elif name == 'lastaccount':
            lastaccount = data
        elif name == 'lastuuid':
            lastuuid = data
        elif name == 'demomode':
            demomode = data
        elif name == 'multiplayer':
            multiplayer = data
        elif name == 'gamechat':
            gamechat = data
        elif name == 'customtheme':
            customtheme = data
        elif name == 'javapath':
            javapath = data
        elif name == 'jvmargs':
            jvmargs = data
        elif name == 'minmem':
            minmem = data
        elif name == 'maxmem':
            maxmem = data
        elif name == 'winwidth':
            winwidth = data
        elif name == 'winheight':
            winheight = data
        print('Налаштування завантаження')

    def save_settings(self):
        print('Збереження налаштувань')
        config = {
            "lastaccount": lastaccount,
            "lastuuid": lastuuid,
            "firsttime": firsttime,
            "maximizedefault": maximizedefault,
            "winwidth": winwidth,
            "winheight": winheight,
            "demomode": demomode,
            "multiplayer": multiplayer,
            "gamechat": gamechat,
            "minmem": minmem,
            "maxmem": maxmem,
            "javapath": javapath,
            "jvmargs": jvmargs,
            "customtheme": customtheme
        }
        print(config)
        with open(".launcher\\settings.json", "w") as outfile:
            json.dump(config, outfile, indent=2)
        print("'settings.json' успішно p,tht;tyj")
        return "'settings.json' Saved Successfully"

    def get_recentinstance(self):
        print("Остання версія:", lastinstance)
        return lastinstance

    def save_recentinstance(self, name):
        global lastinstance

        lastinstance = name
        with open(".launcher\\lastinstance.txt", 'w') as outfile:
            outfile.write(lastinstance)


    # def offline_account(self, Kxysl1k):
    #     print('Offline Username: ' + str(Kxysl1k[0]))
    #     print('Offline UUID: ' + str(Kxysl1k[1]))
    #     print(Kxysl1k)

    # chatgtp wrote this function cuz i struggled with appending offline_account, bruh
    def offline_account(self, username, uuid):
        print('Ім`я користувача офлайн: ' + username)
        print('Offline UUID: ' + uuid)

        offline_account = {
            "username": username,
            "uuid": uuid
        }

        file_path = '.launcher\\accounts.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as openfile:
                try:
                    accountsjson = json.load(openfile)
                    if not isinstance(accountsjson, list):
                        raise ValueError("Дані JSON - це не список")
                except (json.JSONDecodeError, ValueError) as e:
                    print(f"Помилка читання файлу JSON: {e}")
                    accountsjson = []
        else:
            accountsjson = []

        accountsjson.append(offline_account)

        with open(file_path, 'w') as openfile:
            json.dump(accountsjson, openfile, indent=4)

        print("До файлу було додано новий обліковий запис.")

    def get_accounts(self):
        file_path = '.launcher\\accounts.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as openfile:
                return json.load(openfile)
        else:
            print('Не можу отримати облікові записи.json')

    def get_instances(self):
        file_path = '.launcher\\instances.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as openfile:
                return json.load(openfile)
        else:
            print('Не можу отримати instances.json')

    def add_instance(self, name, version, icon):
        new_inst = {
            "name": name,
            "version": version,
            "icon": icon
        }
        file_path = '.launcher\\instances.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as openfile:
                try:
                    instancesjson = json.load(openfile)
                    if not isinstance(instancesjson, list):
                        raise ValueError("Дані JSON - це не список")
                except (json.JSONDecodeError, ValueError) as e:
                    print(f"Помилка читання файлу JSON: {e}")
                    instancesjson = []
        else:
            instancesjson = []

        instancesjson.append(new_inst)

        with open(file_path, 'w') as openfile:
            json.dump(instancesjson, openfile, indent=4)

    def launch_minecraft(self, username, uuid, instancename, version, modloader):
        print(f'\nЗапуск Minecraft {version} в версії {instancename} з іменем користувача: {username} (uuid: {uuid})\n')
        mcver = Version(version)
        mccontext = Context(Path(".launcher\\resources"), Path(".launcher\\.minecraft"))

        class MyWatcher(Watcher):
            def handle(self, event) -> None:
                print("Необроблений журнал PortableMC: ", event)

        mcver.set_auth_offline(username, uuid)
        env = mcver.install(watcher=MyWatcher())
        env.run()

        # Великий спасибі 2 Chatgpt за те, що змінні працюють у всьому світі протягом усього проекту, я не знав, як це працювати.
        # Якщо ви читаєте це, ви - крутий чувак.
api = Api()

webview.create_window('MetaCube Launcher ● IP: ...', background_color="#210202", url="index.html", js_api=api)
# webview.start()

webview.start(debug=False)