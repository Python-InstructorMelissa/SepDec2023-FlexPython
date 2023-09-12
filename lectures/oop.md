```javascript
// Class = A group of things that contains similar properties / A Blueprint of what you want to build / ON a spread sheet  the parameters (contructors) are the columns and the objects (rows)


class Animal {
    constructor(name, species, appendages, classification, diet) {
        this.name = name
        this.species = species
        this.appendages = appendages
        this.classification = classification
        this.diet = diet
        this.willToLive = true
        this.sound = ''
        this.isDead = false
    }
    produceProduct(prodName, cost){
        return new Product(prodName, cost, this)
    }
    feedAnimal(){
        if (this.isDead) {
            console.log("Sorry", this.name, "has passed away :(")
        }
        else {
            console.log(this.name, "ate", this.diet, 'and has lived to see another day')
            return this
        }
    }
    makeNoise(noise){
        if (this.isDead) {
            console.log("Sorry", this.name, "has passed away :(")
        }
        else {
            this.sound = noise
            console.log(this.name, 'learned how to make the noise', this.sound)
            return this
        }
    }
    refuseToEat(){
        if (this.isDead) {
            console.log("Sorry", this.name, "has passed away :(")
        }
        else {
            this.willToLive = false
            this.isDead = true
            console.log(this.name, 'refused to eat and has died')
            return this
        }
    }
    fight(other){
        if (this.isDead && other.isDead) {
            console.log('The zombie war is on, tune in next week!!')
        }
        else if(this.isDead) {
            console.log(other.name, 'won by default')
        }
        else if(other.isDead) {
            console.log(this.name, 'won by default')
        }
        else {
        console.log(this.name, 'fought', other.name, 'and won')
        }
    }
}

class Product {
    constructor(prodName, cost, producer) {
        this.prodName = prodName
        this.cost = cost
        this.producer = producer
    }
    printInfo(){
        console.log(this.producer.name, 'creates', this.prodName, 'for a cost of $'+this.cost)
    }
}

// Creating an Animal
let bee = new Animal("Lily", "HoneyBee", 6, 'Insect', 'nectar')
let panda = new Animal("Jason", "Panda", 4, 'Mammal', 'Bamboo')
bee.feedAnimal().makeNoise('buzz').feedAnimal().refuseToEat()
panda.refuseToEat()

// let honey = new Product("Honey", 'Free', bee)
// honey.printInfo()
panda.produceProduct('Alcohol', '10').printInfo()
bee.fight(panda)



```
