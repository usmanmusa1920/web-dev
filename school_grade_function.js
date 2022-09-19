function person(name, level, grade){
    if (grade >= 4.5 && grade <= 5){
      return `Weldone ${name}, you'r very lucky at this your level (${level}) you have gotten a grade of ${grade} that is awesome.`
    }
    else if (grade < 4.5 && grade >= 2){
      return `Excellent ${name}  you'r an average student of level ${level} with a grade of ${grade} which is fine.`
    }
    else if (grade > 5){
      return `Hey you ${name}, you'r over-dose ${level} student with grade of ${grade} could you imagine, that is crazy`
    }
    else{
      return `Oh! sorry ${name}, you'r unlucky at this your level (${level}) you have gotten a grade of ${grade} which is too bad!`
    }
  }
  
// console.log(person('Usman', 200, 55))
console.log(person('Usman', 200, 5))

// Node js first
const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Who are you? : ', name => {
  console.log(`Hey there i'm ${name}`);
  rl.close();
})

// Note to export a module, use this:
exports.table = function(){
    return 4 * 3;
};

// Second
// npm install prompt-sync
// const prompt = require('prompt-sync')();
// const depmt = prompt('What is you\'r department? : ');
// console.log(`My department is ${depmt}`);
