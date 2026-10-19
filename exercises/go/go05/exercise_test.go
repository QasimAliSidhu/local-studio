package practice

import (
	"strings"
	"testing"
)

func TestDecode(t *testing.T) {
	task, err := DecodeTask(strings.NewReader(`{"title":" learn ","done":true}`))
	if err != nil || task.Title != "learn" || !task.Done {
		t.Fatal(task, err)
	}
	task, err = DecodeTask(strings.NewReader(`{"title":"learn"}`))
	if err != nil || task.Done {
		t.Fatal(task, err)
	}
	for _, text := range []string{``, `{`, `null`, `[]`, `{}`, `{"title":" "}`, `{"title":"x","admin":true}`, `{"title":"x"} {}`, `{"title":"x"} garbage`, `{"title":1}`} {
		if _, err := DecodeTask(strings.NewReader(text)); err == nil {
			t.Errorf("accepted %q", text)
		}
	}
}
