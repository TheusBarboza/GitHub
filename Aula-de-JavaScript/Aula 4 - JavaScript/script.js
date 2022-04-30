const names = ['Theus', 'Larissy', 'Maísa']

console.log(names);

const personObj = {
    profession: 'Developer',
    movies: [
        'O Livro de Eli',
        'Sonic: O Filme',
    ]
}

const personObj2 ={
    ...personObj,
    Name: 'Matheus',
    gender: "Male",
    Age: 20
}


console.log(personObj2)