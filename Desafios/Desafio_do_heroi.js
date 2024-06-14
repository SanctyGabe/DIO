//Classificação de todos os rankings de acordo com o XP
let nome = "Sancty"
let xp = 3000
//Tive alguma dificuldade com a parte de `` e $ mas isso possivelmente eu vou aprender no curso de JS
if (xp <= 1000){
    console.log(`O Herói de nome ${nome}, está no nivel de Ferro`);
} else if (xp >= 1001 && xp < 2000){
    console.log(`O Herói de nome ${nome}, está no nivel de Bronze`);
} else if (xp >= 2001 && xp < 5000){
    console.log(`O Herói de nome ${nome}, está no nivel de Prata`);
} else if (xp >= 5001 && xp < 7000){
    console.log(`O Herói de nome ${nome}, está no nivel de Ouro`);
} else if (xp >= 7001 && xp < 8000){
    console.log(`O Herói de nome ${nome}, está no nivel de Platina`);
} else if (xp >= 8001 && xp < 9000){
    console.log(`O Herói de nome ${nome}, está no nivel de Ascendente`);
} else if (xp >= 9001 && xp < 1000){
    console.log(`O Herói de nome ${nome}, está no nivel de Imortal`);
} if (xp >= 10000){
    console.log(`O Herói de nome ${nome}, está no nivel de Radiante`)
}