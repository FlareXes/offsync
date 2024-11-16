package controllers

import (
	"github.com/beego/beego/v2/client/orm"
	"golang.org/x/crypto/bcrypt"

	beego "github.com/beego/beego/v2/server/web"
	models "github.com/flarexes/offsync/go-web/models"
)

type AuthController struct {
	beego.Controller
}

func (c *AuthController) GetSignUp() {
	c.TplName = "signup.html"
}

func (c *AuthController) GetSignIn() {
	userID := c.GetSession("user_id")
	if userID != nil {
		c.Redirect("/", 302)
		return
	}
	
	c.TplName = "signin.html"
}

func (c *AuthController) SignUp() {
	username := c.GetString("username")
	password := c.GetString("password")
	hashedPassword, _ := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)

	user := models.User{Username: username, Password: string(hashedPassword)}
	o := orm.NewOrm()
	_, err := o.Insert(&user)
	if err != nil {
		c.Ctx.WriteString("Error during sign up")
		return
	}
	c.Redirect("/signup", 302)
}

func (c *AuthController) SignIn() {
	userID := c.GetSession("user_id")
	if userID != nil {
		c.Redirect("/", 302)
		return
	}

	username := c.GetString("username")
	password := c.GetString("password")

	o := orm.NewOrm()
	user := models.User{Username: username}
	err := o.Read(&user, "Username")

	// If User Not Found Return
	if err == orm.ErrNoRows {
		c.Ctx.WriteString("Invalid credentials")
		return
	}

	err = bcrypt.CompareHashAndPassword([]byte(user.Password), []byte(password))
	if err != nil {
		c.Ctx.WriteString("Invalid credentials")
		return
	}
	c.SetSession("user_id", user.Id)
	c.SetSession("username", user.Username)

	c.Redirect("/", 302)
}

func (c *AuthController) LogOut() {
	c.DelSession("user_id")
	c.DelSession("username")
	c.Redirect("/", 302)
}
