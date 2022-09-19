// ES6 function
x = (e, b) => e * b;
console.log("2 * 7 =", x(2, 7))


// Normal function
function x(e, b){
  // console.log(`The multiple of ${e} and ${b} is ${e * b}`);
  return e * b;
}
console.log(x(2, 7))


// function with arbitrary number of arguments
function m(...args){
  console.log(`We have ${args} in the list`);
  return args;
}
console.log(m(7, 0, 8))
