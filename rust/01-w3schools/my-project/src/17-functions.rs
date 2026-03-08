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
// end

// Function with Parameters
/*
You can send information into a function using parameters
*/

fn greet(name: &str) {
    println!("Hello, {}!", name );
}
// end

// Function with return values
/*
 - A function can return a value
 - Use the "->" symbol in the function header to show what type of value will be returned 
 - Inside the function, use the "return" keyword to send the value back
*/
fn do_sum(a: i32, b: i32) -> i32 {
    return a + b;
}
// end

// Omit return keyword
/*
 - In Rust, you can omit the "return" keyword. Just write the value on the last line of the function, without a semicolon
*/
fn do_sum2(c: i32, d: i32) -> i32 {
    c + d
}


fn main () {
    say_hello(); 
    greet("Dona Saroca!!!");
    
    // sample "Function with return values"
    let sum = do_sum(1, 3);
    println!("Sum is: {}", sum);
    // end
    // sample "Omit return keyword"
    let sum2 = do_sum2(3, 7);
    println!("Sum2 is: {}", sum2);
}

