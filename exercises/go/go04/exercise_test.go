package practice

import (
	"errors"
	"strings"
	"testing"
)

func TestLookup(t *testing.T) {
	for _, value := range []string{"value", ""} {
		got, err := Lookup(map[string]string{"key": value}, "key")
		if err != nil || got != value {
			t.Fatal(got, err)
		}
	}
	_, err := Lookup(nil, "missing")
	if !errors.Is(err, ErrNotFound) || !strings.Contains(err.Error(), "missing") {
		t.Fatal(err)
	}
}
