from ItsAGramLive import ItsAGramLive
from farbprinter.farbprinter import Farbprinter
drucker = Farbprinter()
from os import name as osname
from textwrap import TextWrapper
windowsrechner = osname == "nt"
from winregistry import WinRegistry
from winreg import  REG_DWORD
from maximize_console import maximize_console

linebreakx = 50
wrapper = TextWrapper(width=linebreakx)


logo_auswahl = auswahlliste = [
    drucker.f.brightred.black.bold,
    drucker.f.black.brightred.bold,
    drucker.f.yellow.black.bold,
    drucker.f.brightyellow.black.bold,
]
REGEDITPATH = r"HKEY_CURRENT_USER\Console"
regedit_is_zero = "HKEY_CURRENT_USER\Console\VirtualTerminalLevel is set to 0! I will try to change it to 1 so that you can read colored text!"
regedit_success = "I think, it has worked out! Let's start"
virtualterminalregedit = "VirtualTerminalLevel"
able_to_see_col_text = "Everything is configured right! You should be able to see colored text! Please restart the app if you can't see colored text"
regeditfail = """I was unable to change the Registry!\n Let\'s try it anyway!\n If you can\'t read the text in the terminal, add this to your Windows Registry:\n\n[HKEY_CURRENT_USER\Console]\n
"VirtualTerminalLevel"=dword:00000001"""
try_to_create_key = "HKEY_CURRENT_USER\Console\VirtualTerminalLevel not found! I will try to create it so that you can see colored text"

def add_color_print_to_regedit():
    try:
        with WinRegistry() as client:
            try:

                regedit_entry = client.read_entry(
                    REGEDITPATH, virtualterminalregedit
                )
                if int(regedit_entry.value) == 1:
                    print(drucker.f.black.green.negative(able_to_see_col_text))
                    return True
                if int(regedit_entry.value) == 0:
                    print(drucker.f.black.brightyellow.negative(regedit_is_zero))
                    try:
                        client.write_entry(
                            REGEDITPATH,
                            virtualterminalregedit,
                            value=1,
                            reg_type=REG_DWORD,
                        )
                        print(drucker.f.black.green.negative(regedit_success))
                    except:
                        print(drucker.f.black.brightred.negative(regeditfail))
                        return False
            except:
                print(drucker.f.black.brightyellow.negative(try_to_create_key))
                try:
                    client.write_entry(
                        REGEDITPATH,
                        "VirtualTerminalLevel",
                        value=1,
                        reg_type=REG_DWORD,
                    )
                    print(drucker.f.black.green.negative(regedit_success))

                    return True
                except:
                    print(drucker.f.black.brightred.negative(regeditfail))
                    return False
    except:
        print(
            drucker.f.black.brightred.negative(
                "Error checking if VirtualTerminalLevel is set to 1"
            )
        )
maximize_console()
add_color_print_to_regedit()
colorfunctionslogo = [drucker.f.black.red.normal, drucker.f.black.brightyellow.normal]
drucker.p_ascii_front_on_flag_with_border(
    text='InstaOBS',
    colorfunctions=colorfunctionslogo,
    bordercolorfunction=drucker.f.brightgreen.black.italic,
    font="slant",
    width=1000,
    offset_from_left_side=5,
    offset_from_text=15,
    )
drucker.p_ascii_front_on_flag_with_border(
    text='from queroestudaralemao . com . br',
    colorfunctions=colorfunctionslogo,
    bordercolorfunction=drucker.f.brightgreen.black.italic,
    font="slant",
    width=1000,
    offset_from_left_side=5,
    offset_from_text=15,
    )

allcommands = [['info','Show details about the broadcast'],
['mute comments','Prevent viewers from commenting'],
['unmute comments','Allow viewers do comments'],
['viewers','List viewers'],
['chat','Send a comment'],
['pin','Send a comment and pin it'],
['unpin','Remove a pinned comment'],
['comments','Get the list of comments'],
['wave','Wave to a viewer'],
['stop','Terminate broadcast']]


instagramusername = ''
instagrampassword = ''

while instagramusername == '' or instagrampassword == '':
    instagramusername = input(drucker.f.black.brightyellow.normal('\nYour Instagram Username:\n'))
    instagramusername = str(instagramusername).strip()
    instagrampassword = input(drucker.f.black.brightyellow.normal('\nYour Instagram Password:\n'))
    instagrampassword = str(instagrampassword).strip()
    print(drucker.f.black.brightmagenta.normal(f'\nIs this information right?\nUser: {instagramusername}\nPassword {instagrampassword}\n'))
    isitright = input(drucker.f.black.brightyellow.normal('\nWrite NO if it is not right, if it is right press ENTER:\n'))
    if isitright.strip().lower() == 'no':
        instagramusername = ''
        instagrampassword = ''

drucker.p_pandas_list_dict(allcommands, header=['command', 'description'])

live = ItsAGramLive(
    username=instagramusername,
    password=instagrampassword
)
live.start()

