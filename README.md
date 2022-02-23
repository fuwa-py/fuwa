<h1 align="center">
<sub>
    <img src="https://raw.githubusercontent.com/fuwa-py/fuwa/main/.github/icon.png" height="36">
</sub>
&nbsp;
Fuwa
</h1>
<p align="center">
<sup>
A set of scalable and powerful python packages built for the Discord API, that heavily encourage pragmatic design.
</sup>
<br>
<sup>
    <a href="">Read the documentation.</a>
</sup>
</p>

## Information

Fuwa is a set of scalable and powerful python packages built for the Discord API, that heavily encourage pragmatic design, inspired heavily by twilight-rs.

The eco-system of packages will soon include packages for `http`, `OAuth`, an application `Command Framework` and much more.

## Installation

Thanks to Python's installation syntax, it's pretty simple to install fuwa, and its corresponding packages. Let's look at an example. The gateway.

To install any of the fuwa packages, you do not need to have the first-class fuwa package installed, as `pip` will manage this for you.

To install the gateway (as an example), simply run:

```bash
pip install fuwa[gateway]
```

See, simply right! To find out what the following requirement extra is, simply visit the respective github page for each of the packages.


## Core Packages

### [`fuwa-gateway`](https://github.com/fuwa-py/fuwa-gateway)
The gateway handler for the fuwa package eco-system. Incredibly low-level support, so its not recommended you use this on your own. Many future Fuwa packages will depend on this package in the future, such as the command framework.