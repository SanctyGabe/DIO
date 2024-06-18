class Heroi{
    constructor(nome,idade,tipo,ataque){
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
        this.ataque = {
            mago: "usou magia",
            guerreiro: "usou espada",
            monge: "usou artes marciais",
            ninja: "usou shuriken"
        };
    }

    atacar(){
        const ataque = this.ataque[this.tipo] || "usou ataque desconhecido"
        console.log(`O ${this.tipo} atacou usando ${ataque}`);
    }

}

const ninja = new Heroi("Jhonin", 34, "ninja");
const mago = new Heroi("Sharon", 25, "mago");
const guerreiro = new Heroi("Marcia", 12,"guerreira")
ninja.atacar();
mago.atacar();
guerreiro.atacar();