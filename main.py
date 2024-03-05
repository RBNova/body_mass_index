print("VÜCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI")

boy = float(input("Boy (m):"))
kilo = float(input("Kilo (kg):"))

indeks = kilo / (boy*boy)

if indeks <= 18:
    print("\n zayıf VKİ:{}".format(indeks))

elif indeks > 18 and indeks <= 25:
    print("\n normal VKİ:{}".format(indeks))

elif indeks > 25 and indeks <= 30:
    print("\n kilolu VKİ:{}".format(indeks))

elif indeks > 30 and indeks < 35:
    print("\n obez VKİ:{}".format(indeks))

elif indeks >=35:
    print("\n ciddi obez VKİ:{}".format(indeks))