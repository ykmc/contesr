#![allow(non_snake_case, unused_imports, deprecated, dead_code)]

// Input macros
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} }; ($next:expr, mut $var:ident : $t:tt $($r:tt)*) => { let mut $var = read_value!($next, $t); input_inner!{$next $($r)*} }; }
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, [ $t:tt ]) => { { let len = read_value!($next, usize); (0..len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() } }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{VecDeque,HashMap,HashSet,BTreeMap,BTreeSet,BinaryHeap};
// Module for v1.15.1
use std::ascii::AsciiExt; // deprecated since 1.26.0: use inherent method instead

// Functions

// Main
fn main() {

    input! {
        N: usize,
        NP: [(String, i64); N],
    }

    let mut map1:HashMap<String, i64> = HashMap::new();
    let mut map2:HashMap<String, i64> = HashMap::new();

    for (name,point) in &NP {
        let d = map1.entry(name.to_string()).or_insert(0);
        *d += point;
    }

    let mut fpoint = -100000000;
    for (_name,point) in &map1 {
        fpoint = max(fpoint,*point);
    }

    let mut candidates = HashSet::new();
    for (name,point) in map1 {
        if point == fpoint {
            candidates.insert(name);
        }
    }

    for (name,point) in &NP {
        let d = map2.entry(name.to_string()).or_insert(0);
        *d += point;
        if *d >= fpoint && candidates.contains(name) {
            println!("{}", name);
            break;
        }
    }

}