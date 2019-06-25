This is my blog, finally live here: https://rebeccalowe.herokuapp.com/
I'd give it a domain, but I need a good name first. I'm bad at naming things.

This blog was started by following these tutorials:
https://tutorial.djangogirls.org/en/
https://tutorial-extensions.djangogirls.org/en/

Things I've added outside the tutorial:

-I did all my own CSS/HTML.

-I added an 'about' page.

-I added a footer and a navigation bar (currently only Home/About work).

-I truncated blog posts on the main page to 100 words.

-I adjusted the URLs to include slugs (though I'm currently working out how to just display the slug and only keep the pk as a reference)


Things to do (roughly in order):

-Fix the couple of pylint errors. Not sure why they're there and they don't seem to affect how the site runs but I should at least look into what they mean.

-Improve appearance, maybe add some JS.

-There has to be a way to do some HTML within posts, mostly for links. So work out how to do that.

-Add custom error pages.

-Add categories to posts.

-Add search to posts.

-Add resources page. This will probably be another Django app. It will be a list of links to sites that teach you programming/web design stuff.
    Each link will have a brief description and a category which will be used in a search function.

-Add contact page. Probably just a form that sends to my email.

-Create a proper home page. Will display posts but have an intro section above. Then there'll be a new navigation link for 'Blog' which goes to the posts.

-Add some kind of 'I'm not a robot' authentication in order to post a comment. Currently I have to approve comments before they are displayed which is not ideal.