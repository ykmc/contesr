#![allow(non_snake_case, unused_imports)]

// Input macros
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} }; ($next:expr, mut $var:ident : $t:tt $($r:tt)*) => { let mut $var = read_value!($next, $t); input_inner!{$next $($r)*} }; }
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, [ $t:tt ]) => { { let len = read_value!($next, usize); (0..len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() } }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,HashMap,VecDeque,BinaryHeap};

// Functions
fn remove_zero(n: u64) -> u64{
    let mut ret = 0;
    let mut nz:Vec<u64> = Vec::new();
    for d in n.to_string().chars(){
        if d!='0'{
            nz.push(d as u64 -48);
        }
    }
    for d in nz{
        ret = ret*10 + d;
    }
    return ret;
}

// Main
fn main(){

    input!{
        A: u64,
        B: u64
    }

    let na = remove_zero(A);
    let nb = remove_zero(B);
    let nc = remove_zero(A+B);
    println!("{}", if na+nb==nc{"YES"}else{"NO"});

}
