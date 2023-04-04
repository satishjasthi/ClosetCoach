#!/bin/bash

output_directory="./db_dump"

mongorestore --dir "$output_directory"