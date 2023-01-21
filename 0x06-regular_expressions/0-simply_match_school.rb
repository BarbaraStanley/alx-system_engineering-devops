#!/usr/bin/env ruby
# Ruby script that accepts 1 argument, pass it to a regex matching method

puts ARGV[0].scan(/School/).join
