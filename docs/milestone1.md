## Introduction

Differentiation is one of the most important operations in science.  Finding extrema of functions and determining zeros of functions are central to optimization.  Numerically solving differential equations forms a cornerstone of modern science and engineering and is intimately linked with predictive science.

In the introduction, we motivated the need for computational techniques to compute derivatives.  The focus in the introduction was on the finite difference method, but we also computed a symbolic derivative.  The finite difference approach is nice because it is quick and easy.  However, it suffers from accuracy and stability problems.  On the other hand, symbolic derivatives can be evaluated to machine precision, but can be costly to evaluate.  We'll have more to say about cost of symbolic differentiation later.

Automatic differentiation (AD) overcomes both of these deficiencies.  It is less costly than symbolic differentiation while evaluating derivatives to machine precision.  There are two modes of automatic differentiation: forward and reverse.  This course will be primarily concerned with the forward mode.  Time-permitting, we will give an introduction to the reverse mode.  In fact, the famous backpropagation algorithm from machine learn is a special case of the reverse mode of automatic differentiation.
### Problem



### Why



## Background

### Chain Rule

## Review of the Chain Rule

At the heart of AD is the famous *chain rule* from calculus.

### Back to the Beginning
Suppose we have a function $h\left(u\left(t\right)\right)$ and we want the derivative of $h$ with respect to $t$.  The derivative is $$\dfrac{\partial h}{\partial t} = \dfrac{\partial h}{\partial u}\dfrac{\partial u}{\partial t}.$$  This is the rule that we used in symbolically computing the derivative of the function $f\left(x\right) = x - \exp\left(-2\sin^{2}\left(4x\right)\right)$ earlier.

### Adding an Argument
Now suppose $h$ has another argument so that we have $h\left(u\left(t\right),v\left(t\right)\right)$.  Once again, we want the derivative of $h$ with respect to $t$.  Applying the chain rule in this case gives
\begin{align}
  \displaystyle 
  \frac{\partial h}{\partial t} = \frac{\partial h}{\partial u}\frac{\partial u}{\partial t} + \frac{\partial h}{\partial v}\frac{\partial v}{\partial t}.
\end{align}

### The Gradient
What if we replace $t$ by a vector $x\in\mathbb{R}^{m}$?  Now we want the gradient of $h$ with respect to $x$.  We write $h = h\left(u\left(x\right),v\left(x\right)\right)$ and the derivative is now 
\begin{align}
  \nabla_{x} h = \frac{\partial h}{\partial u}\nabla u + \frac{\partial h}{\partial v} \nabla v
\end{align}
where we have written $\nabla_{x}$ on the left hand side to avoid any confusion with arguments.  The gradient operator on the right hand side is clearly with respect to $x$ since $u$ and $v$ have no other arguments.

### The General Rule
In general $h = h\left(y\left(x\right)\right)$ where $y\in\mathbb{R}^{n}$ and $x\in\mathbb{R}^{m}$.  Now $h$ is a function of possibly $n$ other functions themselves a function of $m$ variables.  The gradient of $h$ is now given by 
\begin{align}
  \nabla_{x}h = \sum_{i=1}^{n}{\frac{\partial h}{\partial y_{i}}\nabla y_{i}\left(x\right)}.
\end{align}

### Graph Structure on Calculations

## The Computational Graph
Consider again the example function $$f\left(x\right) = x - \exp\left(-2\sin^{2}\left(4x\right)\right).$$  We'd like to evalute $f$ at the point $a$.  In the graph, we indicate the input value as $x$ and the output value as $f$.  Note that $x$ should take on whatever value you want it to.

Let's find $f\left(\dfrac{\pi}{16}\right)$.  The evaluation trace looks like:

| Trace    | Elementary Operation                   | Numerical Value                  |
| :------: | :----------------------:               | :------------------------------: |
| $x_{1}$  | $\dfrac{\pi}{16}$                      | $\dfrac{\pi}{16}$                |
| $x_{2}$  | $4x_{1}$                               | $\dfrac{\pi}{4}$                 |
| $x_{3}$  | $\sin\left(x_{2}\right)$               | $\dfrac{\sqrt{2}}{2}$            |
| $x_{4}$  | $x_{3}^{2}$                            | $\dfrac{1}{2}$                   |
| $x_{5}$  | $-2x_{4}$                              | $-1$                             |
| $x_{6}$  | $\exp\left(x_{5}\right)$               | $\dfrac{1}{e}$                   |
| $x_{7}$  | $-x_{6}$                               | $-\dfrac{1}{e}$                  |
| $x_{8}$  | $x_{1} + x_{7}$                        | $\dfrac{\pi}{16} - \dfrac{1}{e}$ |

Of course, the computer holds floating point values.  The value of $f\left(\dfrac{\pi}{16}\right)$ is $-0.17152990032208026$.  We can check this with our function.

### Elementary Functions

sine
cosine
tangent
logarithmic
exponential
addition
subtraction
multiplication
division
root

## How to Use

### How to interact?

### How to import?

### How to instantiate AD



## Software Organization

#### Discuss how you plan on organizing your software package.

####  What will the directory structure look like?
####  What modules do you plan on including? What is their basic functionality?
####  Where will your test suite live? Will you use TravisCI? Coveralls?
####  How will you distribute your package (e.g. PyPI)?

## Implementation
### Discuss how you plan on implementing the forward mode of automatic differentiation.

#### What are the core data structures?
#### What classes will you implement?
#### What method and name attributes will your classes have?
#### What external dependencies will you rely on?
#### How will you deal with elementary functions like sin and exp?