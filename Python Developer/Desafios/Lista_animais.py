def identificar_animal(caracteristica1, caracteristica2, caracteristica3):
    animais = {
        "vertebrado": {
            "ave": {
                "carnivoro": "aguia",
                "onivoro": "pomba"
            },
            "mamifero": {
                "onivoro": "homem",
                "herbivoro": "vaca"
            }
        },
        "invertebrado": {
            "inseto": {
                "hematofago": "pulga",
                "herbivoro": "lagarta"
            },
            "anelideo": {
                "hematofago": "sanguessuga",
                "onivoro": "minhoca"
            }
        }
    }

    try:
        return animais[caracteristica1][caracteristica2][caracteristica3]
    except KeyError:
        return "Animal não listado"

caracteristica1 = input().strip().lower()
caracteristica2 = input().strip().lower()
caracteristica3 = input().strip().lower()

resultado = identificar_animal(caracteristica1, caracteristica2, caracteristica3)
print(resultado)