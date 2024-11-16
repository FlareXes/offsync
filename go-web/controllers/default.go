package controllers

import (
	beego "github.com/beego/beego/v2/server/web"
	models "github.com/flarexes/offsync/go-web/models"
)

type OffsyncController struct {
	beego.Controller
}

func (c *OffsyncController) Get() {
	userID := c.GetSession("user_id")
	if userID == nil {
		c.Redirect("/signin", 302)
		return
	}
	c.TplName = "index.tpl"
}

func (c *OffsyncController) Post() {
	userID := c.GetSession("user_id")
	if userID == nil {
		c.Redirect("/signin", 302)
		return
	}

	var profile models.Profile
	if err := c.ParseForm(&profile); err != nil {
		c.Ctx.WriteString("Error binding form data: " + err.Error())
		return
	}
	password := models.GeneratePassword(profile)

	c.Ctx.SetCookie("password", password)
	c.Redirect("/", 302)
}
