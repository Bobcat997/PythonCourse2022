class dog:
    pass

    def __init__(self, name, coat_color, bread_of_dog):
        self.name = name
        self.coat_color = coat_color
        self.bread_of_dog = bread_of_dog

    def how(self):
        print(f'{self.name} How How')

    def tail_whip(self):
        print(f'{self.name} whips his tail')


kratos = dog('Kratos', 'brązowy', 'Owczarek niemiecki')
kratos.how()
kratos.tail_whip()


