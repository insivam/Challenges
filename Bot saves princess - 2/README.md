<h1 align="center"> Bot saves princess - 2 </h1>

<strong>Description</strong>

<p>In this version of "Bot saves princess", Princess Peach and bot's position are randomly set. Can you save the princess?</p>

<strong>Task</strong>

<p>Complete the function <i>nextMove</i> which takes in 4 parameters - an integer <i>N</i>, integers <i>r</i> and <i>c</i> indicating the row &amp; column position of the bot and the character array <i>grid</i> - and outputs the <strong>next</strong> move the bot makes to rescue the princess.</p>

<strong>Input Format</strong>

<p>The first line of the input is N (&lt;100), the size of the board (NxN). The second line of the input contains two space separated integers, which is the position of the bot.   </p>

<p>Grid is indexed using <a href="https://www.hackerrank.com/scoring/board-convention">Matrix Convention</a></p>

<p>The position of the princess is indicated by the character 'p' and the position of the bot is indicated by the character 'm' and each cell is denoted by '-' (ascii value: 45). </p>

<strong>Output Format</strong>

<p>Output only the <strong>next</strong> move you take to rescue the princess. Valid moves are LEFT, RIGHT, UP or DOWN</p>

<strong>Sample Input</strong>

<pre><code>5
2 3
-----
-----
p--m-
-----
-----
</code></pre>

<strong>Sample Output</strong>

<pre><code>LEFT
</code></pre>

<p><strong>Resultant State</strong></p>

<pre><code>-----
-----
p-m--
-----
-----
</code></pre>

<strong>Explanation</strong>

<p>As you can see, bot is one step closer to the princess.  </p>

<p><strong>Scoring</strong> <br>
Your score for every testcase would be (NxN minus number of moves made to rescue the princess)/10 where N is the size of the grid (5x5 in the sample testcase). Maximum score is 17.5 </p></div></div></div>
</div>
