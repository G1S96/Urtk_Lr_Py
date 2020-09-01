d = {
                "Алексеев":[13000,"male"],
                "Горбачёва":[14000,"female"],
                "Осипов":[15000,"male"],
                "Илясова":[9000,"female"],
                "Маслов":[24000,"male"],
                "Авдеева":[18000,"female"],
                "Куликов":[7000,"male"],
                "Борисова":[25000,"female"],
                "Сафонов":[200000,'male'],
                "Волкова":[17000,'female'],
 }
for gon in sorted(d.items(),key=lambda para:para[1]):
    if gon[1][1] == "male":
            print(gon)

