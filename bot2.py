# -*- coding: utf-8 -*-

import tweepy, time, sys, random, subprocess

subprocess.call("clear")
print(" _____                 ______         _                    ")
print("|_   _|                | ___ \       | |                   ")
print("  | |  __      __  ___ | |_/ /  ___  | |_     _ __   _   _ ")
print("  | |  \ \ /\ / / / _ \| ___ \ / _ \ | __|   | '_ \ | | | |")
print("  | |   \ V  V / |  __/| |_/ /| (_) || |_  _ | |_) || |_| |")
print("  \_/    \_/\_/   \___|\____/  \___/  \__|(_)| .__/  \__, |")
print("                                             | |      __/ |")
print("                                             |_|     |___/ ")
print("............................................................")
print("|  Manuel Jesús Flores  |  Twitter: @majeflomon | Ver. 001 |")
print("............................................................")
print(" ")
print("Selecciona una de las siguientes opciones")
print("-------------------------------------------------")
#Opciones
print("1 -> Enviar nombres y apellidos aleatorios\n")
print("2 -> Tweet Correos Electrónicos\n")
print("3 -> Escribir un mensaje personalizado (EN DESARROLLO) \n")
print("4 -> Salir de la aplicación\n")
opcion = raw_input("Indique la opción deseada: ")

#KEYS
CONSUMER_KEY = 'introduzca la clave acá'
CONSUMER_SECRET = 'introduzca la clave acá'
ACCESS_KEY = 'introduzca la clave acá'
ACCESS_SECRET = 'introduzca la clave acá'


#BOT NOMBRES ALEATORIOS

numero = 0

nombres_hombre = ["Arne", "Bjorn", "Per", "Knut", "Terje", "Erik", "Kjell", "Jan", "Rolf", "Gunnar", "Grete", "Berit", "Marit", "Randi", "Kristin", "Karin", "Anja", "Embla", "Hilda", "Silje", "Mechelle", "Sydney", "Amaya", "Donovan", "Leilani", "Dale", "Laura", "Dean", "Marsden", "Cally", "Marsden", "Buckminster", "Anjolie", "Ethan", "Troy", "Gail", "Bevis", "Erasmus", "Craig", "Rose", "Erasmus", "Levi", "Eliana", "Yuli", "Felix", "Quincy", "Venus", "Cole", "Marsden", "Adele", "Amity", "Denton", "Rose", "Knox", "Valentine", "Garrett", "Quentin", "Henry", "Gloria", "Georgia", "Violet", "Owen", "Jayme", "Slade", "Joelle", "Abel", "Leo", "Sandra", "Demetrius", "Breanna", "Murphy", "Jaime", "Kadeem", "Marvin", "Valentine", "Allen", "Xaviera", "Sarah", "Phelan", "Angela", "Hayes", "Dacey", "Martha", "Hamilton", "Cassidy", "Asher", "Merritt", "Sylvester", "Mira", "Aspen", "Baxter", "Tamekah", "Aurora", "Oleg", "Christian", "Summer", "Sade", "Rina", "Philip", "Jerome", "Illana", "David", "Timon", "Yuri", "Fiona", "Harper", "Brenden", "Herrod", "Amity", "Lester", "Kato", "Kyla", "Demetria", "Baker", "Amir", "Jaquelyn", "Gareth", "Porter", "Susan", "Lillian", "Prescott", "Oren", "Rinah", "Brandon", "Chiquita", "Perry", "Veda", "Jasmine", "Coby", "Courtney", "Marcia", "Victoria", "Lydia", "Faith", "Sybill", "Idola", "Uriel", "Clio", "Clark", "Uta", "Ian", "Tatyana", "Rafael", "Keiko", "Colorado", "Venus", "Maxine", "Daphne", "Graham", "Steel", "Jane", "Vernon", "Myra", "Anika", "Cadman", "Unity", "Larissa", "Tanek", "Ciaran", "Alfonso", "Christian", "Venus", "Devin", "Ramona", "Irene", "Benjamin", "Dahlia", "Arden", "Jessica", "Shelby", "Indigo", "Beau", "Lester", "Callum", "Vera", "Steel", "Michelle", "Wang", "Adam", "Victor", "Quincy", "Abdul", "Prescott", "Ryan", "Jonas", "Kevyn", "Darius", "Gil", "Seth", "Reed", "Yeo", "Hector", "Judah", "Erasmus", "Gay", "Luke", "Fallon", "Abdul", "Ulysses", "Kyle", "Mannix", "Ila", "Bradley", "Omar", "Isaac", "Jason", "Pamela", "Noah", "Charity", "Brett", "Idola", "Breanna", "Dane", "Ora", "Priscilla", "Jena", "Louis", "Sophia", "Georgia", "Latifah", "Naomi", "Iris", "Grant", "Erica", "Marsden", "Isabelle", "Stella", "Lars", "Salvador", "Dana", "Beverly", "Jordan", "Sierra", "Dacey", "Irene", "Kerry", "Colt", "Hakeem", "Alana", "Quincy", "Julian", "Walter", "Peter", "Prescott", "Bevis", "Cheryl", "Nadine", "Dominique", "Beatrice", "Camille", "Pamela", "Margaret", "Brendan", "Roary", "Bree", "Trevor", "Josephine", "Blossom", "Allistair", "Prescott", "Mechelle", "Sierra", "Whitney", "Lucy", "Bree", "Rhona", "India", "Athena", "Neil", "Haviva", "Stephanie", "Basil", "Aladdin", "Brennan", "Gemma", "Christine", "Jescie", "Fuller", "Avye", "Amy", "Kylee", "Graiden", "Levi", "Jana", "Malachi", "Trevor", "Bryar", "Medge", "Fuller", "Velma", "Karen", "Mari", "Rooney", "Josiah", "Ralph", "Christian", "Trevor", "Flynn", "Salvador", "Holmes", "Macey", "Chantale", "Barrett", "Stuart", "Lana", "Jada", "Serena", "Orlando", "Alexander", "Hadley", "Logan", "Bradley", "Jenette", "Wylie", "Lacey", "Ella", "Erica", "Elmo", "Prescott", "Stephen", "Sigourney", "Cameran", "Harlan", "April", "Amal", "Damian", "Sawyer", "Ignatius", "Colby", "Sebastian", "Yuli", "Eagan", "Chaim", "Dana", "Yetta", "Caesar", "Hakeem", "Kieran", "Mohammad", "Jemima", "Florence", "Faith", "Dylan", "Sophia", "Stuart", "Chava", "Kelsie", "Jason", "Harlan", "Signe", "Jermaine", "Zelda", "Zane", "Demetria", "Lewis", "Maris", "Dana", "Dexter", "Elliott", "Flynn", "Daquan", "Quin", "Barbara", "Karina", "Eleanor", "Lavinia", "Gavin", "Porter"]

apellidos = ["Erickson", "Voll", "Andersen", "Dahl", "Landvik", "Nielsen", "Christiansen", "Holt", "Solberg", "Skjeggestad", "Caldwell", "Mendez", "Atkinson", "Velasquez", "Erickson", "Hammond", "Freeman", "Gomez", "Reese", "Clark","Singleton", "Irwin", "Christian", "Mcneil", "Mercer", "Dorsey", "Cabrera", "Morin", "Cooper", "Murray","Nielsen", "Boone", "Nielsen", "Burks", "Fulton", "Castaneda", "Chavez", "Aguilar", "Navarro", "Goodwin","Santana", "Vega", "Garner", "Pruitt", "Reid", "Brock", "Conley", "Bridges", "Griffin", "Ayala","Mccormick", "Rocha", "Foley", "Conrad", "Holman", "Hays", "Yang", "Burris", "Lott", "Lawrence","Guerrero", "Parrish", "Gillespie", "Foley", "Kemp", "Davidson", "Gibson", "Callahan", "Townsend", "Preston","Norris", "Hinton", "Lloyd", "Wallace", "Langley", "Ware", "Nicholson", "Hays", "Avila", "Cervantes","Sims", "Todd", "Booker", "Roach", "Griffin", "Rodriguez", "Santos", "Russell", "Leonard", "Clements","Slater", "Velazquez", "Bernard", "Swanson", "Avila", "Daugherty", "Walter", "Huff", "Hudson", "Meyers","Dunlap", "Wooten", "Potter", "Randall", "Brooks", "Saunders", "Glenn", "Jones", "Perry", "Pugh","Acosta", "Sanford", "Townsend", "Sharpe", "Jensen", "Hanson", "Caldwell", "Langley", "Cardenas", "Wilcox","Forbes", "Graves", "Morales", "Abbott", "Lee", "Hendrix", "Olson", "Soto", "Newton", "Armstrong","Calderon", "Moran", "Wood", "Christensen", "Puckett", "Hooper", "Dyer", "Diaz", "Sellers", "Tate","Lawson", "Dickson", "Rowe", "Mason", "Le", "Mcdaniel", "Britt", "Buckner", "Orr", "Jensen","Myers", "Blanchard", "Cherry", "Woodard", "Williamson", "Bruce", "Rodriquez", "Kaufman", "Schneider", "Montoya","Larson", "Petersen", "Mcpherson", "Perkins", "Flores", "Callahan", "Huff", "Stanton", "Cox", "Gay","Mcmillan", "Hernandez", "Sanders", "Gregory", "Yang", "Frye", "West", "Mack", "Burton", "Stafford","Gaines", "Fleming", "Mclaughlin", "Bass", "Monroe", "Lindsey", "Montoya", "Nieves", "Valencia", "George","Jimenez", "Nguyen", "Beard", "Phillips", "Benjamin", "Chavez", "Buckley", "Key", "Noel", "Downs","Moody", "Allen", "Hooper", "Pugh", "Dunlap", "Wilkerson", "Butler", "Haney", "Barrett", "Warner","Fernandez", "Horn", "Baker", "Ford", "Pena", "Tran", "Cherry", "Justice", "Kelly", "Lester","Cox", "Murphy", "Anderson", "Harper", "Hurst", "Delgado", "Jackson", "Serrano", "Burch", "Heath"]

# AUTENTICACIÓN TWITTER    
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

#Bot TXT
#filename = open(argfile, 'r')
#f = filename.readlines()
#filename.close()

#Bot Horario
hora = time.strftime("%H:%M")
hour = hora+" en Sevilla"

#Crear tweet
#while 1 == 1:
    #print("[+] Tweeting something...")
    #api.update_status(status = result)
    #print("[+] Tweet: "+ result)
    #time.sleep(60)  

#OPCIONES APLICACIÓN

if opcion == "4":
        
    print("Hasta otro momento!")
    time.sleep(1)
    sys.exit(0)
    
if opcion == "3":
    print("Opción en desarrollo")
    sys.exit(1)
    
cantidad = int(input("Cuantas veces quieres que se envien Tweets?: "))

#ALEATORIO
while numero < cantidad:
    name = random.choice(nombres_hombre)
    surname = random.choice(apellidos)
    result = name+" "+surname 

#if opcion == "3":
#    mensaje = raw_input("Indique su mensaje: ")
#    while numero < cantidad:
#            msj_final = mensaje+". Escrito por el bot "+result
#            api.update_status(status = msj_final)
#            print("[+] Tweet: "+ msj_final)
#            numero += 1
#            time.sleep(1)
    
while numero < cantidad:
    print("[+] Tweeting something...")
    
    if opcion == "1":

        api.update_status(status = result)
        print("[+] Tweet: "+ result)
        numero += 1
        time.sleep(1)

    elif opcion == "2":
        
        correo = name+"_"+surname+"@hola"
        api.update_status(status = correo)
        print("[+] Tweet: "+ correo)
        numero += 1
        time.sleep(1)
        
    else:
        print("Asegurate de escoger bien la opción")
