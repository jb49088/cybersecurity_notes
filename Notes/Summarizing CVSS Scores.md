
# Summarizing CVSS Scores

The CVSS vector provides good detailed information on the nature of the risk posed by a vulnerability, but the complexity of the vector makes it difficult to use in prioritization exercises. For this reason, analysts can calculate the CVSS base score, which is a single number representing the overall risk posed by the vulnerability. Arriving at the base score requires first calculating some other CVSS component scores.

## Calculating the Impact Sub-Score (ISS)

The first calculation analysts perform is computing the impact sub-score (ISS). This metric summarizes the three impact metrics using the formula:

$$ ISS =1-[(1- Confidentiality) \times(1- Integrity) \times(1- Availability )] $$

Plugging in the values for our SSL vulnerability shown in [[Image 2.51.png|Image 2.51]], we obtain:

$$ \begin{array}{c}\text { ISS }=1-[(1-0.56) \times(1-0.000) \times(1-0.00)] \\ \text { ISS }=1-[0.44 \times 1.00 \times 1.00] \\ \text { ISS }=1-0.44 \\ \text { ISS }=0.56\end{array} $$

## Calculating the Impact Score

To obtain the impact score from the impact sub-score, we must take the value of the scope metric into account. If the scope metric is Unchanged, as it is in our example, we multiply the ISS by 6.42:

$$ \begin{array}{c}\text { Impact }=6.42 \times \text { ISS } \\ \text { Impact }=6.42 \times 0.56 \\ \text { Impact }=3.60\end{array} $$

If the scope metric is Changed, we use a more complex formula:

$$ Impact = 7.52 \times(ISS -0.029)-3.25 \times(\text { ISS }-0.02)^{15} $$

## Calculating the Exploitability Score

Analysts may calculate the exploitability score for a vulnerability using this formula:

$$ \begin{aligned} \text { Exploitability }= & 8.22 \times \text { Attack Vector } \times \text { AttackComplexity } \\ & \times \text { PrivilegesRequired } \times \text { UserInteraction }\end{aligned} $$ 

Plugging in values for our SSL vulnerability, we get

$$ \begin{array}{c}\text { Exploitability }=8.22 \times 0.85 \times 0.77 \times 0.85 \times 0.85 \\ \text { Exploitability }=3.89\end{array} $$

## Calculating the Base Score

With all of this information at hand, we can now determine the CVSS base score using the following rules: 

- If the impact is 0, the base score is 0.
- If the scope metric is Unchanged, calculate the base score by adding together the impact and exploitability scores.
- If the scope metric is Changed, calculate the base score by adding together the impact and exploitability scores and multiplying the result by 1.08.
- The highest possible base score is 10. If the calculated value is greater than 10, set the base score to 10.

In our example, the impact score is 3.60 and the exploitability score rounds to 3.9. Adding these together, we get a base score of 7.5, which is the same value found in [[Image 2.51.png|Image 2.51]].

> [!info] Note
> Now that you understand the math behind CVSS scores, the good news is that you don't need to perform these calculations by hand. NIST offers a CVSS calculator at www.first.org/cvss/calculator/3.1, where you can easily compute the CVSS base score for a vulnerability.

## Categorizing CVSS Base Scores

Many vulnerability scanning systems further summarize CVSS results by using risk categories rather than numeric risk ratings. These are usually based on the CVSS Qualitative Severity Rating Scale, shown in [[Table 1.20]].

![[Table 1.20|no-link no-title clean]]

Continuing with the SSL vulnerability example from [[Image 2.51.png|Image 2.51]], we calculated the CVSS score for this vulnerability as 7.5. This places it into the High risk category, as shown in the header of [[Image 2.51.png|Image 2.51]]. 

> [!info] Note
> Be sure you are familiar with the CVSS severity rating scale for the exam. These scores are a common topic for exam questions!



