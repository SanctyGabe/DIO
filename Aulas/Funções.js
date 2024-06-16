//função basica torradeira!!
//torrar()
//function torrar(){
//    console.log("torrando pão")
//    colocarPao()
//}
//function colocarPao(){
//    console.log("colocando o pão")
//    console.log("pão colocado")
//}

//Funções são ações - nomeie-as corretamente imbecil!
//function enviarEmail(){}
//function salvarNoBancoDeDados(){}

//faça uma função para cada coisa
// função pai pra chamar todas as outras funções
//function main(){
//    getData();
//    checkValeus();
//    sendToDatabase();
//}
//função que pega todos os dadoas
//ORGANIZE ESSA BAGAÇÃ!
//function getData(){
//    console.log("Pegando dados do usuario");
//}
//logica implementada aqui
//function checkValeus(){
//    console.log("Validadndo dados...");
//}
//function sendToDatabase(){
//    console.log("Cadastrando dados dados");
//}
//main();

//function enviarDados(){}
//    let nomeDoBanco = "Banco-de-dados"
//    console.log("Salvando dados em: " + nomeDoBanco)
//        if (3 === 3) {
//            console.log("Senha validada")
//        }
//        else (3 != 3);{
//            console.log ("Senha invalida")
//        }

//------------------FUNÇOES COM PARAMETROS-----------------!!

//função que muda com o parametro
//COLOCAr AS STRINGS,PARAMETROS E TUDO MAIS EM ORDEM! Se não vai ter retrabalho!
//torrar("o ", "Gabriel", " pão de sal ")
//torrar("a ", "Sarah", " pão integral ")

//VAR = atribuição global -> não é recomendavel
//function torrar(genero, nome, pao){
//    console.log("O " + pao + "está pronto");
//    console.log("Foi um pedido d" + genero + nome);
//}

//torrar(" pão de sal ", undefined , 10.25)
//torrar(" pão integral ", " Sarah ", 10.30)

//Deixe as variaveis (no caso aqui {nome = cliente} para o final para não precisar fazer gambiarra.
//O undefined pode ser utilizado para supir uma variavel não especificada.

//function torrar( pao, nome = "cliente", valor){
//    console.log("O" + pao + "está pronto");
//    console.log("Foi um pedido de" + nome);
//    console.log("O valor do pedido foi " + valor)
//}

//base mundo real
//interpolação de string
//Valor entre `` é um texto com vaiaveis no meio, variaveis essas representadas por ${}
//createStringConnection("nu_app", "Gabriel", "5550")

//function createStringConnection(databeseName, user, pass){
//    console.log(`connect:NUPRODUCTS;user=${user};pass=${pass};initial_database=${databeseName}`)
//}

//------------------FUNÇOES COM retorno-----------------!!
//let resultado = soma(5,5)

//console.log("O resultado da função é " + resultado)

//function soma(numA, numB){
//    let somatorio = numA + numB
//    return somatorio
//}
let userName = getFirstName ("Gabriel Santos", " ")
console.log("Seja bem vindo " + userName + " como posso ajudar hoje?")

userName = getFirstName ("Gah-Santos", "-")
console.log("Seja bem vindo " + userName + " como posso ajudar hoje?")

function getFirstName(name, splitChar = " "){
    let firstName = name.split(splitChar)[0]
    return firstName
}