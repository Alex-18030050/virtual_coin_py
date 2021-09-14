# coins
bitcoin = 51786
ethereum = 3922
cardano = 2907609
binance_coin = 500.71	
dogecoin = 0.312183
ada = 2.59
# usa to mxn 
usd = 19.92
#
pesos = float(input("Ingresa la cantidad de pesos mexicanos: ")) 
print("""
A cual moneda se desea convertir el valor?
1. Dolar Estadounidense
2. Bitcoin
3. Ethereum
4. Cardano
""")
opcion = int(input("Selecciona una opcion: "))
if opcion == 1:
    dolares = round(pesos/usd, 2)
    print("USD: ", dolares)
elif opcion == 2:
    mybitcoin = usd/bitcoin
    print("Bitcoin: ", mybitcoin)
elif opcion == 3:
    myeth = usd/ethereum
    print("Ethereum: ", myeth)
elif opcion == 4:
    myada = usd/ada
    print("ADA: ", myada)
else:
    print("Ingresa la opcion entre 1-4")