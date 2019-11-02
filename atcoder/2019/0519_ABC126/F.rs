#![allow(non_snake_case, unused_imports, deprecated, dead_code)]

// Input macros
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} }; ($next:expr, mut $var:ident : $t:tt $($r:tt)*) => { let mut $var = read_value!($next, $t); input_inner!{$next $($r)*} }; }
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, [ $t:tt ]) => { { let len = read_value!($next, usize); (0..len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() } }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{VecDeque,HashSet,HashMap,BinaryHeap};
// Module for v1.15.1
use std::ascii::AsciiExt; // deprecated since 1.26.0: use inherent method instead

// Functions

// Main
fn main() {

    input! {
        M: usize,
        K: usize,
    }

    if M == 0 {
        if K == 0 {
            println!("0 0");
            return;
        }
    } else if M == 1 {
        if K == 0 {
            println!("0 0 1 1");
            return;
        } else if K == 1 {
            println!("-1");
            return;
        }
    }

    let mm = 2_usize.pow(M as u32);
    if K >= mm {
        println!("-1");
        return;
    }

    let mut a1 = VecDeque::new();
    let mut a2 = VecDeque::new();
    for i in 0..mm{
        if i == K {
            continue;
        }
        a1.push_back(i);
        a2.push_front(i);
    }

    for a in a1 {
        print!("{} ", a);
    }
    print!("{} ", K);
    for a in a2 {
        print!("{} ", a);
    }
    print!("{} ", K);

}