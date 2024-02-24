DOMAIN = "lantick"


def setup(hass, config):
    hass.states.set("lantick.licznik1", "10")

    return True