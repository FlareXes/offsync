package controllers

import (
	"encoding/json"
	"fmt"

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

func (c *OffsyncController) API() {
	userID := c.GetSession("user_id")
	if userID == nil {
		c.Redirect("/signin", 302)
		return
	}

	var data map[string]interface{}

	// Parse the JSON data from the body of the request
	if err := json.Unmarshal(c.Ctx.Input.RequestBody, &data); err != nil {
		c.Data["json"] = map[string]string{"error": "Invalid data"}
		c.ServeJSON()
		fmt.Println(err)
		return
	}

	site := data["Site"]
	username := data["Username"]
	length := data["Length"]
	counter := data["Counter"]

	fmt.Println(site, username, length, counter)

	c.Redirect("/", 302)
	// var profile models.Profile
	// if err := c.ParseForm(&profile); err != nil {
	// 	c.Ctx.WriteString("Error binding form data: " + err.Error())
	// 	return
	// }
	// password := models.GeneratePassword(profile)

	// c.Ctx.SetCookie("password", password)
	// c.Redirect("/", 302)
}
