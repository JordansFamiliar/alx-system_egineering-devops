#!/usr/bin/env ruby
sender = ARGV[0].scan(/(?<=from:)[^\]]+/)
receiver = ARGV[0].scan(/(?<=to:)[^\]]+/)
flags = ARGV[0].scan(/(?<=flags:)[^\]]+/)
output = "#{sender.join(",")},#{receiver.join(",")},#{flags.join}"
puts output
