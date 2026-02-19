fn main() {
    // need to add the word "mut" to allow rust to change the value of the variable.
    let mut x = 5;
    println!("The value of x is: {}", x);

    x = 10;
    println!("The new value of x is: {}", x);
}
