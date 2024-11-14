package models

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/binary"
	"math/rand"

	"golang.org/x/crypto/pbkdf2"
)

const letterBytes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"

func generateHMAC(secret, site, counter string) []byte {
	secretBytes := []byte(secret)
	messageBytes := []byte(site + counter)

	h := hmac.New(sha256.New, secretBytes)
	h.Write(messageBytes)

	return h.Sum(nil)
}

func generatePBKDF2Key(password, salt []byte) []byte {
	iterations := 100000
	keyLen := 32

	return pbkdf2.Key(password, salt, iterations, keyLen, sha256.New)
}

func GeneratePassword(profile Profile) string {
	salt := generateHMAC(profile.Secret, profile.Site, profile.Counter)
	hash := generatePBKDF2Key([]byte(profile.Secret), salt)
	seed := int64(binary.BigEndian.Uint64(hash[:8]))
	rand := rand.New(rand.NewSource(seed))
	length := profile.Length
	password := make([]byte, length)

	for i := 0; i < length; i++ {
		password[i] = letterBytes[rand.Intn(len(letterBytes))]
	}
	return string(password)
}
