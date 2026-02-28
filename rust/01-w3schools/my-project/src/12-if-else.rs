// if..else
/*
Use "if" to specify a block of code to be executed, if a specified condition is true
Use "else" to specify a block of code to be executed, if the same condition is false
Use "else if" to specify a new condition to test, if the first condition is false
Use "match" to select one of many code blocks to be executed
*/

fn main() {
    // Use "if" to specify a block of code to be executed if a condition is "true"
    if 7 > 5 {
        println!("7 is greater than 5");
    }

    // You can also test variables
    let x = 10;
    let y = 7;

    if x > y {
        println!("10 is greater than 7");
    }

}