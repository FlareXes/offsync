package controllers

import (
	"encoding/json"
	"fmt"

	// "github.com/beego/beego/v2/client/orm"
	"github.com/beego/beego/v2/client/orm"
	beego "github.com/beego/beego/v2/server/web"
	models "github.com/flarexes/offsync/go-web/models"
	// models "github.com/flarexes/offsync/go-web/models"
)

type ProfilesController struct {
	beego.Controller
}

func (c *ProfilesController) Get() {
	c.TplName = "profiles.html"
}

type Profile struct {
	Site     string `json:"site"`
	Username string `json:"username"`
	Counter  string `json:"counter"`
	Length   int    `json:"length"`
}

func (c *ProfilesController) Post() {
	var profile Profile

	if err := json.Unmarshal(c.Ctx.Input.RequestBody, &profile); err != nil {
		c.Ctx.WriteString("Invalid JSON data")
		fmt.Println(err)
		return
	}

	fmt.Println("Received row data:", profile)
}

func (c *ProfilesController) GetSave() {
	userID := c.GetSession("user_id")
	if userID == nil {
		c.Redirect("/", 302)
		return
	}
	c.TplName = "save.html"
}

func (c *ProfilesController) Save() {
	c.TplName = "save.html"
	userID := c.GetSession("user_id")
	if userID == nil {
		c.Redirect("/", 302)
		return
	}

	var p models.Profile
	if err := c.ParseForm(&p); err != nil {
		c.Ctx.WriteString("Error binding form data: " + err.Error())
		return
	}

	// profile := models.UserProfile{Id: userID.(int64), Site: p.Site, Username: p.Username, Length: p.Length, Counter: p.Counter}
	profile := models.UserProfile{Id: userID.(int64), Site: p.Site, Username: p.Username, Length: p.Length, Counter: p.Counter}
	o := orm.NewOrm()
	_, err := o.Insert(&profile)
	if err != nil {
		c.Ctx.WriteString("Error during saving profile")
		fmt.Println(err)
		return
	}
}
