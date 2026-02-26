// Booleans
// Booleans represent values that are either true or false.

//
fn main() {
    // Boolean variable
    let is_programming_fun: bool = true;
    let is_fish_tasty: bool = !false;

    println!("Is programming fun? {}", is_programming_fun);
    println!("Is fish tasty? {}", is_fish_tasty);
    //
    // Boolean from Comparison

    let age = 20;
    let can_vote = age >= 16;

    println!("Can vote? {}", can_vote);
    //
    // Boolean in "If" statements
    let is_logged_in = true;

    if is_logged_in {
        println!("User is logged in");
    } else {
        println!("User is not logged in");
    }
}