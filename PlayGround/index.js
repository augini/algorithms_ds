function Animal() {}

Animal.prototype = {
  constructor: Animal,
  eat: function () {
    console.log("nom nom nom");
  },
};

function Cat(name) {
  this.name = name;
}

Cat.prototype = Object.create(Animal.prototype);

// adding method specific to cat
Cat.prototype.meow = function () {
  console.log("meow");
};

function Bear(name) {
  this.name = name;
}

Bear.prototype = Object.create(Animal.prototype);

const small_cat = new Cat();
small_cat.eat();
small_cat.meow();

const bear = new Bear();
small_bear.eat();
