// "Scope" refers to where a variable is allowed to be used
/*
 A variable only lives inside the block where it was created. A block is anything inside curly braces
*/

// variable inside a function
fn myFunction() {
    let message = "Hello!";
    println!("{}", message); // message variable can be accessed from here
}

fn main() {
    myFunction();
    // println!("{}", message); // rustc says: Not found in this scope
}


