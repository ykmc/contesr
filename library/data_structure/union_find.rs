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