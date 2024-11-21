package models

import (
	"github.com/beego/beego/v2/client/orm"
)

type User struct {
	Id       int64  `orm:"auto"`
	Username string `orm:"unique"`
	Password string
}

type UserProfile struct {
	Id       int64 `orm:"auto"`
	UserId   int64
	Site     string
	Username string
	Counter  string
	Length   int
}

func init() {
	orm.RegisterModel(new(User))
	orm.RegisterModel(new(UserProfile))
}
