#### Defining a Revenue Calculation Function
Now we define a small function that computes estimated daily ad revenue based on a change in the number of ads displayed (x). The formula multiplies the updated number of advertisements by the adjusted page views, then scales by revenue per impression.

```
python

def rev(x):
    """ Calculate revenue."""
    return ((INITIAL_ADS + x) * (INITIAL_VIEWS - VIEWS_LOST * x) * 
            REV_PER_IMPRESSION)
```

The function returns either a single revenue value or, if x is an array, a vector of revenues. The latter is useful for plotting how performance shifts as more ads are added or removed.

#### Expressing the Revenue Function as a Quadratic Equation
The next snippet expresses the revenue function as a quadratic equation for the number of additional ads (x).

```
python

A = -VIEWS_LOST * REV_PER_IMPRESSION
B = (INITIAL_VIEWS - INITIAL_ADS * VIEWS_LOST) * REV_PER_IMPRESSION
C = INITIAL_ADS * INITIAL_VIEWS * REV_PER_IMPRESSION
print(f"Revenue = {A:.6f}·x² + {B:.2f}·x + {C:.2f}")

```
Each coefficient reflects a different interaction between ads and page views:

- A represents the second-degree term's coefficient and captures how aggressively revenue declines as more ads are added. It's negative, so the parabola opens downward.
- B is the linear term's coefficient, combining the base viewership with the loss caused by ads.
- C is the constant term — the revenue when no additional ads are added. 

#### Calculating the Vertex
Next, we calculate the vertex of a downward-opening quadratic revenue curve, which represents the optimal number of additional ads (x_opt) to maximize revenue. The formula -B / (2 * A) pinpoints the peak of the parabola, and the result is printed with two decimal places to show the theoretical (possibly fractional) optimum.



