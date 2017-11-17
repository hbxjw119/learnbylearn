package main

import "fmt"

func main() {
	//用make初始化一个map，make(map[key-type]val-type)
	m := make(map[string]int)
	//或者
	n := map[string]int{"k1": 3, "bar": 4}
	fmt.Println(n)

	m["k1"] = 3
	m["k2"] = 7

	fmt.Println("map is:", m)

	v1 := m["k1"]
	fmt.Println("v1 is: ", v1)

	fmt.Println("len: ", len(m))

	delete(m, "k2")
	fmt.Println("map is:", m)

	_, prs := m["k2"]
	fmt.Println("prs: ", prs)

}
