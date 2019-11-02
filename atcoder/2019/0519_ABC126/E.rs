#![allow(non_snake_case, unused_imports, deprecated, dead_code)]

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
struct UnionFind {
    par  : Vec<usize>,
    rank : Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> UnionFind {
        let mut vec = vec![0; n];
        for i in 0..n{
            vec[i] = i;
        }
        UnionFind{
            par  : vec,
            rank : vec![0; n]
        }
    }

    fn find(&mut self, x:usize) -> usize {
        if x == self.par[x] {
            return x;
        }else{
            let par = self.par[x];
            let res = self.find(par);
            self.par[x] = res;
            return res;
        }
    }

    fn same(&mut self, x:usize, y:usize) -> bool {
        return self.find(x) == self.find(y);
    }

    fn unite(&mut self, x:usize, y:usize) {
        let x_par = self.find(x);
        let y_par = self.find(y);
        if self.rank[x_par] > self.rank[y_par] {
            self.par[y_par] = x_par;
        }else{
            self.par[x_par] = y_par;
            if self.rank[x_par] == self.rank[y_par] {
                self.rank[y_par] += 1;
            }
        }
    }

}

// Main
fn main() {

    input! {
        N: usize,
        M: usize,
        XYZ: [(usize,usize,usize); M]
    }

    let mut uf = UnionFind::new(N);
    for &(x,y,_z) in XYZ.iter() {
        uf.unite(x-1,y-1);
    }

    let mut ans = vec![];
    for i in 0..N {
        ans.push(uf.find(i));
    }

    ans.sort();
    ans.dedup();

    println!("{}", ans.len());
}