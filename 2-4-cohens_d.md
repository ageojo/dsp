[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)



\* Code: **`2-4-cohens_d.py`**
s

\* [Effect sizes](http://staff.bath.ac.uk/pssiw/stats2/page2/page14/page14.html)


#### **Q1:**  Using the variable `totalwgt_lb`, investigate whether first babies are lighter or heavier than others. 

**ANSWER:** First babies are on average lighter than others. The mean weight for firstborns is 7.201 lbs compared to 7.326lbs for others.
 

#### **Q2:**  Compute **Cohen’s d** to quantify the difference between the groups. 


*Cohen's d* is the difference in group means divided by the weighted average of their standard deviations, known as pooled standard deviation.
 difference in the two groups' means divided by the average of their standard deviations (pooled variation, `s` below)

** Write equation in LaTex**
```markdown

d = (xmean_a - xmean_b) / s

s
s = sqrt( 
    sum(g1N\*g1var + g2N\*g2var) \/ (g1N + g2N) 
    )

```

*Pooled standard deviation* is defined as the square root of the pooled variance, where pooled variance equals the sum of weighted group variance (group1_N \* g1var + group2_N \* g2var) divided by the total number of observations (group1_N + group2_N)

The effect size for the difference in weight between firstborns and others as computed using Cohen's indicates


**ANSWER:** Cohen's d for birth weight as a function of birth order (firstborns vs. others):  -0.0887


#### **Q3:** How does it compare to the difference in pregnancy length?      

**ANSWER:** Cohen's d for pregnancy length as a function of birth order (firstborns vs. others):  0.029


### **Summary:**

Cohen's d is a standardized mean effect, expressing the mean difference between two groups in standard deviation units.

As a rule of thumb, Cohen's d of 0.2 is considered a small effect size, 0.5 as a medium effect size, and 0.8 or higher as a large effect size.

Whether Cohen's d is positive or negative depends on the order in which groups are labeled. 

For both Q2 and Q3, Cohen's d was computed with firstborns labeled as group1 and others as group2.

The value of Cohen's d was negative for birth weight reflecting the fact that the mean birth weight of firstborns is lower than that of others but positive for pregnancy length, indicating that the mean duration of pregnancy is greater for firstborns than others. 

As the absolute value of Cohen's d is very small in both cases, the difference in average birth weight or pregnancy length for firstborns compared to others is trivial, even if statistically significant.
 




