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
fn dfs(n:usize, color:usize, A:&Vec<Vec<(usize,i64)>>, ans:&mut Vec<usize>){
    ans[n] = color;
    for &(next_n, length) in A[n].iter(){
        if ans[next_n] == 9{
            let next_color = if length%2==0{color}else{1-color};
            dfs(next_n, next_color, A, ans);
        }
    }
}
// Main
fn main(){

    input!{
        N: usize,
        UVW: [(usize,usize,i64); N-1]
    }

    let mut A = vec![vec![]; N];
    for (u,v,w) in UVW{
        A[u-1].push((v-1, w));
        A[v-1].push((u-1, w));
    }

    let mut ans = vec![9; N];
    // current node, color(0 or 1), adjacency list, ans vec
    dfs(0, 0, &A, &mut ans);

    for i in 0..N{
        println!("{}", ans[i]);
    }

}