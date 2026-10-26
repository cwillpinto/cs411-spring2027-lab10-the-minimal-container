package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestHealth(t *testing.T) {
	req := httptest.NewRequest(http.MethodGet, "/health", nil)
	w := httptest.NewRecorder()
	handler().ServeHTTP(w, req)
	if w.Code != http.StatusOK || w.Body.String() != "ok\n" {
		t.Fatalf("health=%d %q", w.Code, w.Body.String())
	}
}
