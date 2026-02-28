// if..else
/*
Use "if" to specify a block of code to be executed, if a specified condition is true
Use "else" to specify a block of code to be executed, if the same condition is false
Use "else if" to specify a new condition to test, if the first condition is false
Use "match" to select one of many code blocks to be executed
*/

fn main() {
    // Use "if" to specify a block of code to be executed if a condition is "true"
    if 7 > 5 {
        println!("7 is greater than 5");
    }

    // You can also test variables
    let x = 10;
    let y = 7;

    if x > y {
        println!("10 is greater than 7");
    }

    // if..else 
    // If the condition is not true, you can use "else" to run different code:
    let age = 16;

    if age >= 16 {
        println!("You can vote.");
    } else {
        println!("You are too young to vote");   
    }

    // else if
    // You can check multiple conditions using "else if"

    let score = 77;

    if score >= 90 {
        println!("Grade: A");
    } else if score >= 80 {
        println!("Grade: B");
    } else if score >= 70 {
        println!("Grade: C");
    } else {
        println!("Grade: F");
    }

    // If as an Expression
    /*
    In Rust, If..else can also be used as an expression
    This means you can assign the result of an "if" to a variable
    
    When using "if" as an expression, you must include "else". This ensures the result always has a value.
    */
    let time = 20;
    let greeting = if time < 18 {
        "Good day"
    } else {
        "Good evening"
    };
    println!("{}", greeting);

    // Simplified syntax
    let new_time = 17;
    let new_greeting = if new_time < 18 {"Good Day."} else {"Good Evening."};
    println!("{}", new_greeting);
 }