#![allow(non_snake_case, unused_imports, deprecated)]

// Input macros
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} }; ($next:expr, mut $var:ident : $t:tt $($r:tt)*) => { let mut $var = read_value!($next, $t); input_inner!{$next $($r)*} }; }
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, [ $t:tt ]) => { { let len = read_value!($next, usize); (0..len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() } }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,HashMap,VecDeque,BinaryHeap};
// Module for v1.15.1
use std::ascii::AsciiExt; // deprecated since 1.26.0: use inherent method instead

// Functions

// Main
fn main(){

    input!{
        N: usize,
        K: usize
    }

    let mut ans = 0.0;

    let mut m = 0;
    let mut a = vec![(K,m); 1];
    let mut Kf = K as f64;
    while Kf > 1.0{
        Kf = (Kf/2.0).ceil();
        m += 1;
        a.push( (Kf.ceil() as usize, m) );
    }

    a.reverse();
    for i in 0..a.len(){
        let w;
        if i == a.len()-1{
            w = N - a[i].0 + 1;
            ans += w as f64 / (2_i32.pow(a[i].1)) as f64;   
            break;
        }else if a[i+1].0 > N{
            w = N - a[i].0 + 1;
            ans += w as f64 / (2_i32.pow(a[i].1)) as f64;   
            break;
        } else{
            w = a[i+1].0 - a[i].0;
            ans += w as f64 / (2_i32.pow(a[i].1)) as f64;  
        }
    }

    println!("{}", ans / N as f64);
}