//Objeto o que é -> é toda representação. TUDO  
class formaDeBolo{
    //contructor != JSON pq tambem guarda funções e comportamentos
    constructor(saborDaMassa, saborRecheio){
        //this é o mesmo que let só que para class
        this.saborDaMassa = saborDaMassa
        this.saborRecheio = saborRecheio
    }
    escrever(){
        console.log(`Um delicioso bolo de ${this.saborDaMassa} com recheio de ${this.saborRecheio}`)
    }
    
}

let boloFesta = new formaDeBolo("massa de mandioca", "recheio de queijo")
let boloPremium = new formaDeBolo("massa de baunilha", "recheio de morango")


boloFesta.escrever()
boloPremium.escrever()