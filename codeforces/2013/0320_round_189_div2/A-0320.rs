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
        N: chars,
    }
    
    let mut ans = "YES";
    let mut cnt_4 = 0; 

    // 最上位は 1 必須
    if N[0] != '1' {
        ans = "NO";
    } else {
        for i in 1..N.len() {
            if N[i] == '1' {
                cnt_4 = 0;
                continue;
            // 4 は連続2回まで
            } else if N[i] == '4' {
                cnt_4 += 1;
                if cnt_4 > 2 {
                    ans = "NO";
                    break;
                }
            } else {
                ans = "NO";
                break;
            }
        }
    }
    println!("{}", ans);
}