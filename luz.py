def estado_luz(status):
    match status:
        case "luz ligada":
            return "on"
        case "luz apagada":
            return "off"
        case "luz piscando":
            return "blink"
        case _:
            return "estado desconhecido"
        
print(estado_luz("luz piscando"))