# Python for Finance – Second Edition
This is the code repository for [Python for Finance – Second Edition](https://www.packtpub.com/big-data-and-business-intelligence/python-finance-second-edition?utm_source=github&utm_medium=repository&utm_content=9781787125698), published by Packt. It contains all the supporting project files necessary to work through the book from start to finish.

## About the book
This book uses Python as the computational tool. Since Python is free, any schools or organizations can download and use it. It is a powerful tool for quantitative finance, financial engineering programs, and quantitative master degree programs.

The second edition made several adjustments. First, it reorganizes the book according to various finance subjects. In other words, the first edition focuses more on Python while the second edition is truly trying to apply Python to finance.

The book starts with explaining topics exclusively related to Python. Then we see deal with critical parts of python language explaining concepts like Time Value of Money Stock and Bond Evaluations, Capital Asset Pricing Model , Multi-factor models, Time Series Analysis, Portfolio Theory, Options and Futures , Value at Risk, Monte Carlo Simulation , Credit Risk Analysis, Exotic Option, and Volatility, Implied volatility, ARCH and GARCH .

This book will help us to learn or review the basics of quantitative finance and apply Python to solve various problems such as estimate IBM’s market risk, run a Fama-French 3-factor, 5-factor or Fama-French-Carhart 4 factor models, estimate VaR of a 5-stock portfolio , estimate the optimal portfolio and construct their efficient frontier for a 20 stock portfolio with real-world stocks, with Monte Carlo Simulation. Later, we will also learn how to replicate famous Black-Scholes-Merton option models and how to price some exotic options such as average price call option.

## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter 03.

The code will look like the following:
   
        def pvFunction(fv,r,n):
            return fv/(1+r)**n
        def pvPerpetuity(c,r):
            return c/r
        def pvPerpetuityDue(c,r):
            return c/r*(1+r)
        def pvAnnuity(c,r,n):
            return c/r*(1-1/(1+r)**n) 
        def pvAnnuityDue(c,r,n):
            return c/r*(1-1/(1+r)**n)*(1+r)
        def pvGrowingAnnuity(c,r,n,g):
            return c/r*(1-(1+g)**n/(1+r)**n)

## Software requirements:
 The computational tool used by the book is Python which is free. There are many ways to download this wonderful software. The book introduces three ways to do so: download and install Python via Canopy (Enthought), via Spyder (Anaconda) or download and install Python directly. The Enthought and Anaconda could be viewed as a super package. 
 
### Method #1: installing Python via Enthought
 To install Python, go to the related web page at https://store.enthought.com/downloads/#default. Depend on the operating system, users could download Canopy, such as windows 32-bit. 
 
### Method #2: installing Python via Anaconda 
Go to http://continuum.io/downloads, then find an appropriate package. There exists two versions of 3.5 and 2.7. For this book, the version is not that critical. The old version had fewer problems while the new one usually has new improvements. The version of Anaconda is 4.2.0. Since we would launch Python through Spyder, it might have different versions as well.

#### Launch Python via Spyder
After Python is installed via Anaconda, navigate to Start | All Programs | Anaconda.

### Method #3: Installing Python directly
For most users, knowing how to install Python via Anaconda is more than enough. Just for completeness, here the second way to install Python is presented. There are two steps involved. First, go to http://www.python.org/download.Depending on your computer, choose the appropriate package, for example, Python 3.5.2 version. For this book the version of Python is not important.To launch Python, we could click IDLE (Python 3.5. 32 bit).

### Note:
The code files for all the chapters are given. For chapter05, packages are given so inorder to use the code, refer the chapter.

## Related Products:
* [Python for Finance](https://www.packtpub.com/application-development/python-finance?utm_source=github&utm_medium=repository&utm_content=9781783284375)

* [Mastering Python for Finance](https://www.packtpub.com/big-data-and-business-intelligence/mastering-python-finance?utm_source=github&utm_medium=repository&utm_content=9781784394516)

* [Python: Data Analytics and Visualization](https://www.packtpub.com/big-data-and-business-intelligence/python-data-analytics-and-visualization?utm_source=github&utm_medium=repository&utm_content=9781788290098)
