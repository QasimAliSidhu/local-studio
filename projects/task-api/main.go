package main

import (
	"encoding/json"
	"log"
	"net/http"
	"time"
)

// Start here, then add task routes using the course 18 brief.
func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet {
			w.Header().Set("Allow", "GET")
			http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
	})
	server := &http.Server{Addr: "127.0.0.1:8080", Handler: mux, ReadHeaderTimeout: 5 * time.Second}
	log.Printf("Task API starter listening on http://%s", server.Addr)
	log.Fatal(server.ListenAndServe())
}
