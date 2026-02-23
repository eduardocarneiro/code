fn main() {
    // It is possible to explicity tell Rust what type a value should be.
    let my_num: i32 = 5;         // integer
    let my_double: f64 = 5.99;   // float
    let my_letter: char = 'S';    // character
    let my_bool: bool = true;     // boolean
    let my_text: &str = "Hello";  // string

    println!("my_num: {}", my_num);
    println!("my_double: {}", my_double);
    println!("my_letter: {}", my_letter);
    println!("my_bool: {}", my_bool);
    println!("my_text: {}", my_text);

    /* 
    Basic data types in Rust are divided into different groups:

    * Numbers - Whole numbers and decimal numbers (i32, f64)
    * Characters - Single letters or symbols (char)
    * Strings - Text, a sequence of characters (&str)
    * Booleans - True or false values (bool)

    */
}