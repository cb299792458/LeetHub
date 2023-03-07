class MyQueue {
    constructor(){
        this.input = [];
        this.output = [];
    }
    
    push(e){
        this.input.push(e);
    }
    
    pop(){
        if(!this.output.length) this.reverse();
        return this.output.pop();
    }
    
    peek(){
        if(!this.output.length) this.reverse();
        return this.output.at(-1);
    }
    
    empty(){
        return !this.output.length && !this.input.length;
    }
    
    reverse(){
        while(this.input.length){
            this.output.push(this.input.pop());
        }
    }
}