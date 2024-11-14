package models

type Profile struct {
	Site     string `form:"site"`
	Username string `form:"username"`
	Secret   string `form:"secret"`
	Counter  string `form:"counter"`
	Length   int    `form:"length"`
}
