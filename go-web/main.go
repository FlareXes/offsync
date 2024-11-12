package main

import (
	_ "github.com/flarexes/offsync/go-web/routers"
	beego "github.com/beego/beego/v2/server/web"
)

func main() {
	beego.Run()
}
