#!/usr/bin/ruby
# 2-sort.rb

def sort_arguments(*args)
  numeric_args = args.select { |arg| arg.is_a?(Numeric) }
  non_numeric_args = args.select { |arg| !arg.is_a?(Numeric) }

  sorted_numeric_args = numeric_args.sort
  sorted_args = sorted_numeric_args + non_numeric_args

  sorted_args.each { |arg| puts arg }
end

if __FILE__ == $PROGRAM_NAME
  args = ARGV.map { |arg| arg.to_i.to_s == arg ? arg.to_i : arg }
  sort_arguments(*args)
end
