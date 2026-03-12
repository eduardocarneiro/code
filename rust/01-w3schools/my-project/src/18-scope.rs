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
}


