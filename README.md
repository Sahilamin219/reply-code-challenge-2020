# reply-code-challenge-2020

## MEGLIO UN UOVO OGGI CHE UNA GALLINA DOMANI
## It is better to relax constraints and make assumptions that allow for a solution _now_ rather than finding the optimal solution in 1 hour.
https://challenges.reply.com/tamtamy/home.action


Workspace:
* telegram
* ide (if vscode, take a couple minutes to install all needed linters/formatters/etc, set up python interpreter, etc)
* browser
* anything else?

## Enrivonment
1. `$ conda create -n reply python=3.6 numpy`
2. `$ conda activate reply`

## Attack plan
1. Fast read of the problem statement (~30 min) to identify:
    * General setting (no more than 5 min)
    * I/O format (__check samples!__) (~15 min)
    * scoring (__check samples!__) (~10 min)
2. Discussion on setting and I/O (~20 min)
3. Discussion of other issues such as asking the organizers about unclear statements (~20 min)
4. First coding iteration (~1.5 h):
    1. One person writes I/O parsers/writers (~30 minutes)
    1. Two people find the quickest solution to implement (~30 minutes)
    2. Discussion, task assignment, coding (1 hour)
5. Second coding iteration (~1 h)
6. Ideally: refinement. More likely: still at point 4.2

## Notes
1. Docstrings are not needed, but commenting (ideally before writing code) is much appreciated
2. Don't wait long before asking eachother questions if something is unclear, not well defined, etc
3. There's always gonna be a much better solution we would like to implement, but let's focus on actually sending a solution first
4. Brute force solutions are indeed solutions
5. Random feasible solutions are indeed solutions
6. Heuristics can be a useful tool to improve on 5. and 6.
7. Genetic algorithms, graph search, linear programming are typically what first comes to mind, but they're not easy to formalize and implement in 4 hours