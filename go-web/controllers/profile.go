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

func getUsersByUserId(userId int64) ([]models.UserProfile, error) {
	o := orm.NewOrm()
	var profiles []models.UserProfile

	// Query to get all users where UserId = 1
	_, err := o.QueryTable("UserProfile").Filter("UserId", userId).All(&profiles)
	if err != nil {
		fmt.Println("Error retrieving profiles:", err)
		return nil, err
	}
	return profiles, nil
}

type ProfilesController struct {
	beego.Controller
}

func (c *ProfilesController) Get() {
	userId := c.GetSession("user_id")
	if userId == nil {
		c.Redirect("/", 302)
		return
	}

	profiles, err := getUsersByUserId(userId.(int64))
	if err != nil {
		c.Ctx.WriteString("Error retrieving profiles")
		fmt.Println(err)
		return
	}
	fmt.Println(profiles)
	c.Data["Profiles"] = profiles
	c.TplName = "profiles.tpl"
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

// SAVE PROFILES SECTION

func (c *ProfilesController) GetSave() {
	userId := c.GetSession("user_id")
	if userId == nil {
		c.Redirect("/", 302)
		return
	}
	c.TplName = "save.html"
}

func (c *ProfilesController) Save() {
	c.TplName = "save.html"
	userId := c.GetSession("user_id")
	if userId == nil {
		c.Redirect("/", 302)
		return
	}

	var p models.Profile
	if err := c.ParseForm(&p); err != nil {
		c.Ctx.WriteString("Error binding form data: " + err.Error())
		return
	}

	profile := models.UserProfile{UserId: userId.(int64), Site: p.Site, Username: p.Username, Length: p.Length, Counter: p.Counter}
	o := orm.NewOrm()
	_, err := o.Insert(&profile)
	if err != nil {
		c.Ctx.WriteString("Error during saving profile")
		fmt.Println(err)
		return
	}
}
