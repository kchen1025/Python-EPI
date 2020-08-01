from typing import Set

from test_framework import generic_test

import collections
import string

def transform_string(D: Set[str], s: str, t: str) -> int:
    # loop through all words in dict
     # loop each char, loop through all alphabet
        # if you have a match in our set and not equal to itself, add it to adjacency list
    # graph = collections.defaultdict(list)
    # for word in D:
    #     for i in range(len(word)):
    #         for alpha in string.ascii_lowercase:
    #             comp = word[:i] + alpha + word[i+1:]
    #             if comp in D and comp != word:
    #                 graph[word].append(comp)

    # now that we have our dictionary, start graph at start, and begin doing a BFS through the nodes
    # keeping track of your level with a tuple
    # once you've reached target, return
    # else -1
    queue = collections.deque([(s, 0)])
    D.remove(s)

    while queue:
        visiting = queue.popleft()
        word = visiting[0]
        depth = visiting[1]

        if word == t:
            return depth

        # visit neighbors
        for i in range(len(word)):
            for alpha in string.ascii_lowercase:
                comp = word[:i] + alpha + word[i+1:]
                if comp in D:
                    D.remove(comp)
                    queue.append((comp,depth+1))

    return -1











































    # # # generate dictionary
    # words = {}
    #
    # def getWords(word):
    #     output = []
    #     for i in range(len(word)):
    #         wordKey = word[:i] + '*' + word[i+1:]
    #         output.extend(words[wordKey])
    #     return output
    #
    #
    # def generateDict():
    #     for word in D:
    #         for i in range(len(word)):
    #             wordKey = word[:i] + '*' + word[i+1:]
    #             if wordKey not in words:
    #                 words[wordKey] = []
    #                 #loop through dictionary for matches
    #                 for originalWord in D:
    #                     if originalWord[:i] + '*' + originalWord[i+1:] == wordKey:
    #                         words[wordKey].append(originalWord)
    # generateDict()

    StringWithDistance = collections.namedtuple('StringWithDistance',('candidate_string','distance'))
    q = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)

    while q:
        visting = q.popleft()



















    # StringWithDistance = collections.namedtuple('StringWithDistance',('candidate_string','distance'))
    # q = collections.deque([StringWithDistance(s, 0)])
    # D.remove(s)
    #
    # while q:
    #     visiting = q.popleft()
    #
    #     if visiting.candidate_string == t:
    #         return visiting.distance
    #
    #     for i in range(len(visiting.candidate_string)):
    #         for c in string.ascii_lowercase:
    #             cand = visiting.candidate_string[:i] + c + visiting.candidate_string[i + 1:]
    #             if cand in D:
    #                 D.remove(cand)
    #                 q.append(StringWithDistance(cand, visiting.distance + 1))
    # return -1







if __name__ == '__main__':
    test = ["dhu", "add", "scf", "ckw", "fgn", "mgd", "ltr", "isl", "ere", "hed", "bot", "pim", "hag", "moc", "elm", "tpi", "loy", "axe", "wyn", "rog", "lif", "red", "otc", "ung", "geb", "abr", "urn", "gph", "van", "hin", "dbl", "ult", "gur", "nov", "urf", "dea", "kan", "tsp", "qaf", "sur", "vie", "nid", "afd", "hob", "mgr", "ria", "lca", "pye", "ife", "lac", "als", "pop", "vel", "lag", "out", "mad", "yee", "bps", "rim", "hey", "don", "cod", "ahi", "mal", "luc", "fur", "dim", "pes", "zak", "dom", "jos", "hot", "gud", "plf", "rom", "clk", "dkm", "pbx", "flb", "own", "kep", "deg", "ell", "tck", "pup", "mym", "eme", "iwa", "vii", "psi", "hop", "aam", "spp", "eke", "gie", "aha", "lox", "heo", "dae", "bxs", "asg", "uro", "mhg", "cho", "isn", "fcp", "adv", "elk", "dal", "kef", "vum", "cwm", "hor", "ann", "sel", "you", "feh", "nbg", "jon", "dos", "boo", "eff", "cyl", "cro", "ipm", "nog", "pet", "tas", "zan", "eft", "kas", "dip", "ass", "uti", "pom", "lir", "aln", "bys", "doe", "ted", "llb", "bey", "gry", "fed", "twa", "duo", "fin", "flo", "eyl", "fry", "mts", "hcb", "sal", "alf", "whf", "bam", "caf", "tau", "suk", "aud", "yus", "een", "jur", "pts", "elf", "cit", "led", "bug", "aer", "ady", "emf", "tpd", "jct", "tum", "shr", "csc", "din", "aob", "ary", "cai", "och", "val", "yen", "jms", "yoy", "vex", "nix", "hyp", "tug", "mem", "gem", "ptp", "scr", "vip", "dca", "raw", "yes", "oni", "fod", "moa", "ess", "ref", "pau", "mtn", "mah", "chi", "sau", "cfh", "jeu", "gar", "bld", "koa", "try", "poa", "kif", "tao", "moy", "xyz", "pfg", "nut", "soy", "rhb", "dub", "hae", "ave", "imp", "rex", "yok", "pcf", "tee", "gns", "ume", "acy", "hak", "ges", "sob", "tou", "gyn", "awn", "rux", "lim", "ppd", "frs", "oto", "eir", "afb", "nee", "pow", "cot", "ign", "cpo", "sid", "soc", "haw", "enl", "esd", "sat", "tlr", "tnt", "chs", "yip", "hub", "qat", "olm", "gae", "tha", "dpt", "dey", "ode", "tod", "dah", "kex", "xvi", "uit", "tom", "ram", "dux", "foh", "icy", "ino", "goa", "nus", "fip", "may", "zig", "mrs", "tec", "iva", "oik", "ape", "gus", "eco", "mib", "oat", "zed", "pvt", "net", "sky", "mmf", "pap", "seg", "ask", "ian", "pdq", "yor", "iqs", "ban", "awd", "pob", "ima", "dks", "jnt", "sou", "aux", "lie", "tob", "sey", "alb", "epi", "nob", "liz", "fig", "aix", "ute", "hew", "fwd", "ios", "qto", "pox", "use", "nea", "fon", "yoi", "leg", "job", "erk", "hoi", "wiz", "hei", "dib", "sec", "ata", "lax", "crc", "rio", "hau", "woe", "yet", "bvt", "pfx", "dwt", "blo", "opa", "zac", "fad", "isz", "brl", "ead", "jem", "ese", "hld", "fou", "fll", "apr", "men", "ira", "lyn", "aff", "abe", "tap", "yug", "gor", "txt", "gid", "tea", "kua", "bnf", "pic", "neg", "abv", "mtd", "req", "ahu", "gil", "bai", "imu", "kaf", "ffa", "ala", "hic", "nib", "fab", "dat", "pah", "cry", "tit", "ear", "bch", "few", "tun", "hee", "sgd", "hup", "clo", "bog", "sos", "sai", "mim", "jus", "jut", "abt", "gox", "ipl", "phi", "vod", "abc", "egg", "tph", "pcm", "fag", "ado", "wis", "ups", "gun", "hie", "tji", "oii", "ern", "byp", "hye", "bsf", "pax", "lek", "dup", "waw", "noy", "fir", "oca", "lop", "mar", "bpt", "arb", "opp", "sta", "ora", "len", "dob", "eva", "thy", "low", "cud", "key", "tov", "god", "aug", "wud", "nth", "ros", "bae", "per", "zoa", "gds", "lst", "yan", "jef", "sma", "hoe", "qrs", "ghi", "lou", "pin", "gio", "ctf", "pep", "map", "urb", "taa", "mil", "tex", "tup", "sar", "whr", "wob", "flu", "grx", "adp", "vee", "sfm", "lid", "cis", "cre", "fog", "tpm", "ald", "hep", "pta", "civ", "bbl", "her", "ivy", "pad", "dao", "cpu", "via", "tay", "fow", "wut", "coo", "caw", "aas", "ohs", "yea", "hay", "nap", "mos", "mee", "ecb", "iii", "tam", "gap", "poe", "dha", "lig", "col", "sap", "wid", "cps", "elb", "kee", "art", "lbw", "vas", "waf", "mop", "nun", "jet", "spt", "ccm", "rya", "aes", "fez", "aby", "der", "dis", "imi", "heh", "ins", "meq", "lbf", "tav", "qua", "ray", "eds", "fun", "alk", "lsc", "sex", "bio", "sha", "pee", "han", "emp", "haj", "zod", "tol", "feu", "pan", "wjc", "geo", "ppb", "abd", "rik", "ais", "wes", "swy", "lar", "unb", "env", "amt", "clr", "yin", "nam", "arr", "rum", "boc", "sin", "emm", "yrs", "rot", "gol", "alw", "eat", "ems", "cwt", "wef", "nab", "gut", "dam", "lot", "hod", "sim", "did", "mig", "qtd", "mho", "toa", "ubc", "sab", "cad", "itd", "coz", "kie", "tat", "cwo", "obl", "mux", "cul", "owd", "arc", "dur", "jap", "cgs", "cop", "oms", "atm", "aku", "ock", "tig", "fay", "sub", "jab", "bur", "hny", "sqd", "bye", "pil", "sis", "big", "dlr", "oak", "udo", "sae", "woa", "fth", "ush", "who", "cum", "lib", "khi", "inv", "gin", "dev", "cav", "jug", "kim", "tln", "che", "gra", "att", "yun", "vax", "ova", "baa", "leo", "ifs", "mtg", "aho", "mac", "tlo", "sus", "nan", "bkg", "pud", "fae", "rcd", "toi", "jar", "amb", "ctr", "hah", "spa", "ays", "xxv", "lui", "tal", "glt", "oil", "rus", "tdr", "gan", "tie", "est", "ing", "tos", "xxi", "oke", "sia", "kph", "huh", "lat", "anc", "pig", "any", "lip", "aeq", "awm", "mia", "lxx", "kpc", "ela", "tor", "jew", "sty", "upo", "lap", "lue", "grs", "apx", "hcl", "chn", "obs", "wos", "bom", "oba", "dad", "wad", "par", "foe", "pav", "ako", "nag", "abl", "hes", "cur", "ati", "lyc", "lcd", "nis", "ame", "hat", "but", "pal", "pps", "baw", "are", "pik", "sew", "eau", "ony", "sam", "ugh", "dot", "rok", "hue", "psf", "fat", "app", "urs", "cab", "sud", "dar", "gpd", "usu", "ida", "dig", "tem", "yid", "nye", "twp", "myc", "grr", "bpi", "its", "cpd", "hyd", "seq", "fac", "eof", "cdr", "osc", "guz", "ksi", "rel", "luo", "ptg", "zel", "sic", "glb", "ips", "pkg", "pir", "nip", "ami", "unc", "pli", "lao", "gay", "mpg", "efl", "owe", "pry", "dep", "kyl", "tyt", "koi", "kor", "rha", "mod", "ton", "kgf", "oho", "git", "sue", "ric", "shy", "ull", "pod", "son", "aet", "tog", "gis", "cfd", "lwl", "arg", "wac", "ver", "tfr", "cyp", "ret", "gas", "fid", "cie", "crl", "vis", "kid", "fam", "pty", "xiv", "toe", "ail", "lex", "ink", "hun", "qty", "tur", "pro", "vaw", "fbi", "bls", "fey", "lym", "loe", "cor", "kui", "bag", "rie", "alg", "bea", "ain", "rld", "kay", "aus", "reb", "avn", "xis", "hum", "ppm", "nek", "lav", "dit", "lew", "ona", "riv", "wit", "cun", "roi", "obj", "pot", "goo", "ire", "gib", "les", "uni", "mut", "iao", "cub", "psw", "rap", "pug", "lur", "kyd", "irs", "bec", "syn", "ile", "wag", "ddt", "qqv", "pwt", "zep", "ise", "tps", "oes", "mor", "lei", "fpm", "lod", "law", "het", "tst", "orf", "deb", "gye", "mss", "buz", "rut", "rat", "gld", "toy", "noh", "wir", "one", "fet", "ter", "hud", "poh", "orl", "ump", "rec", "eel", "hab", "yaw", "pen", "tui", "tty", "ust", "sri", "suf", "teg", "ufo", "zad", "bsh", "dew", "bos", "rly", "fen", "jcl", "wry", "gat", "sac", "cpm", "ike", "crs", "mom", "rye", "fly", "and", "uts", "ons", "sil", "aka", "rhd", "sao", "oxy", "odd", "pte", "kop", "hol", "mix", "nar", "vet", "ten", "ani", "yoe", "rit", "ono", "oaf", "buy", "lux", "sow", "aye", "ext", "ptt", "poz", "lor", "spy", "oam", "gro", "tho", "phr", "tbs", "rhe", "umu", "vei", "pis", "alt", "wey", "rox", "rev", "una", "tng", "jan", "vil", "ged", "had", "azo", "tip", "ose", "cia", "jim", "ads", "nep", "hwy", "efs", "exp", "bay", "bin", "jnd", "run", "gps", "inf", "slt", "gyp", "neb", "tae", "oie", "bed", "erf", "rob", "mtx", "pfc", "dkl", "zar", "faq", "ore", "hao", "roc", "ack", "dab", "aga", "aum", "mlx", "abb", "brr", "rep", "ide", "she", "roy", "ans", "aim", "gam", "ake", "nox", "bob", "gcd", "apa", "bal", "wok", "get", "yis", "shh", "iph", "kab", "jat", "liq", "joy", "xxx", "mow", "dod", "rnd", "aor", "sax", "car", "vai", "ulu", "for", "rid", "cog", "doz", "why", "reh", "vac", "msg", "goy", "jot", "old", "bcd", "das", "cos", "rei", "gaw", "ssp", "ole", "cat", "lbs", "ski", "dun", "voe", "vol", "mwa", "kae", "ggr", "bid", "dtd", "utu", "lad", "alo", "pph", "cep", "uca", "rah", "plu", "zer", "mes", "lwm", "kip", "ben", "gen", "syr", "keg", "naw", "zek", "dau", "med", "row", "shi", "fee", "how", "std", "cyc", "ola", "hhd", "sop", "btl", "kln", "bde", "gau", "pho", "wat", "zea", "cpl", "taj", "bel", "pur", "csw", "ive", "coe", "oct", "arm", "amy", "ice", "sqq", "cgm", "jag", "tux", "lee", "roe", "hwt", "wed", "yah", "dcb", "say", "nou", "won", "foy", "hap", "sok", "ers", "lys", "ate", "poi", "dec", "lit", "tef", "meg", "owk", "aht", "fro", "alc", "rms", "opt", "sol", "gad", "lep", "xcl", "bul", "fcy", "ito", "sld", "con", "hon", "err", "pie", "kos", "ilk", "fiz", "grf", "tax", "cap", "sad", "fan", "sed", "prp", "ant", "ens", "dud", "rem", "pea", "kit", "laz", "urd", "sir", "fot", "yez", "jeg", "nub", "asb", "met", "our", "wap", "mag", "mya", "mev", "doa", "wea", "act", "pit", "quo", "ber", "aly", "aid", "yeh", "zoo", "ppt", "zap", "edh", "ish", "ean", "eli", "mir", "loc", "bkt", "ops", "nad", "ibm", "uhs", "kyu", "wab", "dkg", "ayu", "wim", "arx", "jee", "bdl", "wem", "abu", "chm", "wet", "pct", "can", "ron", "sie", "aro", "til", "sit", "sds", "ich", "not", "wup", "fol", "eld", "pfd", "hts", "cpt", "dag", "hrs", "adc", "kai", "kra", "ord", "lin", "yuh", "doc", "hav", "mam", "roo", "sny", "ihs", "bee", "por", "gob", "raj", "ihp", "bus", "tyr", "hcf", "sah", "mae", "boy", "syd", "xat", "nat", "yup", "bap", "jah", "reg", "fud", "ita", "rod", "lah", "fob", "bds", "aah", "agr", "enc", "pam", "ahs", "uta", "hit", "obv", "ion", "pac", "tez", "veg", "sct", "fut", "qts", "qui", "var", "mon", "fei", "lay", "tab", "vag", "sym", "beg", "mph", "pub", "gez", "mun", "lwp", "yox", "prf", "kob", "bis", "cif", "mau", "tpk", "von", "keb", "cdg", "sem", "sch", "dap", "ama", "bac", "shp", "usa", "mat", "mks", "yad", "uji", "rib", "eer", "stg", "div", "doo", "meo", "sfz", "nil", "qid", "bod", "tis", "uru", "ule", "auk", "ade", "eon", "khu", "abn", "dif", "rtw", "xed", "eta", "rab", "lye", "dem", "lud", "mew", "trp", "cam", "ctg", "tib", "bro", "eye", "ism", "bat", "ohm", "cru", "oft", "awl", "pon", "nod", "hox", "eyr", "woo", "tow", "ldg", "qed", "myg", "mit", "ego", "oud", "peh", "cto", "tag", "tot", "shu", "ila", "tye", "gaj", "end", "rle", "yds", "rfz", "ors", "jow", "nim", "kgr", "now", "csk", "rpt", "due", "loo", "vow", "fit", "ran", "tua", "gte", "org", "dyn", "ope", "leu", "mud", "kon", "hia", "fum", "fld", "lea", "pyr", "ipr", "ppi", "box", "rug", "ara", "obe", "voc", "gul", "pwr", "woy", "agy", "rad", "vau", "ker", "hgt", "osi", "umm", "fie", "dft", "mid", "yak", "gee", "non", "soh", "mot", "his", "que", "sen", "wan", "sog", "loq", "oki", "pya", "hel", "lug", "gon", "bub", "far", "hen", "tew", "saw", "haf", "ctn", "adm", "jad", "zip", "sla", "wot", "tar", "bol", "ure", "irk", "bib", "sov", "bud", "jud", "bbs", "loa", "web", "tmh", "wod", "ibo", "wow", "noo", "fox", "bow", "edo", "pmt", "lai", "nom"]

    # print(transform_string(test, 'ela','own'))

    print(transform_string(['bat','cot','dog','dag','dot','cat'], 'cat', 'dog'))

    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
