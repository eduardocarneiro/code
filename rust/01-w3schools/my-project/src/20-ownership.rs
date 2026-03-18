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

    // Clone
    /*
    To keep the original value and also assign it to another varibale, use the ".clone()" method
    */

    let var1 = String::from("data from var1");
    let var2 = var1.clone(); // both variables has the same value

    println!("var1: {}", var1);
    println!("var2: {}", var2);

}

/*
Why ownership matters
    - Rust uses ownership to automatically free memory when it's no longer needed
    - It prevents bugs like using memory that's already been deleted
    - It is one of the reasons Rust is so safe and fast

*/