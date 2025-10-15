list_1=[پدرخوانده,جوکر,تر لکتر,مافيا ساده]
list_2[دکتر,حرفه اي,ارآگاه,جان سخت,روانپزشک,فروشنده,کونستانتين,افيا ساده,]
roles = [r.strip() for r in list_1input.split(',')]
players = [p.strip() for p in list_2input.split(',')]
if len(list_1) !=len(list_2):
    print("تعداد بازيکن و نقش ها برابر است")
   exit()
random.shuffle(players)
