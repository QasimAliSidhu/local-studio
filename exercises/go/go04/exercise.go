package practice

import "errors"

var ErrNotFound = errors.New("not found")

func Lookup(values map[string]string, key string) (string, error) { panic("TODO") }
