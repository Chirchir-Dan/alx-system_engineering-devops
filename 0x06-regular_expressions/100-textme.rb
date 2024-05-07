#!/usr/bin/env ruby

# Define a method to extract sender, receiver, and flags from a text message transaction
def extract_info(text_message)
  # Define the regular expression pattern to match the transaction format
  regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

  # Match the transaction format using the regular expression
  match_data = text_message.match(regex)

  # Check if the match was successful
  if match_data
    # Extract sender, receiver, and flags from the matched data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]

    # Output the extracted information
    puts "#{sender},#{receiver},#{flags}"
  else
    # If no match was found, output a message indicating that the input format is invalid
    puts "Invalid input format: #{text_message}"
  end
end

# Accept one argument from the command line
text_message = ARGV[0]

# Call the method with the input argument
extract_info(text_message)
