// Operators

/*
Rust support many common operators, like:
* Arithmetic Operators
* Assignment Operators
* Comparison Operators
* Logical Operators
*/

// Arithmetic Operators
/*
---------------------------------------
| Operator    Name            Example |
| +           Addition        x + y   |
| -           Subtraction     x - y   |
| *           Multiplication  x * y   |
| /           Division        x / y   |
| %           Modulus         x % y   |
---------------------------------------
*/
// -------------------------------------------------
// Assignment Operators
/*
----------------------------------------
|Operator     Example     Same As
| =           x = 5       x = 5
| +=          x += 3      x = x + 3
| -=          x -= 3      x = x - 3
| *=          x *= 3      x = x * 3
| /=          x /= 3      x = x / 3
| %=          x %= 3      x = x % 3
----------------------------------------
*/

fn main() {
    // Arithmetic Operators
    let add = 5 + 3;
    let sub = 9 - 1;
    let mul = 7 * 5;
    let div = 6 / 2;
    let rem = 10 % 3;

    println!("add: {}", add);
    println!("sub: {}", sub);
    println!("mul: {}", mul);
    println!("div: {}", div);
    println!("rem: {}", rem);
    // 
    // Assignment Operators
    let mut x = 10;
    println!("Start: {}", x);

    x += 5;
    println!("X += 5: {}", x);

    x -= 2;
    println!("X -= 2: {}", x);

    x *= 3;
    println!("X *= 3: {}", x);

    x /= 2;
    println!("X /= 2: {}", x);

    x %= 3;
    println!("X %= 3: {}", x); 
}





