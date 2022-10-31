Bubu the Minion

Question Name: Bubu the minion

Problem Statement

Bubu, the minion has been invited to a birthday party. Bubu has been given two plates. The first plate has N Roties in it and the second plate has M Roti. The Roties have been aligned in these plates one on top of the other in form of a stack as shown below. The tastiness of the ith Roti in the first plate is Ai and the tastiness of the ith Roti in the second plate is Bi.

 

Bubu has a maximum capacity of K. This means that the sum of the tastiness of all the Roties that Bubu eats must be less than or equal to K. Bubu can’t take Rotis from between the stacks i.e for eating Roti i from a plate, Bubu must eat all the Rotis 1<=j<=i-1 from that plate. Given the arrays A and B describing the tastiness of the Rotis in both the plates, print the maximum number of roties Bubu can eat such that the sum of the tastiness of all the Roties that Bubu eats in total from both the plates is atmost K.

Input Format

First line contains three space separated integers denoting K, N, and M.
Output Format

Print the maximum number of roties Bubu can eat such that the sum of the tastiness of all the Roties that Bubu eats in total from both the plates is atmost K.
Constraints

1<=K<=10^9
1<=N,M<=2*10^5
1<=Ai, Bi<=10^9
Sample Input 1

240 3 4

60 90 120

80 150 80 150

Output 1

3

Explanation of Sample 1

Bubu can eat first and second roti from first plate, and first roti from second plate.

Total sum of tastiness = 60+90+80 = 230 which is less than K( = 240).

 

Things to Note for the Candidate :

 

You can use your own IDE like Visual Studio Code, Eclipse, or any other IDE that you are comfortable with to build your solution code.
 

The IDE provided on the platform is purely for submission. Avoid using the IDE for coding out the solution.
 

Test against any custom input in your own IDE. In the IDE provided on the platform, you cannot pass custom test cases and see the output. 
 

Use standard input and standard output in your program for the IDE to run the test cases smoothly against your code. We are giving a sample problem statement along with a solution that will pass the test cases in the IDE. - Sample Problem Statement  (Right Click and Open in New Tab to view.)