// Borrowing and References
/*
 - Sometimes you want to use a value without taking owership of it
 - Rust lets you do this using a "reference" - this is called "borrowing"
*/

fn main() {
    // what is reference?
    /*
     - A reference lets you look a value without owning it. You create a reference using the "&" symbol
    */
    let a = String::from("Hello");
    let b = &a;

    println!("A is: {}", a);
    println!("b is: {}", b);

    // mutable references
    /*
     - If you want to change a value through a reference, you need to make the reference "mut"
    */
    let mut name = String::from("Sarah");
    let name_ref = &mut name;
    name_ref.push_str(" G. C.");

    println!("{}", name_ref);
}
