package main

import "fmt"

func main() {
	nums := []int{2,5,1}
	sum := 0

	//类似于python中的for i,v in range(4)
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum is :", sum)

	for i, num := range nums {
		fmt.Println(i, num)
	}

	kvs := map[string]int{"a": 1, "b": 2}
	for k,v := range kvs {
		fmt.Printf("%s -> %d\n", k, v)
	}
}
