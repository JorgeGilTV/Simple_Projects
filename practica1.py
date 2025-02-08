from tkinter import *


L01="             ..  .. ......................   . ..       ...                     \n"
L02="           ...........,::=+I$ZZODDNDNMNDDD888ODD88888O$+~:,.........            "
L03="           ..ZMMMNMMMMM$ND8NNMNMMMDDNDDM8Z7Z7I78NNNDMNNNMMMDZZ8DMZ..            "
L04="     ......8DDDMZMM8NNMMMNNNDO88OZ$$$$$ZZZZZNMMN8OIZNMMMNNMMMMD=7MNO.....       "
L05="     ...~MN8NOMMDDDMMDM8OZZ$$$7I???++++=++++??7Z8NMMDMO7,.....Z~:M$OMM,..       "
L06="   ...=MMDN$NMZNOMDNDDZO8Z:..................:$$$$$$ZZDMMNOD7:=$8MMNMDMM,  .    "
L07="    :DM8NNOMDNM$MMNMNOO7... .......................:$8O8O8DMMMMMMMM$NNNDMO..    "
L08="...MMMNM8MM8MM+MMMNMNDDI... ...............  .... ....  .888ONDMMMMN.ZDD8MMN. .."
L09="..MM8MMDMMMMMM:MMNMNDNNNM8Z?:.......... .....   ...........,8O88ONMMM:+D8NNMM,. "
L10=",MM8DN,MMMDMMMDIMMMMMMMNDNNND8DOOOO7+++=,,,............ ......?88OOMNM,,DNNNMM. "
L11="MM8NM.7+MMDMMMNMMMOI7DMMMMMMMMMNNNMMNNNNDDDDDDNNNND8I+...........$O8OMM=.NDDDMM."
L12=".MZN:.D:MMMMNMMMMMNNNNDDNDDD88D888NDD88D88OOOZ$$777Z77DMM8I,... ...888DMI.MMDM. "
L13="..MDZ8M:8MMDMNMMNM88DDNNDNNDDNDDDNNNNNNDNMM8OZ$$ZZZO88NNMMD$8I,.,....$8D8M8MM.  "
L14="...MO~NO~NMMNMOM8N8DDDNNNDDDNNDNNNNMZ==I$8D88DNNMMMNNNNMDZ?ZO=87,..  .,DN7MM... "
L15="    MM7D8.7DMMMMNDMMNNNMDNN8$?IODNNNNDDNNNNDDNNNNNNNNNNNMMMMNZ:IO=.....8+NN.    "
L16="  .  $MMNM87,,$NMMMN$I78NNDDNNNNNNDNDDDNNNNDNNNNNNNNNNNNMMMNMMNO,8...:O?N=..    "
L17="     .7MMMNNMMMMMMMNNMMNMNNNNNNNNNNDNNN8DNNNNMMMMMMMMMNMMNNNDMMMMZM.O$$M,       "
L18="     ...MMMMMMMMNMMMMMNMNNNNMMMMMMNNNNNDNNNNNNNNNDDDNNDDDMMMMMMNMOM7$8M...      "
L19="     ..  MMMMNNMNMNOMMMMMMMMMMMMNMNNNNDDNNDNNNNDNNNNNNDNMMMMMMNNMZMMMD          "
L20="     ..  .:NN8NMMMMMDMNNNNN8$???IZNMMMMMMMMMNDDDDNNNNNMMMNMNMMMNMMMN...         "
L21="     .. ....MN,D7?DMMMMMMMMNMNMDNDNDDD8O?~=8MMMMMMNNNNNNMMMMMMMMNM7.            "
L22="     ..  ....M8D+O......,=+?ZNMMMMMMMMMMMMNNDDDZ7NMMMNNNNMMNMMMMM: .            "
L23="            ..,MNM?N..... ..    . .   . ,=7OMMMMMNNOMMNNDNMMMNN7 .              "
L24="             ...ZNMNIM.... .           . ........:MMNMMNDNNDNM                  "
L25="           .. ....MMMNNID=..           .... .......NNMONDNMM..                  "
L26="                .. INMMNN$=O8,...................$ZNZ8MMNMI                     "
L27="                 . ..ZMMMMMMNI?+$Z$?+++~====IOOZIO7NMMMMZ.                      "
L28="                      .DNMMMMMMNM$?+???????++78NMNMMMMZ..                       "
L29="                 . .... ,MMMMMMMMMMMMMMNMMMMMMMMMMMMO....                       "
L30="                          .NMMNM7DO........IMMMMNN7 .                           "
L31="                          . ,MMMMM78DN,.?MD8NMMMM.....                          "
L32="                            . .7MNMNM8I?8MNMMN:....                             "
L33="                              . .ZMMMMMNMMMM+. ....                             "
L34="                               .  .NNNMNMM7.                                    "
L35="                                 .. ..M$.....                                   "
L36="                                 . .........                                   "

text = L01+L02+L03+L03+L05+L06+L07+L08+L09+L10+L11+L12+L13+L14+L15+L16+L17+L18+L19+L20+L21+L22+L23+L24+L25+L26+L27+L28+L29+L30+L31+L32+L33+L34+L35+L36


def begin(top):
    L1 = Label(top, text = L01)
    L1.grid(row=1)
    L1.pack (side = LEFT)
    L2 = Label(top, text = L02+"\n")
    L2.pack (side = LEFT)
    L3 = Label(top, text = L03+"\n")
    L3.pack (side = LEFT)
    L4 = Label(top, text = L04+"\n")
    L4.pack (side = LEFT)
    L5 = Label(top, text = L05+"\n")
    L5.pack (side = LEFT)    
    top.geometry("600x600")
    top.mainloop()
