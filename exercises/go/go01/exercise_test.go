package practice

import "testing"

func TestInvoice(t *testing.T) {
	got, err := InvoiceTotal([]int{125, 200}, []int{3, 2})
	if err != nil || got != 775 {
		t.Fatalf("got %d, %v", got, err)
	}
	got, err = InvoiceTotal(nil, nil)
	if err != nil || got != 0 {
		t.Fatal(got, err)
	}
	for _, pair := range [][2][]int{{{1}, {}}, {{-1}, {1}}, {{1}, {-1}}} {
		if _, err := InvoiceTotal(pair[0], pair[1]); err == nil {
			t.Fatal("expected error")
		}
	}
}
