

function pizzaOven(crustType, sauceType, cheeses, toppings){
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}
var p1 = pizzaOven("deep dish", "traditional", ["mozzarella"],["pepperoni", "sausage"]);
console.log(p1);

var p2 = pizzaOven("Hand Tossed", "Marinara", ["mozzarella", "feta"],["mushrooms", "olives", "onions"]);
console.log(p2);

var p3 = pizzaOven("thin crush", "alfredo sauce", ["mozzarella"],["pineapple", "jalapeno"]);
console.log(p3);

var p4 = pizzaOven("Hand Tossed", "pesto", ["mozzarella", "feta"],["basil", "chicken", "onions"]);
console.log(p4);


//Bonus Challenge: Create a function called randomPizza that uses Math.random() to create a random pizza!


var pizzaOptions = {
        crustType : ["hand-tossed", "deep dish", "thin"],
        sauceType : ["traditional", "alfredo", "marinara", "pesto"],
        cheeses : ["mozarella", "cheddar", "feta"],
        toppings :["pepperoni", "pineapple", "jalapeno", "onion", "mushrooms", "chicken", "olives"]
};
var randChoice = [
        Math.floor((Math.random() * pizzaOptions.crustType.length)), 
        Math.floor((Math.random() * pizzaOptions.sauceType.length)), 
        Math.floor((Math.random() * pizzaOptions.cheeses.length)), 
        Math.floor((Math.random() * pizzaOptions.toppings.length))
];

console.log(randChoice);


function createRandomPizza(){
    var randomPizza = {};
    randomPizza.crustTypeR = pizzaOptions.crustType[randChoice[0]];
    randomPizza.sauceTypeR = pizzaOptions.sauceType[randChoice[1]];
    randomPizza.cheesesR = pizzaOptions.cheeses[randChoice[2]];
    randomPizza.toppingsR = pizzaOptions.toppings[randChoice[3]];
    return randomPizza;
}
console.log(createRandomPizza());
