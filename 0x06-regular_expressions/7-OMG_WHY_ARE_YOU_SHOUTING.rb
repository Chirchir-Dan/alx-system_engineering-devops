#!/usr/bin/env ruby

# Define a method to match capital letters
def match_capital_letters(input)
  # Define the regular expression
  regex = /[A-Z]/

  # Use the regular expression to find matches in the input
  matches = input.scan(regex)

  # Print the matched capital letters joined into a single string
  puts matches.join("")
end

# Accept one argument from the command line
input_argument = ARGV[0]

# Call the method with the input argument
match_capital_letters(input_argument)
