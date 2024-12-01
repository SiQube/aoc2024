use itertools::Itertools;

static TEST_STR: &str = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/../", "/test.txt"));
static INPUT_STR: &str = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/..", "/input.txt"));

fn compute(filename: &str) -> u32 {
    let (left_list, right_list): (Vec<u32>, Vec<u32>) = filename
        .lines()
        .map(|line| {
            line.split_ascii_whitespace()
                .map(|e| e.parse::<u32>().unwrap())
                .collect_tuple()
                .unwrap()
        })
        .unzip();
    return left_list
        .iter()
        .sorted_unstable()
        .zip(right_list.iter().sorted_unstable())
        .map(|(num_l1, num_l2)| num_l1.abs_diff(*num_l2))
        .sum();
}


pub fn main() {
    let test_expected: u32 = 11;
    let test_result = compute(TEST_STR);
    if test_result == test_expected {
        println!("{}", compute(INPUT_STR));
    } else {
        println!("expected {} got {}", test_expected, test_result);
    };
}
