tpl = ("привет", "шалаш", "мир", "потоп", "финиш", "кабак", "ротатор")
print(list(filter(lambda x: x if x[::] == x[-1::-1] else None, tpl)))
