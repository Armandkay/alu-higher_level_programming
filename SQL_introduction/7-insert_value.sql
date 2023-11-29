#!/bin/bash

echo "Inserting new row..."
mysql -hlocalhost -uroot -p < 7-insert_value.sql

echo "Listing all rows..."
mysql -hlocalhost -uroot -p < 6-list_values.sql
