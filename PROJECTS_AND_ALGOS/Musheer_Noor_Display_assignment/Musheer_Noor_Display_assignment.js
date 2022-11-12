
class Node{
    constructor(data){
        this.data = data;
        this.next = null;
    }
}

class Sll{
    constructor(){
        this.head = null
    }

    addFront(value){
        let new_node = new Node(value);
        if (!this.head){
            this.head = new_node;
            return this;
        }
        new_node.next = this.head;
        this.head = new_node;
        return this;
    }

    removeFront(){
        if (!this.head){
            return null;
        }
        this.head = this.head.next;
        return this;
    }

    returnFront(){
        if (!this.head){
            return null;
        }
        return this.head.data;
    }

    contains(value){
        let runner = this.head;
        let match = false;
        while (runner !== null){
            if (value == runner.data){
                match = true;
                return match;
            }
            runner = runner.next;
        }
        return match;
    }

    length(){
        let size = 0;
        let runner = this.head;
        while (runner !== null){
            size ++;
            runner = runner.next;
        }
        return size;
    }

    // Create display() that uses a while loop and a runner to return a string containing all list values. Build what you wish console.log(myList) did!
    display(){
        let myList = [];
        let runner = this.head;
        while (runner !== null){
            myList.push(runner.data);
            runner = runner.next;
        }
        return myList
    }

}

Sll1 = new Sll()
console.log(Sll1.addFront(18))
console.log(Sll1.addFront(5))
console.log(Sll1.addFront(73))
console.log(Sll1.addFront(22))
console.log(Sll1.addFront(-80))
console.log(Sll1.addFront(65))

console.log(Sll1.display())



