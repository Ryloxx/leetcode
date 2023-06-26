use std::{
    any::Any,
    fmt::Debug,
    panic::{catch_unwind, RefUnwindSafe, UnwindSafe},
    rc::Rc,
    sync::Arc,
    thread::{self, JoinHandle},
    time::{Duration, Instant},
};

use rayon::prelude::{IndexedParallelIterator, IntoParallelIterator, ParallelIterator};

pub struct TestResult<T: PartialEq + Debug> {
    expected: T,
    result: Option<T>,
    id: usize,
    time: Duration,
    error: Option<String>,
    cmp_f: Rc<dyn Fn(&T, &T) -> bool>,
}

const IS_DEBUG: bool = false;
// const LEETCODE_MAX_RECURSION_DEPTH: u32 = 20_000;
// const LEETCODE_MAX_MEMORY: u32 = 800 * 1024 * 1024; // 800 MB
// const LEETCODE_MAX_TIMEOUT_MS: i32 = if IS_DEBUG { 1000 * 60 * 60 } else {
// 3000 }; // 3000 ms const BATCH_SIZE: u32 = 5;
const MAX_PRINT_WIDTH_RESULT: u32 = if IS_DEBUG { u32::MAX } else { 200 };

impl<T: PartialEq + Debug> Debug for TestResult<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let mut ret = if let Some(ret) = self.result.as_ref() {
            format!("{:?}", ret)
        } else {
            "".to_string()
        };
        let mut expect = format!("{:?}", self.expected);
        ret.truncate(MAX_PRINT_WIDTH_RESULT as usize);
        expect.truncate(MAX_PRINT_WIDTH_RESULT as usize);
        write!(f, "Test nº \u{001B}[34m{}\u{001B}[0m - {} - {{'Time': '{}ms', 'Execution Error': {}, 'Result': '{:?}', 'Expected': '{:?}'}}", self.id,
        if let Some(res) = self.result.as_ref() {
            if self.cmp_f.as_ref()(&self.expected, res) {
                "\u{001B}[32mPass\u{001B}[0m"
            }else{
                "\u{001B}[31mFail\u{001B}[0m"
            }
         } else {
            "\u{001B}[31mFail\u{001B}[0m"
         },
         (self.time.as_nanos() as f64) / 1000000.,
         if let Some(error) = self.error.as_ref() {error.as_str()} else {"N/A"},
         ret,
         expect)?;
        Ok(())
    }
}

pub fn test_algo<F, T, V, C>(f: F, input: Vec<(T, V)>, cmp: C)
where
    V: PartialEq + Debug + Send + 'static,
    F: Fn(T) -> V + Sync + Send + RefUnwindSafe + 'static,
    T: Sync + Send + UnwindSafe + 'static,
    C: Fn(&V, &V) -> bool + 'static,
{
    let f = Arc::new(f);
    let cmp = Rc::new(cmp);

    input
        .into_par_iter()
        .enumerate()
        .map(|(id, (f_in, expected))| {
            let start = Instant::now();
            let result = catch_unwind(|| f(f_in));
            let time = start.elapsed();
            (id, (result, time), expected)
        })
        .collect::<Vec<(usize, (Result<V, Box<dyn Any + Send>>, Duration), V)>>()
        .into_iter()
        .map(|(id, result, expected)| match result {
            (Ok(ret), time) => TestResult {
                error: None,
                expected,
                id,
                result: Some(ret),
                time,
                cmp_f: cmp.clone(),
            },
            (Err(error), time) => TestResult {
                error: Some(if let Some(error) = error.downcast_ref::<String>() {
                    format!("{:#?}", error)
                } else if let Some(error) = error.downcast_ref::<&str>() {
                    format!("{:#?}", error)
                } else {
                    format!("{:#?}", error)
                }),
                expected,
                id,
                result: None,
                time,
                cmp_f: cmp.clone(),
            },
        })
        .for_each(|res| {
            println!("{:?}", res);
        });
}
