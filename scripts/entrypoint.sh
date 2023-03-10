#!/bin/sh

uvicorn roombooking.main:app --host 0.0.0.0 --port "${API_PORT}" "${UVICORN_ARGS}"