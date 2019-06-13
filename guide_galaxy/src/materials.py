def discovery_material_price(arabic_result, final_result):
    if float(arabic_result) and float(final_result):
        return (final_result - arabic_result) / arabic_result
    raise ValueError('invalid values')


def discovery_material_sale(arabic_value, material_price):
    if float(arabic_value) and float(material_price):
        return arabic_value + (arabic_value * material_price)
    raise ValueError('invalid values')


class Material():
    def __init__(self, name, price):
        materials = ['silver', 'iron', 'gold', 'dirt']
        if float(price) and name in materials:
            self.name = name
            self.price = float(price)
            return
        raise ValueError('invalid values')
