#!/usr/bin/env ruby
#Ruby script that accepts 1 argument, pass it to a regex matching method
puts ARGV[0].scan(/hb{2,5}n/).join
