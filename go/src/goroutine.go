package main

import (
	"fmt"
	"runtime"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		runtime.Gosched()
		fmt.Println(s)
	}
}

func sum(a []int, c chan int) {
	total := 0
	for _, v := range a {
		total += v
	}
	c <- total
}

func fibonacci(n int, c chan int) {
	x, y := 1, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x + y
	}
	close(c)
}

func main() {
	//example 1
	//go say("world")  //开一个新的goroutines执行
	//say("hello")


	//example 2
	//a := []int{3,6,2,4,5}
	//c := make(chan int)
	//go sum(a[:len(a)/2], c)
	//go sum(a[len(a)/2:], c)

	//x, y := <-c, <-c 
	//fmt.Println(x, y, x + y)

	//example 3
	c := make(chan int, 10)
	go fibonacci(cap(c), c)
	for i := range c {
		fmt.Println(i)
	}
}