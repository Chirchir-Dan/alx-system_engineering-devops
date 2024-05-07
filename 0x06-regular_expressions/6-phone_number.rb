#!/usr/bin/env ruby

# Define a method to match the regular expression
def match_phone_number(input)
  # Define the regular expression
  regex = /^\d{10}$/

  # Check if input matches the regular expression
  if input =~ regex
    puts "#{input}"
  else
    puts
  end
end

# Accept one argument from the command line
input_argument = ARGV[0]

# Call the method with the input argument
match_phone_number(input_argument)
