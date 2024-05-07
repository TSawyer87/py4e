- The basic structure of an HTML document includes tags, which surround the content and apply meaning to it.
- Open a plain text editor and type
```html
<!DOCTYPE html>
<html>
<body>
    This is my first web page
</body>
</html>
```
- Save to location of choosing i chose `/home/jr/html/myfirstpage.html'
- To open in a browser enter `/home/jr/html/myfirstpage.html` and press enter.

- The purpose of HTML is to apply meaning, not presentation.
- The first line on the top, `<!DOCTYPE html>`, is a **document type declaration** and it lets the browser know which flavor of HTML you're using (HTML 5, in this case).
- It's very important to stick this shebang in, if you dont browsers will assume you don't really know what you're doing and act in a very peculiar way.
- `<html>` is the **opening tag** that kicks things off and tells the browser that everything between that and the `</html>` **closing tag** is an HTML document.
- The stuff between `<body>` and `</body>` is the main content of the document that will appear in the browser window.
- [[Closing tags]]