// "Scope" refers to where a variable is allowed to be used
/*
 A variable only lives inside the block where it was created. A block is anything inside curly braces
*/

// variable inside a function
fn my_function() {
    let message = "Hello!";
    println!("{}", message); // message variable can be accessed from here
}


fn main() {
    my_function();
    // println!("{}", message); // rustc says: Not found in this scope

    // variable inside a block
    let score = 80;

    if score > 50 {
        let result = "Pass";
        println!("Result: {}", result);
    }
    // println!("Result: {}", result); // Error: not found in this scope

    // variables in the same scope
    /*
    In Rust, you can declare a new variable with the same name in the same scope using "let". 
    This is called "shadowing"
    Code below will show some warning to compile the code
    */

    let x = 5;
    let x = 10;

    println!("X is {}", x); // prints 10

    // reuse variable name inside new block
    let z = 5;
    
    {
        let z = 11;
        println!("Z inside a block is: {}", z); // prints 11
    }
    
    println!("Z outside a block is: {}", z); // prints 5
}


