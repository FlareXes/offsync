package controllers

import (
	beego "github.com/beego/beego/v2/server/web"
	models "github.com/flarexes/offsync/go-web/models"
)

type OffsyncController struct {
	beego.Controller
}

func (c *OffsyncController) Get() {
	c.TplName = "index.tpl"
}

func (c *OffsyncController) Post() {
	var profile models.Profile
	c.TplName = "index.tpl"

	if err := c.ParseForm(&profile); err != nil {
		c.Ctx.WriteString("Error binding form data: " + err.Error())
		return
	}

	password := models.GeneratePassword(profile)

	c.Data["Answer"] = password

	// c.SetSession("password", password)

	c.SetSession("username", "john_doe")
    c.SetSession("logged_in", true)
    c.Ctx.WriteString("Session set!")

	// TODO
	// if site == "" || username == "" || length == "" || counter == "" {
	// 	fmt.Println("Missing form fields!")
	// }
	// c.Ctx.Redirect(302, "/")
	// c.Redirect("/", 302)
}
