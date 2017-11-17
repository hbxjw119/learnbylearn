package main

import "fmt"

func main() {
	//申明一个字符串变量
	var a string = "initial"
	fmt.Println(a)

	//申明两个整形变量
	var b, c int = 1, 2
	fmt.Println(b, c)

	//申明布尔变量
	var d = true
	fmt.Println(d)

	//申明整形，但没初始化，go自动初始化
	var e int
	fmt.Println(e)

	//var f string = "short"的简写
	f := "short"
	fmt.Println(f)
}
