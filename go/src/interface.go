package main

import "fmt"

type Human struct {
	name string
	age int
	phone string
}

type Student struct {
	Human  //匿名字段
	school string
	loan float32
}

type Employee struct {
	Human  //匿名字段
	company string
	money float32
}

//human实现SayHi方法
func (h Human) SayHi() {
	fmt.Printf("hi, I am %s you can call me on %s\n", h.name, h.phone)
}

//Human实现Sing方法
func (h Human) Sing(lyrics string) {
	fmt.Println("la la la...", lyrics)
}

//Employee重载Humande SayHi方法
func (e Employee) SayHi() {
	fmt.Printf("hi, I am %s, I work at %s. Call me on %s\n", e.name,
		e.company, e.phone)
}

//Interface Men被Human,Student和Employee实现
//因为这三个类型都实现了这两个方法
type Men interface {
	SayHi()
	Sing(lyrics string)
}

func main() {
	mike := Student{Human{"Mike", 25, "111-222"}, "MIT", 0.00}
	paul := Student{Human{"Paul", 26, "333-333"}, "Harvard", 100}
	sam := Employee{Human{"Sam", 36, "234-233"}, "Golang Inc", 1000}
	tom := Employee{Human{"tom", 37, "444-555"}, "Things Ltd.", 5000}

	var i Men

	i = mike
	fmt.Println("this is Mike, a Student:")
	i.SayHi()
	i.Sing("November rain")

	i = tom
	fmt.Println("this is tom, an Employee:")
	i.SayHi()
	i.Sing("born to be wild")

	fmt.Println("let's use a slice of Men and see what happens")
	x := make([]Men, 3)

	x[0], x[1], x[2] = paul, sam, mike

	for _, value := range x {
		value.SayHi()
	}
}
