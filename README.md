


## Description

This repository contains a Django script designed to automate the generation of fictitious financial transaction data for development and testing purposes. The script creates random transactions for predefined users based on pre-configured categories and monetary ranges, facilitating the process of verifying different application behaviors and enhancing testing quality.
## Features

- **Random Transaction Data**: Generates transaction data with random amounts and dates within specified ranges.
- **Customizable Categories and Amounts**: Allows configuration of transaction categories and their corresponding amount ranges.
- **Multiple Users**: Supports generating transactions for multiple predefined users.
- **Year-Specific Data Generation**: Capable of generating data for multiple years.


## How It Works

The script uses predefined user names to find users in the database. It then proceeds to generate transactions based on the categories and their specified monetary ranges. Each user will have transactions created for each category for the years specified in the script.

Here's a breakdown of the script's logic:

- **User Filtering**: Fetches users from the database based on predefined usernames.
- **Random Date Generation**: For each transaction, a random date within the specified year is generated.
- **Transaction Creation**: For each category, two transactions per user per year are created with random descriptions and amounts within defined limits.


