package practice

import (
	"context"
	"io"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

type trackingBody struct {
	io.Reader
	closed bool
}

func (b *trackingBody) Close() error { b.closed = true; return nil }

type roundTrip func(*http.Request) (*http.Response, error)

func (f roundTrip) RoundTrip(r *http.Request) (*http.Response, error) { return f(r) }
func TestFetch(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.Method != "GET" {
			t.Error(r.Method)
		}
		w.WriteHeader(404)
	}))
	defer server.Close()
	got, err := FetchStatus(context.Background(), server.Client(), server.URL)
	if err != nil || got != 404 {
		t.Fatal(got, err)
	}
	ctx, cancel := context.WithCancel(context.Background())
	cancel()
	if _, err := FetchStatus(ctx, server.Client(), server.URL); err == nil {
		t.Fatal("expected cancellation")
	}
	body := &trackingBody{Reader: strings.NewReader("ok")}
	client := &http.Client{Transport: roundTrip(func(r *http.Request) (*http.Response, error) {
		return &http.Response{StatusCode: 200, Body: body, Header: make(http.Header)}, nil
	})}
	if _, err := FetchStatus(context.Background(), client, "http://example.test"); err != nil {
		t.Fatal(err)
	}
	if !body.closed {
		t.Fatal("body not closed")
	}
}
