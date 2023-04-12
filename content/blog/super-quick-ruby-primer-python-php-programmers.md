---
title: A super quick Ruby primer for Python and PHP programmers
description: 
date_created: 2014-01-19
---

Recently, I've been looking at learning Ruby, but couldn't find a tutorial that didn't take me for a complete idiot. As you might expect, Ruby has a pretty standard way of adding two and two, setting variables and whatnot.

Instead of wasting your time with the obvious stuff, let me walk you through Ruby like a grown up.

**The interactive shell**

To open an interactive shell, type `irb` in your terminal. This is equivalent to `python` or `php -a`.

**A simple Ruby class**

Here's a simple, well-commented Ruby class:

```
=begin
In Ruby, docs are above their block and not under them as in
Python. RDoc is the standard documentation format.
Rhttp://rdoc.sourceforge.net/doc/

By the way, this is a block comment. It starts with =begin
and ends with =end. Notice how =end must be on its own line.
=end
class Husky < Dog # A husky is a dog. Also: single inheritance
 # initialize() is the ruby constructor
 def initialize(name = 'Fido')
 @name = name
 super()
 end

 # no parameters? no parenthesis.
 # this returns nil, the Ruby equivalent of null/None
 def say_name
 # Quotes work as in PHP:
 # * single-quoted strings are returned as-is
 # * double-quoted strings are interpolated
 puts 'Hello!'
 puts "My name is #{@name}"
 # @name refers to the instance variable name.
 # it's equivalent to Python's self or PHP's this
 end

 # you don't need to use 'return' in Ruby. just use the variable
 def name_tag
 name_tag = "%s, Dog, %d years old" % [
 @name,
 4
 ] # 'Steve, Dog, 4 years old'

 name_tag # Returns name_tag
 end

 # this is a static method
 # call it with Husky.bark, not mydog.bark
 def Husky.bark
 puts 'Woof!' # puts works like print in Python
 print 'I am' # print works like echo
 print 'a dog' # it doesn't add a line break at the end
 end
end

```

You can then use your class like this:

```
steve = Husky.new('Steve') # Steve the Husky
steve.say_name() # Parenthesis are optional
Husky.bark

```

**Operators**

Operators in Ruby are pretty standard. The only oddity is the power operator: `3**2` is equivalent to `3^2` in many languages. We use `and` and `or` for comparison, not `&&` and `||`.

**Collections**

Ruby lists are pretty simple:

```
list = ['one', 'two', 3, 'four']
list[0] # 'one'
list.length # 4
list[-1] # 'four'

```

Associative arrays (we call them hashes) work a bit like in PHP:

```
billy = {
 'first_name' => 'Billy',
 'last_name' => 'Kidd',
 'age' => 12,
}
billy['age'] # 12

```

You can iterate over them in a syntax you might be familiar with:

```
for element in my_list
 ...
end

for key, value in my_hash
 ...
end

```

**If, while and others**

Ruby uses `if`, `elsif` and `else`. There is no need to put the conditions between parenthesis, just like in Python. Each block is closed by `end`.

**Other details**

By convention, Ruby uses two spaces for indentation.

