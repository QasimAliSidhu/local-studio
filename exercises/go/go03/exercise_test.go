package practice

import "testing"

type fileSize int64

func (f fileSize) Size() int64 { return int64(f) }

type blob struct{ bytes int64 }

func (b blob) Size() int64 { return b.bytes }
func TestTotalSize(t *testing.T) {
	if got := TotalSize([]Sized{fileSize(20), blob{35}}); got != 55 {
		t.Fatal(got)
	}
	if got := TotalSize(nil); got != 0 {
		t.Fatal(got)
	}
}
