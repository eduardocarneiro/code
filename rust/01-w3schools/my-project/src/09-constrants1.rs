/*
Constant variables are used to store values that never change.
Constants must be defined with a type (e.g. i32 or char)
*/

fn main(){
    const BIRTHYEAR: i32 = 1985;
    const MINUTES_PER_HOUR: i32 = 60;

    println!("My Birthyear is: {}", BIRTHYEAR);
    println!("Minutes per hour are: {}", MINUTES_PER_HOUR);

    // CORRECT 
    // const BRITHYEAR: i32 = 1985;
    //
    // WRONG
    // const BIRTHYEAR = 1985;

    // Naming Rules
    /*
    It is a good practice to declare CONSTANT with uppercase

    It is not required, but useful for code readability

    */

    // Constants vs Variables
    /*
    ---------------------------------------------------------------------
    | Feature         | Constant (const)        | Variable (let)        |
    | Can change?     | No                      | Yes, If 'mut' is used |
    | Type required?  | Yes                     | No (optional)         |
    ---------------------------------------------------------------------
    */
}
