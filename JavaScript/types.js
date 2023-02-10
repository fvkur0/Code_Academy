// This is a scratch pad for testing script sections

console.log('This is a test')

/*
let name = "Pat"; // String Literal
let age = 31; // Number Literal
*/
let person = {
    name: 'Pat',
    age: 31
}
let isApproved =  true; // Boolean Value
let firstName = undefined;
let lastName = null;

// Dot Notation  *Default Choice
person.name = 'Joe';

// Bracet Notation
let selection = 'name';
person[selection] = 'Mary';

console.log(person)


// Arrays --------- Data structure to display a list of items

let selectedColors = ['red', 'blue'];
console.log(selectedColors);
selectedColors[2] = 'green';
console.log(selectedColors);
console.log(selectedColors[0]);
console.log(selectedColors.length);

// Functions
// Perform a task 

function greet(name, lastName) {
    console.log('Hello Motherfucker ' + name + lastName);
}

greet('Pat', ' M');
greet('Jones', ' Town');

// Calculating a value

function square(number) {
    return number * number;
}

console.log(square(2));
