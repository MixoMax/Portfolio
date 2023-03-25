package main

import (
	"fmt"
	"time"
)

func main() {
	var n int
	fmt.Println("Enter a number:")
	fmt.Scan(&n)

	max_n := 0
	max_count := 0
	start_time := time.Now().UnixNano()

	count := 0
	var i int64 = int64(n)
	for i > 1 {
		if i%2 == 0 {
			i = i / 2
		} else {
			i = 3*i + 1
		}
		count++
	}
	max_n = n
	max_count = count

	end_time := time.Now().UnixNano()

	fmt.Printf("Starting number: %d\n", n)
	fmt.Printf("Number of iterations: %d\n", max_count)
	fmt.Printf("Execution time: %d ms\n", (end_time-start_time)/1000000)
}
