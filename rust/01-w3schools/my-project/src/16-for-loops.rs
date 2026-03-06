// "for" loop
/*
Use "for" when you know exaclty how many times you want to loop
Use "for" loop together with the "in" keyword, instead of a "while" loop
*/

fn main() {
    // This prints numbers from 1 to 5.
    for i in 1..6 {
        println!("i is: {}", i);
    }

    // to include the last number, use "..="
    for j in 1..=6 {
        println!("j is: {}", j);
    }

    // Break and Continue
    for k in 1..=10 {

        if k == 3 {
            continue;
        }

        if k == 5 {
            break;
        }
        println!("k is: {}",  k);
    }
}
