import tkinter as tk
import random

# Lista di parole di esempio
parole = ["dio porco",
                     "dio cane",
                     "dio mucca",
                     "dio delfino",
                     "dio rinoceronte",
                     "dio leone",
                     "dio ghepardo",
                     "dio maiale",
                     "dio cavallo",
                     "dio medusa",
                     "dio gatto",
                     "dio pappagallo",
                     "dio ape",
                     "dio aquila",
                     "dio aligatore",
                     "dio anaconda",
                     "dio anguilla",
                     "antilope",
                     "dio rana",
                     "dio leopardo",
                     "dio pesce palla",
                     "dio lombrico",
                     "dio narvalo",
                     "dio scoiattolo",
                     "dio pipistrello",
                     "dio iguana",
                     "dio lucertola",
                     "dio pinguino",
                     "dio koala",
                     "dio dromedario",
                     "dio cammello","dio cigno","dio papera","dio anatra","dio piccione","dio gabbiano","dio talpa","dio quaglia","dio giraffa","dio salmone","dio muflone","dio ragno","dio macaco","dio cacatua","dio ermellino","dio fagiano","dio coyote","dio granchio","dio gallo","dio gallina","dio grillo","dio ippopotamo","dio castoro","dio cobra","dio cervo","dio cicala","dio bovino","dio suino","dio foca","dio avvoltoio","dio trota","dio zebra","dio struzzo","dio fenicottero","dio renna","dio scorpione","dio merlo","dio tenia","dio suricato","dio rospo","dio dingo","dio pellicano","dio ocelot","dio lamantino","dio montone","dio nautilus","dio termosifone","dio topo","dio televisore","dio tastiera","dio telefono","dio fucile","dio telecomando","dio ambulanza","dio foglio","dio elica","dio bluetooth","dio mafioso","dio orologio","dio testicolo","dio banana","dio limone","dio pera","dio romano","dio obeso","dio batteria","dio fiat panda","dio coreano","dio malato","dio pompa","dio benzinaio","dio pedofilo","dio aspirapolvere","dio asciugamano","dio bilancia","dio nasale","dio anale","dio orale","dio putrefatto","dio impestato","dio microbo","dio imbalsamato","dio frusto","dio ascella","dio mignolo","dio scarpa","dio mutanda","dio brufolo","dio fango","dio infangato","dio merda","dio calendario","dio impolverato","dio prolunga","dio materasso","dio squalo","dio mondo","dio vino","dio vaso","dio sgabello","dio tovagliolo","dio nucleare","dio boia","dio ratto","dio cartello","dio topo","dio bidè","dio radice","dio immerdato","dio rimini","dio zappa","dio morto","dio negro","dio anziano","dio villano","dio ventilatore","dio stampante","dio pesticida","dio usurato","dio albero","dio zoofilo","dio pedofilo","dio feticista","dio vespa","dio calabrone","dio vagina","dio transgender","dio sole","dio comunista","dio nazista","dio fascista","dio dittatore","dio allungato","dio pressato","dio vinile","dio dvd","dio telecamera","dio mensola","dio lampadario","dio quadro","dio alterato","dio pisano","dio genovese","dio melone","dio smerdone","gesù con un tumore ai testicoli","gesù bestemmiato ladro","dio ladro","madonna puttana","gesù appeso per il cazzo","gesù mafioso ladro","gesù cagante bastardo","gesù duracel","dio duracel","dio energiser","gesù femboy","gesù hadicappato","gesù sofferente","madonna sverginata","maria vergine implosa","gesù cartolaio","dio mensola","dio trapano","dio scazzato","gesù masochista","dio polmone","gesù negro","madonna sboldra bastarda","dio glorioso","dio crudele","dio feroce","dio abissale","dio leggendario","dio fragile","dio ardente","dio lacerante","dio trionfante","dio oscillante","dio folle","dio che scopa","dio strafotente","dio scarico","dio stufo","madonna futanari","gesù con il cazzo corto","gesù dal cazzo negro","dio clistere anale","cristo pompinaro","geova bastardo","madonna scostumata","padre pio infertile","cristo inculato","madonna bagascia","geova maiale","gesù sgommato","dio sgommato","geova sgommato","bastarda la madonna","gesù drogato","cristo rotto in culo","gesù abusivo","geova abusivo","dio abusivo","madonna abusiva","noè zoofilo","madonna sbuccia cazzi","geova rincoglionito","gesù putrido","dio catamarano","gesù con i coglioni  bucati","il papa alcolizzato","dio babbuino","dio imputridito","tutti i santi bastardi","dio boia","dio smerdante","dio assurdo","dio mogano","dio ghiaia","gesù scalzo in una valle di chiodi", "madonna sborrata", "madonna a pecora", "madonna a novanta", "dio inculato da un orda di unni", "madonna stuprata dagli accadi", "gesù leccatore di cappelle sumere", "dio con la schiena sborrata", "gesù incula bambine", "madonna divoratrice di dildi, cristo venditore di rose toy", "dio caraffa, dio giams", "dio scavatore di buche", "madonna perforatrice di mucche", "gesù falegname", "gesù costruttore di croci", "dio scopritore di caverne", "gesù farcitore", "madonna guidatrice di cazzi", "porco dio impennato", "gesù nei campi di cotone", "Madonna imbalsamata","anubi","la madonna introiata bastarda","dio con lo scroto pendente","gesù svuota palle","il dio cane egiziano circoinciso orfano stronzo"]
 

# Contatore
contatore = 0

# Funzione per generare una parola e aggiornare il contatore
def genera_parola():
    global contatore
    parola = random.choice(parole)
    contatore += 1
    output_label.config(text=parola)
    contatore_label.config(text=f"BESTEMMIE: {contatore}")

# Creazione GUI
root = tk.Tk()
root.title("BOTOKU SIMULATOR")
root.geometry("700x400")
root.configure(bg="green")  # Sfondo chiaro per contrasto con il testo nero

# Etichetta del titolo con sfondo uguale alla finestra e testo nero
title_label = tk.Label(root, text="BOTOKU SIMULATOR", font=("Arial", 30, "bold"), bg="green", fg="black")
title_label.pack(pady=10)

# Bottone con sfondo bianco e testo nero
genera_button = tk.Button(root, text="tira un bestemmione", command=genera_parola, bg="darkred", fg="black")
genera_button.pack(pady=15)

# Etichetta per la parola generata con sfondo uguale alla finestra e testo nero
output_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center", bg="green", fg="black")
output_label.pack(pady=20)

# Etichetta del contatore con sfondo uguale alla finestra e testo nero
contatore_label = tk.Label(root, text="BESTEMMIE: 0", font=("Arial", 12), bg="green", fg="black")
contatore_label.pack(pady=10)

root.mainloop()
