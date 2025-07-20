import numpy as np 
import matplotlib.pyplot as plt 


# Constants:
INITIAL_ADS = 10            # initial number of ads
INITIAL_VIEWS = 100_000     # initial number of page views
VIEWS_LOST = 5_000          # views lost per extra ad
REV_PER_IMPRESSION = 0.001  # revenue per ad impression 

def rev(x: int) -> int:
    """ returns initial revenue given X number of ads
        args x = Number of ads    
      """
    return ((INITIAL_ADS + x) * (INITIAL_VIEWS - VIEWS_LOST * x) * 
            REV_PER_IMPRESSION)

print("--- Website Ad Revenue Optimization ---\n")
print(f"Starting Ads: {INITIAL_ADS}")
print(f"Page Views: {INITIAL_VIEWS:,}  |  Loss per Ad: {VIEWS_LOST:,}")
print(f"Revenue per Impression: ${REV_PER_IMPRESSION:.3f}\n") 

# Quadratic: rev(x) = A*x^2 + B*x + C: 

A  =  -VIEWS_LOST * REV_PER_IMPRESSION 
B = (INITIAL_VIEWS - INITIAL_ADS * VIEWS_LOST) + REV_PER_IMPRESSION 
C = INITIAL_ADS * INITIAL_VIEWS * REV_PER_IMPRESSION
print(f"Revenue = {A:.6f}·x² + {B:.2f}·x + {C:.2f}")


# Calculate optimal x with the vertex equation:

x_opt = -B / (2 * A)
print(f"\nTheoretical optimal x: {x_opt:.2f}") 

# Search nearby integers for feasibility:
xs = np.arange(max(-INITIAL_ADS, int(x_opt) - 5), int(x_opt) + 6)
mask = (INITIAL_ADS + xs >= 0) & (INITIAL_VIEWS - VIEWS_LOST * xs >= 0)
xs = xs[mask]

if xs.size:
    re_vals = rev(xs)
    idx = np.argmax(re_vals)
    x_best = xs[idx]
    revenue_best = re_vals[idx]
else:
    x_best, revenue_best = 0, C

ads_final = INITIAL_ADS + x_best
views_final = INITIAL_VIEWS - VIEWS_LOST * x_best

print("\nOptimized Results:")
print(f"  Additional Ads: {x_best}")
print(f"  Total Ads/Page: {ads_final}")
print(f"  Page Views: {views_final:,}")
print(f"  Max Revenue: ${revenue_best:,.2f}")

# Plot:
xp = np.linspace(min(-INITIAL_ADS, x_best - 15), x_best + 25, 200)
plt.plot(xp, rev(xp), color='skyblue', linewidth=2)
plt.plot(x_best, revenue_best, 'ro', 
         label=f"Optimal (x=+{x_best} ads), Revenue=${revenue_best:,.2f}")
plt.plot(0, C, 'go',
         label=(f"Initial (x=0), Revenue=$"
                f"{INITIAL_VIEWS * REV_PER_IMPRESSION * INITIAL_ADS:,.2f}"))
plt.axvline(x_best, color='gray', ls='--')
plt.title('Ad Revenue vs Additional Ads', fontsize=16)
plt.xlabel('Additional Ads (x)', fontsize=14)
plt.ylabel('Daily Revenue ($)', fontsize=14)
plt.grid()
legend = plt.legend(framealpha=1)    
plt.tight_layout()
plt.show() 



