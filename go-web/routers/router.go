package routers

import (
	beego "github.com/beego/beego/v2/server/web"
	"github.com/flarexes/offsync/go-web/controllers"
)

func init() {
	beego.Router("/", &controllers.OffsyncController{})
	beego.Router("/submit", &controllers.OffsyncController{}, "post:Post")
}
