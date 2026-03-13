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
}


