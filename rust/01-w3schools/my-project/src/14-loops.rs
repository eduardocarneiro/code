// Loops
/*
Rust has three types of loops: "loop", "while", and "for"
*/

fn main() {
    // loop
    /*
    "loop" is the simplest of Rust's three loop types
    It will run forever unless you tell it to stop
    */
    /*
    loop {
        println!("This will repeat forever!");
    }
    */

    // loop break
    let mut count = 1;
    // to stop "loop", use the "break" keyword
    loop {
        println!("Hello world!");

        if count == 3 {
            break;
        }
        count += 1;
    }
}

