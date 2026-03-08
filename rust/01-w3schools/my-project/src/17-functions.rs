// Functions
/*
- A function is a block of code that only runs when you call it
- Functions is used to organize your code, avoid repeating yoursef, and make your program easier to understand 
*/

// creating a function
/*
fn function_name() {
    // code here
}
*/

// calling a function
/*
 - to call a function, write the name of the function followed by two parantheses().
*/
// sample
fn say_hello() {
    println!("Hello from a function!");
}

// Function with Parameters
/*
You can send information into a function using parameters
*/

fn greet(name: &str) {
    println!("Hello, {}!", name );
}

fn main () {
    say_hello(); 
    greet("Dona Saroca!!!");
}
