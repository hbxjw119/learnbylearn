package main

import "fmt"
import "strings"

func main() {
	var str string = "this is an example of a string"
	var isHavePrefix = strings.HasPrefix(str,"this")
	if isHavePrefix {
		fmt.Printf("the string \"%s\" have prefix this\n", str)
	} else {
		fmt.Printf("the string \"%s\" do not have prefix this\n", str)
	}
}
