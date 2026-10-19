package practice

import (
	"encoding/json"
	"net/http/httptest"
	"strings"
	"testing"
)

func TestHealth(t *testing.T) {
	handler := HealthHandler()
	for _, tc := range []struct {
		method, path string
		status       int
	}{{"GET", "/health", 200}, {"POST", "/health", 405}, {"GET", "/missing", 404}, {"POST", "/missing", 404}} {
		recorder := httptest.NewRecorder()
		handler.ServeHTTP(recorder, httptest.NewRequest(tc.method, tc.path, nil))
		if recorder.Code != tc.status {
			t.Errorf("%s %s: %d", tc.method, tc.path, recorder.Code)
		}
		if tc.status == 200 {
			var body map[string]string
			if err := json.Unmarshal(recorder.Body.Bytes(), &body); err != nil || body["status"] != "ok" {
				t.Fatal(recorder.Body.String())
			}
			if !strings.Contains(recorder.Header().Get("Content-Type"), "application/json") {
				t.Fatal("content type")
			}
		}
		if tc.status == 405 && recorder.Header().Get("Allow") != "GET" {
			t.Fatal("missing Allow")
		}
	}
}
