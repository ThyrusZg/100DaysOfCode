100 days of code notes
==============

## Day2
x = 324_123.45  
This is **float** type. In this case "_" is there for visibility due to the big number. When printing number in the
console, underscore will be removed.

Mathematical functions in priority order: 
- 1 ()
- 2 **
- 3 //
- 4 * or /
- 5 + or -

When there is both * and / example: a*b/c it * and / have same priority but * will be executed first because it is most
left. So priority is looked form left to right when same mathematical priority is between mathematical functions. 

## Day3 

False or True or False  this code will be evaluated as true

## Day4

    def function_1(text):
        return text + text

    def function_2(text):
        return text.title()
    
    output = function_2(function_1("hello"))
    print(output) -> output is "Hellohello"


## Day 33

Fun naming for response status codes

- 1xx - Hold on (informational response)
- 2xx - Here you go (successful )
- 3xx - Go Away (redirection )
- 4xx - You Screwed Up (client error)
- 5xx - I Screwed Up (server error)