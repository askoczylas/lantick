DOMAIN = "lantick"


def setup(hass, config):
    
    liczniki = [1, 2, 3]
    for x in liczniki:
        hass.states.set("ais_hello.licznik" + str(x), x*5)

    return True
