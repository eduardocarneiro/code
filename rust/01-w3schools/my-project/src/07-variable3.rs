fn main() {
    let x = 5;
    x = 10; // Error
    println!("{}", x)
}

/* 
the error below If I try to run the command rustc variable3.rs
###
eduardo@eoc:~/github-eduardocarneiro/code/rust/01-w3schools/my-project/src$ rustc variable3.rs 
error[E0384]: cannot assign twice to immutable variable `x`
 --> variable3.rs:3:5
  |
2 |     let x = 5;
  |         - first assignment to `x`
3 |     x = 10; // Error
  |     ^^^^^^ cannot assign twice to immutable variable
  |
help: consider making this binding mutable
  |
2 |     let mut x = 5;
  |         +++

warning: value assigned to `x` is never read
 --> variable3.rs:2:13
  |
2 |     let x = 5;
  |             ^
  |
  = help: maybe it is overwritten before being read?
  = note: `#[warn(unused_assignments)]` (part of `#[warn(unused)]`) on by default

error: aborting due to 1 previous error; 1 warning emitted

For more information about this error, try `rustc --explain E0384`.
###
*/