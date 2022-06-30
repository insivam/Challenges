<h1 align="center"> BotClean </h1>

<strong>Description</strong>

<p>The goal of Artificial Intelligence is to create a rational agent (<a href="https://www.hackerrank.com/external_redirect?to=http://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597#reader_B004O4BZ16" target="_blank">Artificial Intelligence 1.1.4</a>). An agent gets input from the environment through sensors and acts on the environment with actuators. In this challenge, you will program a simple bot to perform the correct actions based on environmental input. </p>

<strong>Task</strong>

<p>Meet the bot <strong>MarkZoid</strong>.  It's a cleaning bot whose sensor is a head mounted camera
and whose actuators are the wheels beneath it. It's used to clean the floor.</p>

<p>The bot here is positioned at the top left corner of a 5*5 grid. Your task is to move
the bot to clean all the dirty cells.</p>

<strong>Input Format</strong>

<p>The first line contains two space separated integers which indicate the current position of the bot. <br>
The board is indexed using <a href="https://www.hackerrank.com/scoring/board-convention">Matrix Convention</a> <br>
5 lines follow representing the grid. Each cell in the grid is represented by any 
of the following 3 characters: 'b' (ascii value 98) indicates the bot's current position, 'd' (ascii value 100) indicates a dirty cell and '-' (ascii value 45) indicates a clean cell in the grid. </p>

<p><strong>Note</strong> If the bot is on a dirty cell, the cell will still have 'd' on it. </p>

<p><strong>Output Format</strong></p>

<p>The output is the action that is taken by the bot in the current step, and it can be either one of the movements in 4 directions or cleaning up the cell in which it is currently located. The valid output strings are
LEFT, RIGHT, UP and DOWN or CLEAN. If the bot ever reaches a dirty cell, output CLEAN to clean the dirty cell. Repeat 
this process until all the cells on the grid are cleaned.</p>

<strong>Sample Input #00</strong>

<pre><code>0 0
b---d
-d--d
--dd-
--d--
----d
</code></pre>

<strong>Sample Output #00</strong>

<pre><code>RIGHT
</code></pre>

<p><strong>Resultant state</strong></p>

<pre><code>-b--d
-d--d
--dd-
--d--
----d
</code></pre>

<p><strong>Sample Input #01</strong></p>

<pre><code>0 1
-b--d
-d--d
--dd-
--d--
----d
</code></pre>

<p><strong>Sample Output #01</strong></p>

<pre><code>DOWN
</code></pre>

<p><strong>Resultant state</strong></p>

<pre><code>----d
-d--d
--dd-
--d--
----d
</code></pre>

<strong>Task</strong>

<p>Complete the function <i>next_move</i> that takes in 3 parameters <em>posr</em>, <em>posc</em> being the co-ordinates of the bot's current position and <em>board</em> which indicates the board state to print the bot's next move. </p>

<p>The codechecker will keep calling the function <i>next_move</i> till the game is over or you make an invalid move.</p>

<strong>Scoring</strong>

<p>Your score is (200 - number of moves the bot makes)/40. CLEAN is considered a move as well.</p>

<p>Once you submit, your bot will be played on four grids with three of the grid configurations unknown to you. The final score will be the sum of the scores obtained in each of the four grids.</p>

<p align="right"><strong>Final Score: 17.82</strong></p>

