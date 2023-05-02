use std::{
    fmt::Display,
    sync::Arc,
    thread::{self, JoinHandle},
    time::{Duration, Instant},
};

pub struct TestResult<T: Ord> {
    expected: T,
    result: Option<T>,
    id: usize,
    time: Duration,
    error: Option<String>,
}

impl<T: Ord + Display> Display for TestResult<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Test nº {} - {} - {{'Time': '{}ms', 'Execution Error': {:?}, 'Result': '{}', 'Expected': '{}'}}", self.id,
        if let Some(res) = self.result.as_ref() {
            if self.expected == *res{
                "Pass"
            }else{
                "Fail"
            }
         } else {
            "Fail"
         },
         (self.time.as_nanos() as f64) / 1000000.,
         self.error,
         if let Some(ret) = self.result.as_ref() { ret.to_string()} else {"".to_string()},
         self.expected)?;

        Ok(())
    }
}

pub fn test_algo<F, T, V>(f: F, input: Vec<(T, V)>)
where
    F: Fn(T) -> Result<V, String> + Sync + Send + 'static,
    V: Ord + std::fmt::Display + Send + 'static,
    T: Send + 'static,
{
    let f = Arc::new(f);
    input
        .into_iter()
        .enumerate()
        .map(|(id, (f_in, expected))| {
            let f = f.clone();
            (
                id,
                thread::spawn(move || {
                    let start = Instant::now();
                    let result = f(f_in);
                    let time = start.elapsed();
                    (result, time)
                }),
                expected,
            )
        })
        .collect::<Vec<(usize, JoinHandle<(Result<V, String>, Duration)>, V)>>()
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
                    },
                    (Err(error), time) => TestResult {
                        error: Some(error),
                        expected,
                        id,
                        result: None,
                        time,
                    },
                }
            } else {
                TestResult {
                    error: Some("Unexpected Error".to_string()),
                    expected,
                    id,
                    result: None,
                    time: Duration::new(0, 0),
                }
            }
        })
        .for_each(|res| {
            println!("{}", res);
        });
}
