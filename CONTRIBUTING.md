# Contributing
Carefully read this before making a pull request or an issue.

# Issues
Always check the documentation or examples first.

**Always** use *Google* first. (seriously, do it)

If you want to report a bug, tell us the version (commit #) and OS you're using, search first, and give steps to reproduce with minimal code (if applicable).

# Pull requests
I. No plagiarized/stolen/copyrighted/patented code or material. No code or material from an incompatible license (i.e. GPL).

II. Describe what your code does well, and test it first.

III. Always follow project code style. "(suggested)" = optional but preferred (see below).

# Code style
## General
### Parentheses and spaces
Don't use spaces inside parenthesis. (required)

Use spaces in math, unless the line is already approaching the character limit. (suggested)

    -- GOOD
    fn(x + y)
    num_lemons = num_lemons + 1
    z = z * (abc / 2)

### Comments
Keep comments to a reasonable minimum. Need more than a comment or two every few hundred lines? Fix your code. (required)

### Functions
No monolithic functions. Break up into smaller functions. (required)

### Lines
Try hard to keep lines under 100 characters. Newline after, unless that would result in worse readability. (required)

### Semicolons
Lua supports semicolons, but does not require them. Do not use semicolons in Lua. (required)

### Objects (metatables)
Avoid creating new objects unless absolutely neccesary. Use `anim` for temporary animations. (required)

Don't waste CPU/RAM by loading resources in an object's `new` function. Use `precache`. (required)

## Identifiers and statements
Strive for simplicity in implementation. Avoid verbosity. Absolute minimum to make your code readable and unambiguous, no silly abstractions. See [Worse is Better](https://www.jwz.org/doc/worse-is-better.html). (required)

Always use snake_case where possible. (required)

Avoid using a single-char prefix with snake_case. (e.g. prefer `num_lemons` over `n_lemons`) (suggested)

### GOOD

    function player:shoot_lemon(x, y)
        if (x and y) then
            self.lemons[num_lemons] = lemon_shot.new(x+2, y-1)
            num_lemons = num_lemons + 1
        end
    end

### BAD (strongly exaggerated)

    function ObjectPlayer:doShootBusterLemon(offsetX, offsetY)
        if (offsetX ~= nil and offsetY ~= nil) then
            local busterFactory = busterShotFactory.new()
            self.busterLemons:addLemon(busterFactory:newLemon(offsetX+2, offsetY-1))
            busterFactory.kill()
            numberOfLemons = numberOfLemons + 1
        end
    end

## Indentation
Indent with real tabs. They are intended to be displayed as 4 characters in both Lua and C. (required)

If line becomes too long (~100ch max) use newline and indent with tabs & spaces. See below. (required)

Use a single tab to indent multi-line function arguments if applicable. (required)

Character `*` respresents `<space>`, `>-` represents `<tab>`

### GOOD

    function foo(x)
    >---if (x) then
    >--->---too_long_name(very_very_very_long_argument01,
    >--->--->---very_very_very_long_argument02,
    >--->--->---very_very_very_long_argument03)
    >---end
    end

### BAD

    function foo(x)
    **if (x) then
    ****too_long_name(very_very_very_long_argument01,
    ******************very_very_very_long_argument02,
    ******************very_very_very_long_argument03)
    **end
    end

## Variable declaration
Always declare local variables `local`. (required)

Try to declare each local variable at the start of a function or block. (suggested)

### GOOD

    function foo()
        local abc = ""
        local tmp
        
        tmp = get_something(abd)
        abc = process(tmp)
        fn(abc, tmp)
    end

### BAD

    function foo()
        tmp = get_something() -- really bad
        
        abc = ""
        abc = process(tmp)
        
        fn(abc, tmp)
    end

## If statements
Always enclose conditions in parentheses. (required)

Enclose math/logic in parentheses if it helps improve readability. (suggested)

### GOOD

    if (x == 2 and (fn(x ^ (2 * z)) ~= 3)) then
        foo()
    end

### BAD

    if x == 2 and fn(x^2*z) ~= 3 then
        foo()
    end
