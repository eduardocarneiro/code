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
//
// Comparison Operators
/*
-------------------------------------------------
| Operator    Meaning                     Example |
| ==          Equal to                    x == y  |
| !=          Not equal                   x != y  |
| >           Greater than                x > y   |
| <           Less than                   x < y   |
| >=          Greater than or equal to    x >= y  |
| <=          Less than or equal to       x <= y  |
-------------------------------------------------
*/
// Logical Operators
/*
-------------------------------------------------------------------------------
| Operator    Name    Description                                               |
| &&          AND     Returns true if both statements are true                  |
| ||          OR      Returns true if one of the statements is true             |
| !           NOT     Reverse the result, returns false if the result is true   |
-------------------------------------------------------------------------------
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
    //
    // Comparison Operators
    let a = 5;
    let b = 9;

    println!("5 == 9: {}", a == b);
    println!("5 != 9: {}", a != b);
    println!("5 > 9: {}", a > b);
    println!("5 < 9: {}", a < b);
    println!("5 >= 9: {}", a >= b);
    println!("5 <= 9: {}", a <= b);
    //
    // Logical Operators
    let logged_in = true;
    let is_admin = false;

    println!("Is regular user: {}", logged_in && !is_admin);
    println!("Has any access: {}", logged_in || is_admin);
    println!("Not logged in: {}", !logged_in);

}






