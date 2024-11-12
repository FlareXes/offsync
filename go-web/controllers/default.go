package controllers

import (
	"fmt"

	beego "github.com/beego/beego/v2/server/web"
)

type MainController struct {
	beego.Controller
}

func (c *MainController) Get() {
	c.Data["Website"] = "beego.vip"
	c.Data["Email"] = "astaxie@gmail.com"
	c.TplName = "index.tpl"
}

type OffsyncController struct {
	beego.Controller
}

func (c *OffsyncController) Get() {
	c.Data["Site"] = "GitHub"
	c.Data["Username"] = "FlareXes"
	c.TplName = "index.tpl"
}

type Profile struct {
	Site     string `form:"site"`
	Username string `form:"username"`
	Length   string `form:"length"`
	Counter  string `form:"counter"`
}

func (c *OffsyncController) Post() {
	site := c.GetString("site")
	username := c.GetString("username")
	length := c.GetString("length")
	counter := c.GetString("counter")
	// c.TplName = "submit.html"
	c.Ctx.Redirect(302, "/")

	if site == "" || username == "" || length == "" || counter == "" {
		fmt.Println("Missing form fields!")
	} else {
		fmt.Println(site, username, length, counter)
	}
	fmt.Println(site, username, length, counter)
}
