package main

import (
	"fmt"
	"strconv"
)

type Human struct {
	name string
	age int
	phone string
}

//Human 实现了fmt.Stringer
func (h Human) String() string {
	return "<" + h.name + " - " + strconv.Itoa(h.age) + " years " + h.phone + " >"
}

func main() {
	Bob := Human{"bob", 39, "111-222"}
	fmt.Println("this Human is ", Bob)
}