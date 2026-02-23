// Basic data type in Rust are divided into different groups:

/*
Numbers - Whole numbers and decimal numbers (i32, f64)
Characters - Single letters or symbols (char)
Strings - Text, a sequence of characters (&str)
Booleans - True or false values (bool)
*/

// Samples
fn main() {
    
    // Integer (i32)
    let age: i32 = 40;
    println!("Age is: {}", age);

    // Floating Point (f64)
    let price: f64 = 1.99;
    println!("Price is: {}", price);

    // Characters (char)
    let my_grade: char = 'A';
    println!("My Grade is: {}", my_grade);

    // String (&str)
    let name: &str = "Eduardo";
    println!("My name is: {}", name);

    // Booleans (bool)
    let is_rust_nice: bool = true;
    println!("Is Rust nice? {}", is_rust_nice);

}