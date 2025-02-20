# CMPS 2200  Recitation 02

**Name (Team Member 1):** Sofia Bareiro   
**Name (Team Member 2):** Mauricio Uribe

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**The simple_work_calc function derives the value of W(n) by recursively computing the recurrence W(n) = aW(n/b)+n with base case W(1)=1. The test_simple_work fuction will verify that simple_work_calc produces the expected outputs by running test cases. After correcting the test cases, they became: 
assert simple_work_calc(8, 2, 2) == 10  
assert simple_work_calc(8, 3, 2) == 10  
assert simple_work_calc(9, 2, 3) == 12**

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**The asymptotic behavior of W(n) depends on the relationship between c and log(b)a. If c<log(b)a, the recursive term dominates, leading to W(n)=O(n^(logb^a). If c>log(b)a, the work function dominates, giving W(n)=O(n^c). If c=log(b)a, both terms contribute equally, resulting in W(n)=O(n^clogn). To confirm these results, test_compare_work was modified to compare empirical values for different work functions across multiple values of n.**

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**The span S(n) represents the longest chain of dependent recursive calls in the algorithm, modeling the parallel execution time with a processors. The recurrence follows S(n)=S(n/b)+f(n). Implementing span_calc allows us to empirically compute the span, while test_compare_span verifies its correctness across different cases. Based on problem 4, if f(n)=1, then S(n)=O(logn);if if(n)=logn, then S(n)=O(log^2n);and if f(n)=n, then S(n)=O(n). These results were confirmed by comparing empirical values to theoretical expectations.**
