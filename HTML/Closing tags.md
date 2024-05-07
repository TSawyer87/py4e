- The `</body>` and `</html>` put a close to their respective elements.

> [!i]
> Not all tags have closing tags like this (`<html></html>`) some tags, which do not wrap around content will close themselves. The line-break tag for example, looks like this : `<br>` - a line break doesn’t hold any content so the tag merrily sits by its lonely self. We will come across these examples later. All you need to remember is that all tags with content between them should be closed, in the format of opening tag → content → closing tag. It isn’t, strictly speaking, always a requirement, but it’s a convention we’re using in these tutorials because it’s good practice that results in cleaner, easier to understand code.

> [!self-closing]
> You might come across “self-closing” tags, whereby a [`br`](https://www.htmldog.com/references/html/tags/br/) tag, for example, will look like “`<br />`” instead of simply “`<br>`”. This is a remnant of XHTML, a form of HTML based on another markup language called XML. HTML5 is much more chilled out than XHTML and will be happy with either format. Some developers prefer one way, some prefer the other. We tossed a coin and decided to stick with the simpler version.

[[Attributes]]