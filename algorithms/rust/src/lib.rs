use std::{
    any::Any,
    fmt::Debug,
    panic::{catch_unwind, RefUnwindSafe, UnwindSafe},
    rc::Rc,
    sync::Arc,
    thread::{self, JoinHandle},
    time::{Duration, Instant},
};

pub struct TestResult<T: Ord + Debug> {
    expected: T,
    result: Option<T>,
    id: usize,
    time: Duration,
    error: Option<String>,
    cmp_f: Rc<dyn Fn(&T, &T) -> bool>,
}

impl<T: Ord + Debug> Debug for TestResult<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
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
         if let Some(ret) = self.result.as_ref() { format!("{:?}", ret) } else {"".to_string()},
         self.expected)?;

        Ok(())
    }
}

pub fn test_algo<F, T, V, C>(f: F, input: Vec<(T, V)>, cmp: C)
where
    V: Ord + Debug + Send + 'static,
    F: Fn(T) -> V + Sync + Send + RefUnwindSafe + 'static,
    T: Sync + Send + UnwindSafe + 'static,
    C: Fn(&V, &V) -> bool + 'static,
{
    let f = Arc::new(f);
    let cmp = Rc::new(cmp);
    input
        .into_iter()
        .enumerate()
        .map(|(id, (f_in, expected))| {
            let f = f.clone();
            (
                id,
                thread::spawn(move || {
                    let start = Instant::now();
                    let result = catch_unwind(|| f(f_in));
                    let time = start.elapsed();
                    (result, time)
                }),
                expected,
            )
        })
        .collect::<Vec<(
            usize,
            JoinHandle<(Result<V, Box<dyn Any + Send>>, Duration)>,
            V,
        )>>()
        .into_iter()
        .map(|(id, handle, expected)| {
            let result = handle.join();
            if let Ok(result) = result {
                match result {
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
                }
            } else {
                TestResult {
                    error: Some("Unexpected Error".to_string()),
                    expected,
                    id,
                    result: None,
                    time: Duration::new(0, 0),
                    cmp_f: cmp.clone(),
                }
            }
        })
        .for_each(|res| {
            println!("{:?}", res);
        });
}
