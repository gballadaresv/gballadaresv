  
# Define a hash like in Python (dictionaries are called hashes in ruby)
hash = { 
	"one": 1, 
	"two": 2, 
	"three": 3 
}

symbol_hash = { :one => 1, :two => 2, :three => 3 }

puts "HASHES"
# Log hashes generated... They are IDENTICAL!
puts hash
puts symbol_hash


# WHAAAAAAT?? Strings get transformed to symbols when used inside
# the hash's definition...
puts hash[:one]
puts symbol_hash[:one]

# Add some elements...
hash["four"] = 4
hash[:five] = 5 

# Now, the string does not get converted to a symbol!
puts hash["four"]
puts hash[:five]
puts hash # WHAAAT?!?!?

# ProTip: when a hash is the last argument given to a method,
# {} brackets can be omitted inside the method call. For example:

puts "uno": 1, "dos": 2, "tres": 3

# Is the same as saying:

puts({"uno": 1, "dos": 2, "tres": 3})
