 // Strings
/*
 - Strings are used to store text
 - There are two main types of strings in Rust
    * $str   -> It is called "string slices", and is used for fixed text like "Hello"
    * String -> It is used when you need a string that can change
*/

fn main() {
    // Create a String
    /* String can be created from two ways:
    - literal using the "to_string()" method
    - Using the "String::from()" function
    */
    let text1 = "Hello world".to_string();
    println!("{}", text1);

    let text2 = String::from("Hello world!");
    println!("{}", text2);

    // Change a String
    /*
    Strings are mutable, so you can change them if they are declared with "mut"
    - Use "push_str()" to add text to a string
    */

    let mut greeting = String::from("Hello");
    greeting.push_str(" World");
    println!("{}", greeting); // Hello World

    // to add one character use "push()"
    let mut word = String::from("Hi");
    word.push('!');
    println!("{}", word); // Hi!

    // Concatenate Strings
    /*
    Use "format!" macro to concatenate strings
    */
    let s1 = String::from("Hello");
    let s2 = String::from("World");
    let s3 = String::from("what a beautiful day!");

    let result = format!("{} {} {}", s1, s2, s3);
    println!("{}", result);
}



