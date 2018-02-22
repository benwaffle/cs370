use std::time::SystemTime;
use std::collections::HashSet;

fn len(x: u32) -> u8 {
    let mut y = x;
    let mut res = 0;
    while y > 0 {
        res += 1;
        y /= 10;
    }
    res
}

fn is_pan(i: u32, j: u32) -> bool {
    let target = 0b1111111110;
    let m = i*j;
    let mut cnt = 0;
    let ns = vec![i, j, m];
    for mut x in ns {
        while x > 0 {
            cnt |= 1 << (x % 10);
            x /= 10;
        }
    }
    if cnt == target && len(i) + len(j) + len(m) == 9 {
        true
    } else {
        false
    }
}

fn main() {
    let start = SystemTime::now();
    let mut set = HashSet::new();
    for i in 2..10 {
        for j in 1000..10000 {
            if is_pan(i, j) {
                println!("{} * {} = {}", i, j, i*j);
                set.insert(i*j);
            }
        }
    }
    for i in 10..100 {
        for j in 100..1000 {
            if is_pan(i, j) {
                println!("{} * {} = {}", i, j, i*j);
                set.insert(i*j);
            }
        }
    }
    println!("{:?}", set.into_iter().sum::<u32>());
    println!("{} ms", start.elapsed().unwrap().subsec_nanos() as f64 / 1000.0 / 1000.0);
}
