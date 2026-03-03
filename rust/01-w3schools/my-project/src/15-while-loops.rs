// While Loop
/*
The "while" loop runs as long as a condition is "true"

The "while" loop checls the condition before each loop, so if the condition is "false" at the start, the loop will not run at all
*/

fn main() {
    let mut count = 1;

    while count <= 5 {
        println!("Count: {}", count);
        count += 1;
    }
    // Stop a While Loop
    /*
    You can stop a "while" loop when you want by using "break"
    */
    let mut num = 1;

    while num <= 10 {
        if num == 7 {
            break;
        }
        println!("Number is: {}", num);
        num += 1;
    }
}