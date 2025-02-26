# fonts api
learning to build a web api

## features
- FREEEEEEEEE
- database with some fonts i used
- getting fonts by various methods
    - id
    - name
    - family
    - projects
    - (sans)serif
    - random
- will hopefully turn this into a gallery on my [website](https://mynteee.github.io/) eventually
- possible images and otf/files coming if i feel like it

## use
go to [https://mynte.pythonanywhere.com/items](https://mynte.pythonanywhere.com/items). this will return the entire database. from here you can sort to whatever is your use case is by appending the appropriate subpath to the link above and parameters which can be found below. if ur still confused just read the code lol.

### 1. id 
**/[id]** where **[id]** is some whole number (probably) that i assigned to the font and has no real meaning otherwise will return the font with that id
### 2. name 
**/name/[name]** where **[name]** is the name of the font according to css, if that doenst work then its according to google, otherwise its whatever i have on my computer will return the font with that name (if the name has multiple words still use a space in between; -'s should also work)
### 3. family 
**/family/[family]** where **[family]** is one of the 5 generic font families set out by css (serif, sans-serif, monospace, cursive, fantasy) will retusn all the fonts in that family
### 4. project 
**/project/[project]** where **[project]** is the project the font was used in will return all the fonts used in that project
### 5. serif 
**/serif** will return all the serif fonts
### 6. sans-serif 
**/sans-serif** will return all the sans-serif fonts
### 7. random 
**/random** will get you a random font

## contributing
just make a pull request and if its a cool font why not or if you do something else cool thats nice too \
\
thanks for reading have fun