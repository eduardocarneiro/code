// Rust Ownership
/*
 - Rust uses "ownership" to manage memory in a safe way.
 - Every value in Rust has an "owner". The owner is usually a variable.

 Ownership Rules
  - Each value has one owner
  - When the owner goes out of scope, the value is deleted
  - You can only have one owner at a time, unless you "borrow" it
*/

fn main() {
    // Basic Ownership
    /*
    In this example, "a" owns the string. Then we move it to "b".

    - When we assign "a" to "b", the ownership moves. This means only "b" can use the value now, because "a" is no longer valid.
    */
    let a = String::from("Hello");
    let b = a;

    // println!("{}", a); // Error: "a" no longer owns the value
    println!("{}", b);

    // 
    /*    
    - Simple types like numbers, characters and booleans are "copied", not moved.
    - This means you can still use the orginal variable after assigning it to another
    */
    let y = 5;
    let z = y;

    println!("y: {}", y);
    println!("z: {}", z);

}
