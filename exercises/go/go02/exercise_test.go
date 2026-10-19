package practice

import (
	"reflect"
	"testing"
)

func TestWords(t *testing.T) {
	got := WordCounts("Go go\tPYTHON\nGo!")
	if !reflect.DeepEqual(got, map[string]int{"go": 2, "python": 1, "go!": 1}) {
		t.Fatal(got)
	}
	if got := WordCounts(" "); got == nil || len(got) != 0 {
		t.Fatal(got)
	}
}
