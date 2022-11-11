
class Node{
    constructor (data){
        this.data = data
        this.next = null;
    }
}

class Sll{
    constructor(){
        this.head = null;
    }
        // Write a method that adds to the front of this Singly Linked List.
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

        // Write a method that removes from the front of this Singly Linked List. 
    removeFront(){
        if (!this.head){
            return null;
        }
        this.head = this.head.next;
        return this;
    }
}
Sll1 = new Sll()
console.log(Sll1.addFront(18))
console.log(Sll1.addFront(5))
console.log(Sll1.addFront(73))

console.log(Sll1.removeFront())
console.log(Sll1.removeFront())

