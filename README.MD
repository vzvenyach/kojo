# Explanation

On March 24, 2014, a group of DC Open Government folks went on the Kojo Nnamdi show to discuss DCDecoded.org. As a demonstration project for myself and very few other people, I built a little application that emails me daily updates with the guests for the coming day.

# Usage

1. Clone the repository

2. Create an .env file from the .env.example

3. Set up a crontab -e line, mine is as follows:

`0 10 * * * cd /path/to/kojo/ ; foreman start`

4. Enjoy the daily email!

# License

Public Domain