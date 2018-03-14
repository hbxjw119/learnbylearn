package main

import (
	"database/sql"
	"fmt"
	"strconv"
	_ "github.com/go-sql-driver/mysql"
)

func main() {
	db, err := sql.Open("mysql", "root:xujiwei-@/go_test?charset=utf8")
	checkErr(err)

	/*
	stmt, err := db.Prepare("insert userinfo set username=?,departname=?,created=?")
	checkErr(err)

	res, err := stmt.Exec("jimmyxu", "didichuxing", "2017-11-27")
	checkErr(err)

	id, err := res.LastInsertId()
	checkErr(err)

	fmt.Println(id)

	stmt, err = db.Prepare("update userinfo set username=? where uid=?")
	checkErr(err)

	res, err = stmt.Exec("jimmyxuupdate", id)
	checkErr(err)

	affect, err := res.RowsAffected()
	checkErr(err)
	*/

	stmt, err := db.Prepare("insert userinfo(username, departname, created) values(?, ?, ?)")
	checkErr(err)
	for i := 0; i < 10; i++ {
		un := "x" + strconv.Itoa(i)
		dn := "d" + strconv.Itoa(i)
		c := "2017-11-1" + strconv.Itoa(i)
		_, err = stmt.Exec(un, dn, c)
		checkErr(err)
	}

	rows, err := db.Query("select * from userinfo")
	checkErr(err)

	for rows.Next() {
		var uid int
		var username string
		var department string
		var created string
		err = rows.Scan(&uid, &username, &department, &created)
		fmt.Println(username)
		checkErr(err)
	}
	/*
	stmt, err = db.Prepare("delete from userinfo where uid=?")
	checkErr(err)

	res, err = stmt.Exec(id)
	checkErr(err)

	affect, err = res.RowsAffected()
	checkErr(err)

	fmt.Println(affect)
	*/

	db.Close()
}

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}