// Match
/*
When you have many choices, using "match" is easier than writing lots of "if..else".
"match" is used to select one of many code blocks to be executed.
*/

/*
Example Explained:
https://www.w3schools.com/rust/rust_match.php
*/
fn main() {
    let day = 4;

    match day {
        1 => println!("Monday"),
        2 => println!("Tuesday"),
        3 => println!("Wednesday"),
        4 => println!("Thursday"),
        5 => println!("Friday"),
        6 => println!("Saturday"),
        7 => println!("Sunday"),
        _ => println!("Invalid day."),
    }
}