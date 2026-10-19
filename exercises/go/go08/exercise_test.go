package practice

import (
	"context"
	"errors"
	"reflect"
	"testing"
)

func TestSquares(t *testing.T) {
	input := []int{3, -1, 2, 3}
	got, err := Squares(context.Background(), input, 2)
	if err != nil || !reflect.DeepEqual(got, []int{9, 1, 4, 9}) {
		t.Fatal(got, err)
	}
	if !reflect.DeepEqual(input, []int{3, -1, 2, 3}) {
		t.Fatal("input changed")
	}
	got, err = Squares(context.Background(), nil, 8)
	if err != nil || len(got) != 0 {
		t.Fatal(got, err)
	}
	if _, err := Squares(context.Background(), nil, 0); err == nil {
		t.Fatal("expected error")
	}
	ctx, cancel := context.WithCancel(context.Background())
	cancel()
	if _, err := Squares(ctx, []int{1, 2, 3}, 2); !errors.Is(err, context.Canceled) {
		t.Fatal(err)
	}
	many := make([]int, 10000)
	for i := range many {
		many[i] = i
	}
	got, err = Squares(context.Background(), many, 7)
	if err != nil {
		t.Fatal(err)
	}
	for i, v := range got {
		if v != i*i {
			t.Fatal(i, v)
		}
	}
}
