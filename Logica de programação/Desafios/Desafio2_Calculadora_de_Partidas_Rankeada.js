function calcularRankeadas(vitorias, derrotas) {
    const saldoVitorias = vitorias - derrotas;
    let nivel;
  
    if (vitorias < 10) {
      nivel = "Ferro";
    } else if (vitorias >= 11 && vitorias <= 20) {
      nivel = "Bronze";
    } else if (vitorias >= 21 && vitorias <= 50) {
      nivel = "Prata";
    } else if (vitorias >= 51 && vitorias <= 80) {
      nivel = "Ouro";
    } else if (vitorias >= 81 && vitorias <= 90) {
      nivel = "Diamante";
    } else if (vitorias >= 91 && vitorias <= 100) {
      nivel = "Lendário";
    } else if (vitorias >= 101) {
      nivel = "Imortal";
    } else {
      nivel = "Nível inválido";
    }
  
    return { saldoVitorias, nivel };
  }
  
  const vitorias = 30;
  const derrotas = 20;
  
  const resultado = calcularRankeadas(vitorias, derrotas);
  
  console.log(`O Herói tem de saldo de ${resultado.saldoVitorias} está no nível de ${resultado.nivel}`);