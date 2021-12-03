class Delivery:

    products = ['meat', 'cheese', 'vegetables']
    #product_a = 'meat'
    #product_b = 'cheese'
    #product_c = 'vegetables'

    def __init__(self, address, product):
       self.address = address
       self.product = product
       #assert self.product == Delivery.product_a or self.product == Delivery.product_b
              #or self.product == Delivery. product_c, "We only deliver meat, cheese or vegetables"
       assert self.product in Delivery.products, "We only deliver meat, cheese or vegetables"

    def do_delivery(self):
           print('заказ выполнен')

def main():

    a = Delivery('Gagarin ST.36-215', 'vegetables')
    a1 = 1
    b1 = a1
    a1 = 2
    print(b1)

    print(a.do_delivery())


if __name__ == '__main__':
    main()
