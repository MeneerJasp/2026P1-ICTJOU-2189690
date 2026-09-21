def kwadraat(getal):
    return getal * getal


def bmi_uitrekenen(lengte, gewicht):
    '''
    Berekent de BMI aan de hand van lengte en gewicht

    args:
    - lengte : lengte is in meters
    - gewicht : gewicht is in kilo's
    '''

    lengte_kwadraat = kwadraat(lengte)
    bmi = gewicht / lengte_kwadraat
    return bmi

bmi_test = bmi_uitrekenen(1.93, 93)
print(bmi_test)