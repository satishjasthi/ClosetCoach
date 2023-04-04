#!/bin/bash

database_name="ClosetCoach"
output_directory="./db_dump"

mongodump --db "$database_name" --out "$output_directory"
