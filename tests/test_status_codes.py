"""Tests for the ``requests.codes`` status code lookup."""

import requests


def test_early_hints_maps_to_103():
    # "Early Hints" is status 103 (RFC 8297), not 102 (Processing).
    assert requests.codes.get("early_hints") == 103
    assert requests.codes.get("early-hints") == 103
    assert requests.codes.get("EARLY_HINTS") == 103
    assert requests.codes.get("checkpoint") == 103


def test_processing_maps_to_102():
    assert requests.codes.get("processing") == 102
    assert requests.codes.get("PROCESSING") == 102
    # "early-hints" must no longer resolve to 102.
    assert requests.codes.get("early-hints") != 102
