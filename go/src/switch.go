package main

import "fmt"
import "time"

func main() {
	i := 2
	fmt.Println("write ", i, "as ")
	switch i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	}

	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday: //多个case写一行
		fmt.Println("It's the weekend")
	default:
		fmt.Println("It's a weekday")
	}

	//switch后面没有跟表达式，这种写法类似于if/else
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("It's before noon")
	default:
		fmt.Println("It's after noon")
	}

	whatamI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("I'm a bool")
		case int:
			fmt.Println("I'm a int")
		default:
			fmt.Printf("Don't know type %T\n", t)
		}
	}
	whatamI(true)
	whatamI(1)
	whatamI("hey")

}
