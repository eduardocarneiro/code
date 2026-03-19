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

/*
NOTE: You can only have one mutable reference to a value at a time!

Why Borrowing is important:

Borrowing helps you reuse values safely, without giving them away.
    - It lets you use values wihtout taking ownership
    - It avoids cloning, which can be slow for large data
    - It makes your programs safer and faster
*/
