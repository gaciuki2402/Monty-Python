class Comrade_Dishes():
    def Details(self):
        self.foods={
            "Githeri":70,
            "Rice":50,
            "Ugali":20,
            "Beans":30,
            "Chapati":15,
            "Pojo":30,
            "Fish":150,
            "Beef":80,
            "Pilau":100,
            "Chips":90,
            "Sausage":30
        }
    def Available_Foods(self):
        print(f"...FOODS BELOW FIFTY BOB...")
        for food in self.foods:
            price=self.foods[food]
            if price>=50:
                continue
            print(f"{food}...{price}")
        print(f"...FOODS ABOVE FIFTY BOB...")
        for food in self.foods:
            price=self.foods[food]
            if price<=50:
                continue
            print(f"{food}...{price}")












f1=Comrade_Dishes()
f1.Details()
f1.Available_Foods()