# 🐍Python Django Real Estate website

A real estate listings website built with `python` `django` `bootstrap` and deployed with `Digital Ocean`.

[![Project](https://img.shields.io/badge/Project-Python-green.svg)](https://bankole2000.github.io/githubfinder)

_<p align="center">"Snakes on guitars... The new beat of the web"</p>_

<div align="center" style="text-align:center; margin:auto;">
<img align="center" src="https://i.imgur.com/AD74eQP.gif" width="150"/>
</div>

A learning oriented web project ... (Kept thinking to myself _"how/why the hell haven't I built one all these years?_ o.O" - well now I have, lol ). Built with `python-django` `bootstrap4` and a little `javascript ES6` and `JQuery`.

## What it is

A simple, reponsive portfolio website. Built with:

- Python 🐍
- Django 🎸
- Bootstrap 4 🌈
- Vanilla JS - ES6
- JQuery
- [Patience](https://www.wikihow.com/Love-Programming) - Strictly for the love of coding _Mehn!_

## What it does

- Display Real Estate Listings with Realtors and Details
- Try to look pretty, simple, and hopefully not too formal.
- Customized django Backend for managing the entire Site 
- Links Single Listing details page to contact Realtor
- Realtor Contact Form and Email SMTP 
- 
## Learning Points

- Django Mixins
- Django functions
- Responsive design & media queries
- CSS Grid
- Flexbox
- CSS Animations/transitions
- Psuedo Elements

## Issues

1. **Node sass error**

Compiling `.scss` files with `node-sass` using the following script in `package.json`

```json
"scripts": {
    "sass": "node-sass -w scss/ -o dist/css/ --recursive"
  }
```

produced certain errors on VSCode on windows, specifically =>

```json
{
  "status": 3,
  "message": "File to read not found or unreadable: C:/Users/Urhiafe Patience/projects/portfolio/scss/main.scss",
  "formatted": "Internal Error: File to read not found or unreadable: C:/Users/Urhiafe Patience/projects/portfolio/scss/main.scss\n"
}
```

To fix this, I used a solution I found [here](https://github.com/michaelwayman/node-sass-chokidar/issues/22), replacing the contents of the `node_modules/node-sass/lib/render.js` file with [this patched file](https://github.com/marcosbozzani/node-sass/blob/bug-vscode-watch/lib/render.js). Started rendering properly afterwards

2. **Overriding CSS**

while coding the responsiveness (using media queries defined in the `_config` and `_mobile` partials), the css began to overide each other, with css on earlier lines being overridden by css in later lines (something i learnt from jen Simmons) like so =>

```css
main#home h1 {
  // @media small screens
  margin-top: 5vh;
}
main#home h1 {
  // @media larger screens
  margin-top: 20vh;
}
```

So earlier occuring css is overriden in the browser like this =>
~~main#home h1 {
margin-top: 5vh;
}~~ while later css is implemented. Thus to ensure that responsive css is applied by the browser, I imported the `_mobile.scss` file last in the `main.scss` file

## Acknowledgments

- Many thanks to [@bradtraversy](https://github.com/bradtraversy) for his awesome courses - _i will not fail you sensei_
- Thanks to [@torvalds](https://github.com/torvalds) For Making the world a better place
- And To anyone reading this... _You're awesome!_

_<p align="center">And remember from here on end... History has it's eyes on you...</p>_
