```html

<DOCTYPE html>
<html>
<head>
    <title>My first web page</title>
</head>
<body>
    This is my first web page
    How exciting
</body>
</html>
```

In the browser the document looks like this:
```html
This is my first web page How exciting.
```
- The text is on the same line because browsers don't usually take any notice of what line your code is on.
- It also doesn't take notice of spaces.

If you want text to appear on different lines or, rather, if you intend there to be two distinct blocks of text (because, remember, HTML is about meaning, not presentation), you need to explicitly state that.
Change your two lines of content to look like this:
```html
<p>This is my first webpage</p>
<p>How exciting</p>
```
- The p tag is used for **paragraphs**
```html

<DOCTYPE html>
<html>
<head>
    <title>My first web page</title>
</head>
<body>
    <p>This is my first web page</p>
    <p>How exciting</p>
</body>
</html>
```

Now the webpage prints on two lines:
```html
This is my first web page
How exciting
```