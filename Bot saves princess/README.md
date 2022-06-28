<h1 align="center"> Bot saves princess </h1>

<strong>Description</strong>

<p>Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move one step at a time in any of the four directions. Can you rescue the princess? </p>

<strong>Input format</strong>

<p>The first line contains an odd integer N (3 &lt;= N &lt; 100) denoting the size of the grid. This is followed by an NxN grid.  Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.</p>

<p>Grid is indexed using <a href="https://www.hackerrank.com/scoring/board-convention">Matrix Convention</a></p>

<strong>Output format</strong>

<p>Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.</p>

<strong>Sample input</strong>

## <pre><code>3

-m-
p--
</code></pre>

<strong>Sample output</strong>

<pre><code>DOWN
LEFT
</code></pre>

<strong>Task</strong>

<p>Complete the function <i>displayPathtoPrincess</i> which takes in two parameters - the integer N and the character array grid. The grid will be formatted exactly as you see it in the input, so for the sample input the princess is at grid[2][0]. The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess. The goal is to reach the princess in as few moves as possible.</p>

<p>The above sample input is just to help you understand the format. The princess ('p') can be in any one of the four corners.</p>

<p><strong>Scoring</strong> <br>
Your score is calculated as follows : (NxN - number of moves made to rescue the princess)/10, where N is the size of the grid (3x3 in the sample testcase). </p></div></div></div>
    </div>

</div>
