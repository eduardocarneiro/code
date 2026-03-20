// Rust Loops Summary
/*
Rust has three types of loops

* Extra keywords
You can use these in any loop:
 - break - stop the loop
 - continue - skip value in the loop

######
"loop"
###### 
* The simplest kind of loop, It runs forever unless you stop it with "break"
* Use "loop" when you do not know in advance how many times to repeat --- IMPORTANT

loop {
    // do something
    if condition {
        break;
    }   
}

-----
#######
"while"
#######
* repeats code while a condition is true. It checks the condition before each loop.
* Use "while" when you want to repeat code until something happens --- IMPORTANT

while count <= 5 {
    println!("{}", count);
    count += 1;
}

-----
#######
"for"
#######
* repeats code a fixed number of times
* use "for" when you know exaclty what to loop through

for i in..5 {
    println!("{}", i);
}
*/