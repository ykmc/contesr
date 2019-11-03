#![allow(non_snake_case, unused_imports)]

// Input macros
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} }; ($next:expr, mut $var:ident : $t:tt $($r:tt)*) => { let mut $var = read_value!($next, $t); input_inner!{$next $($r)*} }; }
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, [ $t:tt ]) => { { let len = read_value!($next, usize); (0..len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() } }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,HashMap,VecDeque,BinaryHeap};

// Functions

// Main
fn main(){
    input!{
        N: usize,
        XY: [(i64,i64); N],
    }
    let mut ans = 0;
    for i in 0..N{
        let (mut f1, mut f2, mut f3, mut f4) = (false, false, false, false);
        for j in 0..N{
            if i==j{
                continue;
            }
            if XY[i].0 == XY[j].0 && XY[i].1 > XY[j].1{
                f1 = true;
            }
            if XY[i].0 == XY[j].0 && XY[i].1 < XY[j].1{
                f2 = true;
            }
            if XY[i].1 == XY[j].1 && XY[i].0 > XY[j].0{
                f3 = true;
            }
            if XY[i].1 == XY[j].1 && XY[i].0 < XY[j].0{
                f4 = true;
            }
        }
        if f1 && f2 && f3 && f4{
            ans += 1;
        }
    }
    println!("{}", ans);
}
