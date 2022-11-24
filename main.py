import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self,name: str,price: float,quantity=0):
        #run validations to received arguments
        assert price >= 0,f"Price {price} is not greater than zero!"
        assert quantity >= 0,f"Quantity {quantity} is not greater than zero!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price=self.price*self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            print(reader,'print reader')
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # for i.e 5.0,10.0
        if isinstance(num,float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:

            return False


    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

phone1 = Item("jscPhonev10",500,5)
phone1.broken_phones=1
phone2 = Item("jscPhonev20",700,5)
phone2.broken_phones=1




