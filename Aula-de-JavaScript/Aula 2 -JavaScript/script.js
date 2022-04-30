// <--- Utilizado para comentários, utilizado para anotações - comentário de uma linha
/* <--- Comentário
        de multilinhas */
    
// var type boolean true | false

var isEnabled = true;
var test = 'false';

console.log(isEnabled)
console.log(test)


// array - index

var names = ['Matheus', 'Larissy'];
console.log(names)
console.log(names[2])

names.push('Maísa')  // matriculou o aluno
console.log(names.length)

var teams = new Array();
teams.push('Brasil')
console.log(teams)

// IF - condicional

function testName(name) {
    if(name.length > 10){
        return 'Nome grande'
    } else {
        return 'Nome pequeno'
    }
}

function isEqual(name){
    if(name === 'Matheus'){
        return 'É igual a Miguel'
    } else if (name === 'Maria') {
        return 'É igual a Maria'
    } else {
        return "não é igual a nada"
    }
    console.log('Opaa')
}

console.log(testName('Matheus'))

console.log(isEqual('Maria'))