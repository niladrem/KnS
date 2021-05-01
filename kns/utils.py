from copy import deepcopy

def minimize_permutation(in_permutation) -> list:
    in_sorted = sorted(in_permutation)
    return [in_sorted.index(i) for i in in_permutation]


def generate_permutations(l, ones, left, out):
    if ones > left:
        return
    if left == 1:
        if ones:
            out.append(l + [1])
        else:
            out.append(l + [0])
    generate_permutations(l + [0], ones, left-1, out)
    if ones:
        generate_permutations(l + [1], ones-1, left-1, out)


def extract_list(input_list, permutation):
    out1 = []
    out2 = []
    for i, elem in enumerate(input_list):
        if permutation[i]:
            out1.append(elem)
        else:
            out2.append(elem)
    return out1, out2


def has_twins(in_list, min_twins=2, twins=None):
    for length in range(min_twins*2, len(in_list) + 1, 2):
        idx = 0
        permutations = []
        generate_permutations([], length / 2, length, permutations)
        while idx + length <= len(in_list):
            for permutation in permutations:
                perm1, perm2 = extract_list(in_list[idx:idx+length], permutation)
                perm1_ = minimize_permutation(perm1)
                perm2_ = minimize_permutation(perm2)
                if perm1_ == perm2_:
                    if twins:
                        twins.p1 = perm1
                        twins.p2 = perm2
                    return True
            idx += 1
    return False


def add_number_to_permutation(permutation, position, number):
    out = deepcopy(permutation)
    out.insert(position, number)
    return out


def test_candidates_for_position(permutation, min_len, available_numbers, position):
    candidates = []
    for number in available_numbers:
        tmp = add_number_to_permutation(permutation, position, number)
        if not has_twins(tmp, min_len):
            candidates.append(number)
    return candidates

victory = """\033[32m
XXXXXXXXXXXXXXXXXXKKKKKKKKKKK00OOkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOkOkkkkkkkkkk
XXXXXXXXXXXXXXXXXXKKKKKKKK0kdlc:;;,;:clodxxxkkOOOOOOOOOOOOOOOOOOkkkkkkkkkkkk
XXXXXXXXXXXXXXXXXXXXKKK0Oxl:;,'''''',,,,,;,,,;;cldkOOOOkkkkkkkkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXXXXKKK0kdoc:;,,,,,',,,,,,,,''''''';cdkkkkkkkkkkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXXXXKKKOkoc:;,,,,,,;::::;;;,'''...'''';lkkxkkkkkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXXXXXKKOkoc::::;::lodxxkxdl:,'''.......':;..ckkkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXXXXXXKK0xolclodxk0KKKKK0Oko:,,'.... ........okkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXXXXXXKOxkOkk0KKKXXXXXXKK0Oxc,'......  ... ..:kkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXXXXXKOkk000KKKXXXXXXXKKK0kdc;'.......   .. .,xkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXXXXK0kk0000KKKKXXXXKKKKKOxoc;,....... .  . ..dxkkxkkkkkkkkkx
XXXXXXXXXXXXXXXXXXKK0kO0KKKKKKXXXXXXKKK0Odl:;'....    ..  ..'oxxxxxxxxxxxxxx
XXXXXXXXXXXXXXXXXXXKK0O000000KKKKKKKKK00Oko:,'..  .....'  ..,lxxxxxxxxxxxxxx
XXXXXXXXXXXXXXXXXXKK0xxxkkkkxkkOO00000OOOkxl'... . ...'l  . ,cxxxxxxxxxxxxxx
XXXXXXXXXXXXXXXXXXkokd::lxxol:clddxxxxddlc:,... . ......  . ':xdddoooooooooo
XXXXXXXXXXXXXXXXXXKxkOolkOoclolccoloodxxxdxdo;. . ....     .................
XXXXXXXXXXXXXXXXXXXKOkxO0OOxdxxxxkxk000OOOOkxl. .   .       ................
XXXXXXXXXXXXXXXXXXXKKOO00OOOkxxxkOO000000Okkxo'             ................
XXXXXXXXXXXXXXXXXXKKKkO0OOOkxodkO0000000OOkkkxc.            .... ..     ... 
XXXXXXXXXXXXXXXXXKKKK0ddolcclodddxkkkOOOOOkkkxl;.             .           ..
XXXXXXXXXXXXXXXXKKKKKK0dolcloxxxdodxxkkOOOkkxdl:;;;'.                      .
XXXXXXXXXXXXXXKKKKKKKKKOxo,:llloodxxkkkkkkkxdolclllc,...                    
KKKKKKKKKKKKKKKKKKKKKKKKkoclloxxkkkkkkkkxxdolccloddo:..''.                  
KKKKKKKKKKKKKKKKKKKKKKK00xccloxxkkkxddddooc:::oddddl,..''''....             
0000000000000K0KKKKKK000Oolccoddxdoollcc::;;ldddxdl;.'..'''....''...        
00000000000000000KKK000ko;,;cc;;:;,;,,;;;:lodddddl,''',,'.'....,,,,,,'.     
00000000000000000000ko:,,''........',,,:coodddddo;'''',,'...'.',,,,,,,,,'.  
OOO000000000000000kc,,''''.........,;:cllooddddo:'',,''.......'''',,,,,,,,,.
OOOOO000OOOO000Oxc,''''..'.........:cllooodddddc'',,''...''.....''',,,,,,,,,
OOOOOOOOOOOOOOkc,'''''........'.....:clooddddoc,'''''............''''',,,,,,
OOOOOOOOOOOOOx;'.'.''.........'......:llodddo:,'','''.........''...''''',,,,
OOOOOOOOOOOOo,.....'.................':lodoc,.....'..........'''''.....'',,,
kOOOOOOOOOkl,'...................'..'.';ol;,'. .............''''''''...'''',
kkkkkkkkkkc'''..........................''.............'....'''''.''.....'',
kkkkkkkkkc'...................'.......................''....'''''.''.'''...,
      ██╗    ██╗██╗   ██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗ █████╗ 
      ██║    ██║╚██╗ ██╔╝██╔════╝ ██╔══██╗██╔══██╗████╗  ██║██╔══██╗
      ██║ █╗ ██║ ╚████╔╝ ██║  ███╗██████╔╝███████║██╔██╗ ██║███████║
      ██║███╗██║  ╚██╔╝  ██║   ██║██╔══██╗██╔══██║██║╚██╗██║██╔══██║
      ╚███╔███╔╝   ██║   ╚██████╔╝██║  ██║██║  ██║██║ ╚████║██║  ██║
       ╚══╝╚══╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
"""


defeat = """\033[31m
KKKKKKKKKKKK00000000000000000000OOOOOkxddoodxkkkkkxxxxxxxxxxxxxxxxxxxxx
KKKKKKKKKKKK0000000000000000000OOxdollccc::ccoddddddxxxxxxxxxxxxxxxxxxx
KKKKKKKKKKKK0000000000OOxdooooc;,,'''''''''',;:::;;;:ldxxxxxxxxxxxxxxxx
KKKKKKKKKKKK0000000ko:;,'''........'''''''''.......',,;ldxxxxxxxxxxxxxx
KKKKKKKKKKK000000Oo,'''..'''''''...,,'....'''''......',',cxxxxxxxxxxxxx
KKKKKKKKKKK00000kxc,'..........''''''''............... ...:ddxxxxxxxxxx
KKKKKKKKKKK0000Oxoc,'''.'....''',;:;;,'......  .......  ....,:dxxxxxxxx
KKKKKKKKKKK00000kdc;,;,...''',,:codooc:,'......           ...'cdxxxxxxx
KKKK000KKKK00000kd:,'''.''',;cloxkOOkxdl:,'......          ...cddxddddd
KKKK000000000000Odl:;;,,,;:coxkO0000OOkxo;'.......          ...:odddddd
KKK00000000000000kdlc:::loddkOOOO000OOOxoc;'.......         .'..;dddddd
KKK0000000000000OxooddodxkkkOOOOOOOOOOOxoc;'.......          .;''oddddd
0000000000000000OxdoxxxkkOOOOOOOOOOOOOkxoc;'......    .'..    .;.,oolc:
0000000000000000OkddkO000000xkkkkkOOOOkxo:;,'...     ......    .,......
00000000000000000O0K00000OO0kxkkOOOOOOOkxdc;'...     ......     .'.....
000000000000000KKKKKKXKkk0K0kodkOOOOkkkkkxdo:....    ':::.       '.....
0000000Okk00000000KKK0kOKKOxlcoxkkkkxxxxxddl;....    .'',.       ......
000000Okxlx00000000OkkKXKOl;::ldddddddooc;'';ll:'                 .    
000000OkdcxO000000OxO000kod0x'';cllol;,;codddxddc.                     
00000OkxdO000O00OkxOOOkxd0K0d,'';:;';oxkkkxxxxddoc'                    
O000OkkkO000000OxdOOOkdoO0kd,';:cclockkkkkxxxxddooc'.           .      
OOOOOkkxkkO0000OOO0Oxox0Okdlc;;:cloodxkkxxxxxddooooc;,'....    ..'.....
OOOOOkkxxxxOOOOOOOOkokOkxolllcc::cloddddxxxxddddddolc::;::c:'  ........
OOOkkxddddddxkkOOOOkOOkxdllllll:::loddddddddddddddoolcccccc:...........
kkkkkddddddddxxkkOOkkkxdccl:;;;:c::coodddxddddddddollc:lllc'...........
kkkkkxddxddddxxxxkkkkxddd;,'',;ccc::clooooddddddool::;clll;............
kkkkxxddxxxxxxxxxxxxxdoc,...'',;;:::cclooooooooolc:,,:cllc'............
xxxxxxxddxxxxxxxxxxddo:........'',;:cccccccccccc:;'';clcc;.............
xxxxxdxxdxxxxxxxxxddol'..........',::cccc:;;,''''.';::cc:'.............
xxxdddxxxxxxxxxxdddoc'............',,,;;'........',;::c:'....... ......
xxxdddxxxxxxxdddool:'..  ........ ......   ...',,;;:::;'...............
xxoooddxxxxxdddolc;....  ......            .',;;;::::;'................
dolooodxxxxdddol:'............        ........',;;;;,..................
dlloooodxxdddolc'................        .......,;,,...................
██████╗ ██████╗ ███████╗███████╗ ██████╗ ██████╗  █████╗ ███╗   ██╗ █████╗ 
██╔══██╗██╔══██╗╚══███╔╝██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗  ██║██╔══██╗
██████╔╝██████╔╝  ███╔╝ █████╗  ██║  ███╗██████╔╝███████║██╔██╗ ██║███████║
██╔═══╝ ██╔══██╗ ███╔╝  ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╗██║██╔══██║
██║     ██║  ██║███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚████║██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝                                                                       
"""

baner = """
ddddddddddddddddddddddddddddddddddddddollooooooodxxxxkkkkkkkkkkkkkkkkkkkkkxxxxdooooooollodddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddooccccc,',;,,,,:ccldxxkkkkkkkkkkkkkkkkkkkkkxxdlcc:,,,,;,',cccccooddddddddddddddddddddddddddddddd
ddddddddddddddddddddddddddoc;;;,'''..''''''''',,,:lxxkkkkkkkkkkkkkkkkkkkkkxxl:,,,'''''''''..''',;;;codddddddddddddddddddddddddd
dddddddddddddddddddddddddl;,''''''''''''''''''',,,;lxxkkkkkkkkkkkkkkkkkkkxxl;,,,''''''''''''''''''',;lddddddddddddddddddddddddd
dddddddddddddddddddddddol;'''..'''',;:::::;;,'',,;:cdxkkkkkkkkkkkkkkkkkkkxdl:;,,'',;;:c:::;,''''..''';loddddddddddddddddddddddd
ooddddddooooooooooddddol,......''',;codddoolc:;;;::coxkkkkkkkkkkkkkkkkkkkxoc::;;;:cloodddoc;,'''......,loddddooooooooodddddddoo
oooooooooooooodooddodoo:'.......'',coxxkkkkkkxdolollodxkkkkkkkkkkkkkkkkkxdollolodxkkkkkkxxoc,''.......':ooooddooooooooooooooooo
oooooooooooooooooooooooc.........';coxxkkkkkkkkxxxdooxkkkkkkkkkkkkkkkkkkkxooddxxkkkkkkkkxxoc;'.........cooooooooooooooooooooooo
ooooooooooooooooooooooo;.........',:oxxxxkkkkkxxxxxdoxkkkkkkkkkkkkkkkkkkkxodxxxxxkkkkkxkxxo:,'.........;ooooooooooooooooooooooo
ooooooooooooooooooooool;.........':odxxxxkkkkkkxxxxdloxkkkkkkkkkkkkkkkkkkoldxxxxkkkkkkxxxxdo:'.........;loooooooooooooooooooooo
ooooooooooooooooooooool:'........';codddxxdddooooooodxkkkkkkkkkkkkkkkkkkkxdooooooodddxxdddoc;'........':loooooooooooooooooooooo
lllllllllooooooooooolllc..,'''',;clcllc::c;,,;;ll;,:lcokkkkkkkkkkkkkkkkkocl:,;cl;;,,;c::cllclc;,'''',..clllooooooooooolllllllll
lllllllllllllllcclllllll,.':;;:clodddxxooolll:cddccoooxkkkkkkkkkkkkkkkkkxoooccddc:llloooxxdddolc:;;:'.,lllllllcclllllllllllllll
cc:;...................'...,lllloodddxddddooooddxoldxkkkkkkkkkkkkkkkkkkkkkxdloxddooooddddxdddoollll,...'...................;:cc
'...........................,cllooodddddddolllodddldxkkkkkkkkkkkkkkkkkkkkkxdldddolllodddddddooollc,...........................'
............................:lccloooooollcllc::clllxxxkkkkkkkkkkkkkkkkkkkxxxlllc::cllclloooooolccl:............................
......  .  .       .......'cll:::clloooolcccc:;:clxxxxxkkkkkkkkkkkkkkkkkxxxxxlc:;:ccccloooollc:::llc'......        .  .  ......
.....     .    ...........'lolc;,,:cccloooolc::coxxxxxxxkkkkkkkkkkkkkkkxxxxxxxoc::cloooolccc:,,;clol'...........    .     .....
...         .',''''''......,lllc:,',;;:cloooooodxkkkkxxxxxxxxxxxxxxxxxxxxxkkkkxdoooooolc:;;,',:clll,......'''''','.         ...
...       .','''''.'........,lllcc:,''''coxxkkkkkkkkkkkxxxxxxxxxxxxxxxxxkkkkkkkkkkkxxoc'''',:cclll,........'.''''','.       ...
..       .''''''.'...........,lllcc:;,'';ldxxxxxxxxkkkkxdxxxxxxxxxxxxxdxkkkkxxxxxxxxdl;'',;:cclll,...........'.''''''.       ..
..   .. .','''.'..............':llcc:;,,,codddddxxxkkkkdddddddddddddddddkkkkxxxdddddoc;,,;:ccll:'..............'.''','. ..   ..
...... .',''''..................,cc::;'..,,';ccllloxxkkdddddddddddddddddxkxxolllcc;',,..';::cc,..................'''','. ......
...    .'''''''...................'','.....';:ccclodxxxdddddddddddddddddxxxdolccc:;'.....',''...................'''''''.    ...
...    .'''''......................................':llloooodddddddoooolll:'......................................'''''.    ...
...   .''''''........................................;clllllooooooolllllc;........................................''''''.   ...
.    ..''''''.........................................';::clooolloolc::;'.........................................''''''..    .
     .''''..............................................',;:clccclc:;,'..............................................''''.     
    .'''''.....................................    ......,;:::::::::;,......    .....................................'''''.    
   .'''''....................................      ......';;:::::::;;'.....     . ....................................'''''.   
              ____  ___     _     ____   _   _  _____        ____   _      ___  __/_/ _   _  ___     _     _  __ ___ 
             / ___||_ _|   / \   / ___| | \ | || ____|      | __ ) | |    |_ _||__  /| \ | ||_ _|   / \   | |/ /|_ _|
            | |     | |   / _ \  \___ \ |  \| ||  _|        |  _ \ | |     | |   / / |  \| | | |   / _ \  | ' /  | | 
            | |___  | |  / ___ \  ___) || |\  || |___       | |_) || |___  | |  / /_ | |\  | | |  / ___ \ | . \  | | 
             \____||___|/_/   \_\|____/ |_| \_||_____|      |____/ |_____||___|/____||_| \_||___|/_/   \_\|_|\_\|___|
                                                                                                           
"""