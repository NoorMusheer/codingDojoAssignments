
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

    // Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.
    returnFront(){
        if (!this.head){
            return null;
        }
        return this.head.data;
    }

    // Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.
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
}
Sll1 = new Sll()
console.log(Sll1.addFront(18))
console.log(Sll1.addFront(5))
console.log(Sll1.addFront(73))
console.log(Sll1.addFront(22))
console.log(Sll1.addFront(-80))
console.log(Sll1.addFront(65))


console.log(Sll1.contains(30))


