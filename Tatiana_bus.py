#tatiana, no angusties y mejor anda a una cafeteria ._.
cafe_trr = 4000
cafe_cm = 2000
transp = 1600
tatiana_plata = 20000

camp = tatiana_plata - (cafe_cm*2) - (transp * 2)
trra = tatiana_plata - (cafe_trr * 2) 

if camp < trra:
    print("la opcion mas economica para tatiana es campanario, ya que le sobran ", camp , "pesos" )
elif trra < camp:    
    print("la opcion mas economica para tatiana es terraplaza, ya que le sobran ", trra , "pesos" )
else:
    print("los costos dan igual, q cafe tan caro, y el transporte tmb, asi que vaya donde sea, va a gastar la misma vaina.")