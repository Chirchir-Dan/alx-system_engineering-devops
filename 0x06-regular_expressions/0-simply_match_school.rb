#!/usr/bin/env ruby

# Define a method to match the regular expression
def match_school(input)
  # Define the regular expression
  regex = /School/

  # Use the regular expression to find matches in the input
  matches = input.scan(regex)

  # Print the matched parts of the input string
  puts matches.join('')
end

# Accept one argument from the command line
input_argument = ARGV[0]

# Call the method with the input argument
match_school(input_argument)
