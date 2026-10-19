package practice

type Sized interface{ Size() int64 }

func TotalSize(items []Sized) int64 { panic("TODO") }
