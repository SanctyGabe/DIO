let invoice ={
    name: "gabriel",
    age: 26,
    products: {
        0: ["Pamonha", 20],
        1: ["Pizza congelada", 20],
        2: ["Feijão", 9.99]
    }
}

generateInvoice (invoice)

function generateInvoice(invoice){
    console.log (`O comprador é ${invoice.name}`)
    console.log (`A idade é ${invoice.age}`)
    console.log ("---------------------")

    for(const index in invoice.products){
        const [productName, productPrice] = invoice.products[index]
        console.log (`${productName}:${productPrice}`)
    }

}