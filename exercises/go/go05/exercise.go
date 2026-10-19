package practice

import "io"

type Task struct {
	Title string `json:"title"`
	Done  bool   `json:"done"`
}

func DecodeTask(r io.Reader) (Task, error) { panic("TODO") }
