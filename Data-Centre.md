# Statistics Data Centre Documentation

## Overview

The data centre shows all the data that is supported by the search platform. It provides detailed mapping for player and team statistics, including definitions, categorical classifications, and data availability ranges.

## Supported Sports (Categories)

The Data Centre currently supports the following sports:

- Men's Football (MFB)
- Men's Basketball (MBB)
- Women's Basketball (WBB)
- Men’s Ice Hockey (MIH)

## Men's Football (MFB) Scope

### Sub-Category: Players

The player-level data for Men's Football is categorized by field units and specific play types.

| Category | Supported Sub-categories |
| --- | --- |
| Offense | Passes, Receiving, Rushing, PATs, Total Offense, Plays, Scoring, Red Zone |
| Defense | Fumble Return, Fumbles, Interception Return, Blocks, PBU, Sacks, Tackles, Tackles for Loss, Turnovers, Safety |
| Special Teams | Field Goal, Kickoff, Kickoff Returns, Punt return, Punts, PATs |

## Data Availability & Historical Scope

The Data Centre tracks historical performance across different eras. The availability is categorized into "Standard" ranges and "Advanced" ranges (highlighted in the interface).

### Global Availability Matrix

| Sport | Standard Data Range | Advanced Metric Range |
| --- | --- | --- |
| Men's Football | 2014 – Present | 2021 – Present |
| Men's Basketball | 2009 – Present | 2011 – Present (Select Metrics) |
| Women's Basketball | 2009 – Present | N/A |

### Specific Availability Exceptions

#### Men's Football (2021 – Present Only)

The following metrics were introduced or granularly tracked starting in the 2021 season:

- Defense: Takeaways, Field Goal Blocked by, PAT kick blocked by, Caused turnovers.
- Offense (Teams): Pass Attempts, Times Sacked, Red Zone (detailed scoring/turnover types), Points off Turnovers, 1st/2nd Down Conversions, Time Leading/Tied.
- Special Teams: Net Kickoff Yards, Kickoffs Returned, Net/Average Punt Yards, Blocked Punts/Field Goals.
- Play Direction: Rush Left, Rush Middle, Rush Right.

#### Men's Basketball (2011 – Present Exceptions)

While most basketball data begins in 2009, certain advanced efficiency metrics for teams are available from 2011:

- Points From Turnovers Percentage
- Transition Offense Efficiency

### Sub-Category: Teams

Team-level data includes aggregate performance and game-state metrics.

| Category | Supported Sub-categories |
| --- | --- |
| Offense | Passes, Receiving, Rushing, First Down, Third Down, Fourth Down, Red Zone, Points, Scoring, Total Offense, 2nd Down, Biggest Lead, Biggest Scoring Run, Time of Possession, Time Leading, Plays, Turnovers |
| Defense | Fumbles, Fumble Return, Tackles, Interception Return, PBU, Sacks, Blocks, Tackles for Loss, Safety, Times Scores Level |
| Special Teams | Kickoff, Field Goal, PATs, Punts, Punt return |
| Penalties | Team Penalties, Penalty Yards |
| Results | Wins in Overtime |

## Men's Basketball (MBB) Scope

### Sub-Category: Players

Basketball metrics are focused on efficiency and play-by-play impact.

| Category | Key Metrics Tracked |
| --- | --- |
| Offense | Field Goals (Made/Att/%), Assists, Points (Paint, Fast Break, 2nd Chance), Free Throws, Three Pointers, Usage %, Efficiency Game Score |
| Defense | Blocks, Defensive Rebounds, Steals, Defensive Rebound % |
| Fouls | Personal Fouls, Technical Fouls, Offensive Fouls, Fouled Out, Fouls On |
| General | Minutes, Plus/Minus, Double/Triple/Quadruple Doubles |

Data Availability: 2009–Present

### Sub-Category: Teams

Aggregate team performance and advanced efficiency ratings.

| Category | Key Metrics Tracked |
| --- | --- |
| Offense | Points, Assists, Bench Points, Biggest Lead, Field Goals, Free Throws, Offensive Rating, Paint/Fast Break/2nd Chance Points, Possessions, Transition Offense |
| Defense | Steals, Blocks, Defensive Rebounds, Points Against, Defensive Rating, Opponent Possessions, Transition Defense |
| Fouls | Team Fouls, Technical Fouls (Bench/Coach), Personal Fouls, Fouled Out |
| General | Minutes, Total Rebounds, Leading Time, Time Level |

## Women's Basketball (WBB) Scope

### Sub-Category: Players

The scope for Women's Basketball Players mirrors the Men's Basketball scope, focusing on individual efficiency and contribution.

| Category | Metrics Scope |
| --- | --- |
| Offense | Scoring, Shooting Percentages (2PT, 3PT, FT, EFG, True Shooting), Playmaking (Assists, Turnovers), Usage |
| Defense | Rim Protection (Blocks), Ball Hawking (Steals), Rebounding |
| Fouls | Discipline and Fouls Drawn |
| General | Court Time and Advanced Impact (Plus/Minus, Box Score Achievements) |

### Sub-Category: Teams

Comprehensive team metrics including deadball situations and non-player-specific attributes.

| Category | Metrics Scope |
| --- | --- |
| Offense | Scoring, Shooting, Ball Movement, Possession-based Efficiency, Second Chance Opportunities, Transition Play |
| Defense | Points Allowed, Rebounding (including Deadball and Team Rebounds), Defensive Efficiency |
| Fouls | Cumulative Team and Bench Discipline |
| General | Game Flow (Lead Changes, Time Level) |

## MBB Player Statistics

| Statistic Name | Description | Aliases |
| --- | --- | --- |
| Field Goals Attempted | The total number of field goal shots attempted by the player or team. | Field goals attempted, FGA |
| Assists | Number of passes that directly lead to a teammate scoring a basket. | ast |
| Assists to Turnover Ratio | Ratio of assists to turnovers, measuring ball handling efficiency. | Assist to turnover ratio,, Asst TO ratio |
| Blocks | Number of opponent shots blocked by the player. | blk, Blocks |
| Shots Blocked | Number of player's shots that were blocked by opponents. | blocked shots, blocked |
| Efficiency Game Score | Advanced efficiency metric that weights various statistical categories. | game score, efficiency game score |
| Fast Break Points Attempted | Number of fast break scoring opportunities attempted. | fast break points attempted, fast brk pts att |
| Fast Break Points Made | Points scored on fast break opportunities. | fast break points, fast brk pts |
| Fast Break Points Percentage | Shooting percentage on fast break attempts. | Fast break field goal percentage, fast brk, FG % |
| Effective Field Goals Percentage | Field goal percentage adjusted for the added value of three-point shots. | eff fg% |
| Field Goals Made | Total number of successful field goals (excluding free throws). | Field goals made, FGM |
| Field Goals Percentage | Shooting percentage calculated from field goals made divided by attempted. | Field goal percent, field goal %, FG % |
| Fouled Out | Number of games where player was disqualified due to foul limit. | fouled out |
| Offensive Fouls | Fouls committed by the player while their team has possession. | Offensive foul, Off foul |
| Fouls on | Number of fouls committed against the player by opponents. | fouls on |
| Personal Fouls | Total number of personal fouls committed by the player. | personal fouls, pers foul |
| Technical Fouls | Fouls assessed for unsportsmanlike conduct or rule violations. | technical fouls, tech fouls, techs |
| Free Throws Attempted | Total number of free throw attempts. | free throws attempted, free throws att, FTA |
| Free Throws Made | Total number of successful free throws. | free throws made, free throws md, FTM |
| Free Throw Percentage | Shooting percentage calculated from free throws made divided by attempted. | Free throw percentage, Free throw perc, FT % |
| Minus | Points scored by opponents while player was on court. | points against |
| Minutes | Total playing time in minutes. | min, minutes played |
| Offensive Rating | Points produced per 100 possessions while player is on court. | Offensive rating, off rate |
| Plus | Points scored by player's team while they were on court. | points for |
| Plus Minus | Difference between team's points and opponent's points while player is on court. | +/- |
| Points | Total points scored by the player. | points scored, pts, points |
| Fast Break Points | Points scored during fast break situations. | fast break points, FB pts |
| Paint Points | Points scored from shots taken inside the paint area. | paint pts, pts in paint, paint points |
| Paint Points Attempted | Number of scoring attempts from inside the paint area. | points in paint attempts, points in pnt att, paint pts att |
| Paint Points Made | Successful scoring attempts from inside the paint area. | points in paint made, points in pnt md, paint pts md |
| Paint Points Percentage | Shooting percentage on attempts from inside the paint. | points in paint percentage, points in paint % |
| Second Chance Points | Points scored following offensive rebounds. | second chance points, 2nd chnc pts |
| Defensive Rebounds | Rebounds collected after opponent's missed shots. | def rebounds, defensive reb, def reb, def rb, defrb |
| Defensive Rebound Percentage | Percentage of available defensive rebounds collected by the player. | def reb %, defrb% |
| Offensive Rebounds | Rebounds collected after own team's missed shots. | offensive rebounds, off reb, off rb, offrb |
| Offensive Rebounds Percentage | Percentage of available offensive rebounds collected by the player. | off reb % |
| Rebounds | Total rebounds (offensive + defensive) collected by the player. | total rebounds, rebounds, tot reb, rebounds total, rbds |
| Second Chance Points Attempted | Scoring attempts following offensive rebounds. | second chance points attempted, 2nd chance pts att |
| Second Chance Points Made | Successful scoring attempts following offensive rebounds. | second chance points made, 2nd chance pts made, 2nd chance pts md |
| Second Chance Points Percentage | Shooting percentage on second chance opportunities. | second chance points percentage, 2nd chance pts % |
| Steals | Number of times player intercepted opponent's pass or dribble. | stl, steals |
| Three Pointers Attempted | Number of shots attempted from beyond the three-point line. | Three point FG att, Three point att, 3 pt FG att, 3 pt att |
| Three Pointers Made | Number of successful shots from beyond the three-point line. | Three point FG made, Three point made, 3 pt FG md, 3 pt md |
| Three Point Percentage | Shooting percentage on three-point attempts. | 3pt %, Three point percentage, Three point %, 3 pt %, 3 pt FG % |
| True Shooting Attempts | Adjusted shooting attempts accounting for free throws and three-pointers. | true shot att |
| True Shooting Percentage | Comprehensive shooting efficiency including free throws and three-pointers. | ts% |
| Turnovers | Number of times player lost possession through error or violation. | to, turnovers |
| Turnover Percentage | Percentage of possessions that end in a turnover by the player. | turnover % |
| Two Pointers Attempted | Number of field goal attempts from inside the three-point line. | two points attempted, two points att, two pt FG att, 2 pt att |
| Two Pointers Made | Number of successful field goals from inside the three-point line. | two pointsmade, two points md, two pt FG md, 2 pt md, 2 pt made |
| Two Point Percentage | Shooting percentage on two-point attempts. | two point percent, 2 pt % |
| Usage Percentage | Percentage of team possessions used by the player while on court. | usage rate |
| Double double | Games with double digits in two statistical categories. | double double |
| Triple double | Games with double digits in three statistical categories. | triple double |
| Quadruple double | Games with double digits in four statistical categories. | quadruple double |

## MBB Teams Statistics

| Statistic Name | Description | Aliases |
| --- | --- | --- |
| Steals | The number of times a player or team legally took the ball away from an opponent, resulting in a change of possession. | steals, stl |
| Technical Fouls | The number of technical fouls called against the player or team due to unsportsmanlike conduct or other infractions. | technical fouls, tech fouls, techs |
| Blocks | Total number of opponent shots blocked by the team. | blks, blocks |
| Defensive Rebounds | Team rebounds collected after opponent missed shots. | def rebounds, defensive reb, def reb |
| Defensive Rebounds Deadball | Defensive rebounds awarded during dead ball situations. | defensive deadball rebounds, def DB reb |
| Team Defensive Rebounds | Defensive rebounds not credited to individual players. | team defense rebounds, team def reb |
| Points Per Possession | Average points allowed per defensive possession. | Defensive Points per Possession, Def pts per loss |
| Defensive Rating | Points allowed per 100 possessions by the team. | defensive rating, Def rate |
| Opponent Possessions | Total number of possessions by the opposing team. | oppo poss, opponent possessions |
| Transition Defence | Defensive efficiency in transition situations. | trans def, transition d, defense transition |
| Fouled Out | Number of team players disqualified due to foul limit. | fouled out |
| Offensive Fouls | Fouls committed by the team while in possession. | Offensive foul, Off foul |
| Fouls on | Total fouls committed against the team by opponents. | fouls on |
| Personal Fouls | Total personal fouls committed by all team players. | personal fouls, pers foul |
| Team Fouls | Team fouls accumulated in each period. | team foul |
| Total Fouls | Sum of all fouls committed by the team. | total foul |
| Bench Technical Fouls | Technical fouls assessed against team bench personnel. | bench fouls |
| Coach Technical Fouls | Technical fouls specifically assessed against the head coach. | Coach technical foul, coach tech foul |
| Minutes | Total playing time for the team in the game. | min, minutes played |
| Points | Total points scored by the team. | points scored, pts, points |
| Points Against | Total points scored against the team by opponents. | pts against, points against |
| Personal Rebounds | Rebounds credited to individual team players. | personal rebunds, per reb |
| Team Rebounds | Rebounds not credited to any specific player. | team reb, team rebounds |
| Rebounds | Total rebounds collected by the team. | total rebounds, rebounds, tot reb, rebounds total |
| Leading Time | Total time the team held the lead during the game. | times lead |
| Time Level | Number of times the score was tied during the game. | ties, times tied |
| Assists | Total team assists leading directly to made baskets. | ast, assists |
| Assists to Turnover Ratio | Ratio of team assists to team turnovers. | Assist to turnover ratio,, Asst TO ratio |
| Bench Points | Points scored by non-starting players. | bench pts, Bench Points |
| Biggest Lead | Largest point advantage held by the team during the game. | largest lead, biggest lead |
| Biggest Lead Score | Score when the team held its biggest lead. | largest lead score |
| Largest Run | Longest consecutive scoring streak by the team. | biggest run, scoring run |
| Largest Run Score | Score during the team's largest scoring run. | biggest run score |
| Shots Blocked | Number of team shots blocked by opponents. | blocked shots, blocked |
| Fast Break Points Attempted | Fast break scoring opportunities attempted by the team. | fast break points attempted, fast brk pts att |
| Fast Break Points Made | Points scored by the team on fast break opportunities. | fast break points, fast brk pts |
| Fast Break Points Percentage | Team's shooting percentage on fast break attempts. | Fast break field goal percentage, fast brk, FG % |
| Field Goals Attempted | Total field goal attempts by the team. | Field goals attempted, FGA |
| Field Goals Made | Total successful field goals by the team. | Field goals made, FGM |
| Field Goals Percentage | Team's field goal shooting percentage. | Field goal percent, field goal %, FG % |
| Free Throws Attempted | Total free throw attempts by the team. | free throws attempted, free throws att, FTA |
| Free Throws Made | Total successful free throws by the team. | free throws made, free throws md, FTM |
| Free Throw Percentage | Team's free throw shooting percentage. | Free throw percentage, Free throw perc, FT % |
| Lead Changes | Number of times the lead changed hands during the game. | lead changes, lead chg |
| Offensive Points Per Possession | Average points scored per offensive possession. | offensive points per possession, Off pts per poss |
| Offensive Rating | Points scored per 100 possessions by the team. | Offensive rating, off rate |
| Fast Break Points | Points scored by the team in fast break situations. | fast break points, FB pts |
| Points From Turnovers | Points scored off opponent turnovers. | points from turnover, pts from TO |
| Paint Points | Points scored by the team from inside the paint. | paint pts, pts in paint, paint points |
| Paint Points Attempted | Team scoring attempts from inside the paint area. | points in paint attempts, points in pnt att, paint pts att |
| Paint Points Made | Successful team scoring attempts from inside the paint. | points in paint made, points in pnt md, paint pts md |
| Paint Points Percentage | Team shooting percentage on paint attempts. | points in paint percentage, points in paint % |
| Second Chance Points | Points scored following team offensive rebounds. | second chance points, 2nd chnc pts |
| Possessions | Total number of offensive possessions by the team. | poss, possessions |
| Offensive Rebounds | Team rebounds collected after own missed shots. | offensive rebounds, off reb |
| Offensive Rebounds Deadball | Offensive rebounds awarded during dead ball situations. | offensive deadball rebounds, off DB reb |
| Team Offensive Rebounds | Offensive rebounds not credited to individual players. | team offense rebounds, team off reb |
| Second Chance Points Attempted | Team scoring attempts following offensive rebounds. | second chance points attempted, 2nd chance pts att |
| Second Chance Points Made | Successful team scoring attempts following offensive rebounds. | second chance points made, 2nd chance pts made, 2nd chance pts md |
| Second Chance Points Percentage | Team shooting percentage on second chance opportunities. | second change points percentage, 2nd chance pts % |
| Three Pointers Attempted | Total three-point attempts by the team. | Three point FG att, Three point att, 3 pt FG att, 3 pt att |
| Three Pointers Made | Total successful three-point shots by the team. | Three point FG made, Three point made, 3 pt FG md, 3 pt md |
| Three Point Percentage | Team's three-point shooting percentage. | 3pt %, Three point percentage, Three point %, 3 pt %, 3 pt FG % |
| Transition Offense | Offensive efficiency in transition situations. | trans off, offense transition |
| Turnovers | Total turnovers committed by the team. | to, turnovers |
| Team Turnovers | Turnovers not attributed to individual players. | team to, Team turnovers |
| Two Pointers Attempted | Total two-point field goal attempts by the team. | two points attempted, two points att, two pt FG att, 2 pt att |
| Two Pointers Made | Total successful two-point field goals by the team. | two pointsmade, two points md, two pt FG md, 2 pt md, 2 pt made |
| Two Point Percentage | Team's two-point shooting percentage. | two point percent, 2 pt % |

## MFB Player Statistics

| Statistic Name | Description | Aliases |
| --- | --- | --- |
| Longest Field Goal Made | The longest successful field goal attempt made by the player during the game, measured in yards. | longest fgm |
| Field Goals Attempted | The total number of field goal attempts made by the player during the game. | fga |
| Field Goals Blocked | The total number of field goal attempts that were blocked by the player during the game. | blocked fg |
| Field Goals Made | The total number of successful field goals made by the player during the game. | fgm |
| Fumble Return Touchdowns | The total number of touchdowns scored by the player as a result of returning a fumble recovery. | fumble return td |
| Fumble Return Yards | The total number of yards gained by the player when returning a fumble recovery. |  |
| Fumbles Forced | The total number of fumbles caused by the player during the game. | forced fumble(s) |
| Fumbles Lost | The total number of fumbles lost by the player during the game. | lost fumble |
| Fumbles Recovered | The total number of fumbles recovered by the player during the game. | fumble recoveries |
| Longest Interception Return | The longest distance, in yards, the player returned an interception during the game. | longest int return |
| Interception Return Yards | The total number of yards gained by the player when returning an interception. | ir yards |
| Interception Touchdowns | The total number of touchdowns scored by the player as a result of returning an interception. | ir td |
| Kickoffs Gross Yards | The total number of yards covered by all kickoffs made by the player during the game. | kickoff yards |
| Kickoffs Out of Bounds | The total number of kickoffs that went out of bounds during the game. | kickoff oob |
| Total Kickoffs | The total number of kickoffs made by the player during the game. | kcikoffs |
| Kickoffs Touchbacks | The total number of kickoffs that resulted in touchbacks during the game. | kickoff tb |
| Longest Kick Return | The longest distance, in yards, the player returned a kickoff during the game. | longest kr |
| Total Kick Returns | The total number of kickoffs returned by the player during the game. | kick returns |
| Kick Return Touchdowns | The total number of touchdowns scored by the player as a result of returning a kickoff. | kr td |
| Kick Return Yards | The total number of yards gained by the player when returning a kickoff. | kr yards, kr yds |
| Kicks Blocked By | The total number of kicks (field goals or extra points) blocked by the player during the game. | blocked kicks |
| Pass Breakups | The total number of passes defended by the player during the game, resulting in an incomplete pass. | pbu |
| Passing Attempts | The total number of times the player has attempted to throw a forward pass during the game. | pass att |
| Passing Completions | The total number of successful forward passes completed by the player during the game. | pass comp |
| Intercepted Passes | The total number of forward passes thrown by the player that were intercepted by the opposing team during the game. | defense interception, interceptions caught |
| Longest Pass Completion | The longest distance, in yards, of a completed forward pass thrown by the player during the game. | longest pass |
| Passing Sacks | The total number of times the player was sacked while attempting a forward pass during the game. | pass sacks |
| Passing Touchdowns | The total number of touchdowns scored by the player through completed forward passes during the game. | pass td, passing td |
| Passing Yards | The total number of yards gained by the player through completed forward passes during the game. | pass yards, pass yds, passing yds |
| Passing Yards Lost to Sacks | The total number of yards lost by the player due to sacks while attempting forward passes during the game. Default to this if the query is "Passing yards sacked" or "Passes yards sacked" | pass sack yards, passing sck yards, pass sack yds, passing sack yds |
| Pass Interceptions | The total number of times the player intercepted a forward pass thrown by the opposing team during the game. | interceptions thrown, pass had intercepted |
| Quarterback Hurries | The total number of times the player pressured the opposing quarterback, causing them to hurry their throw, during the game. | qbh |
| PAT Kicks Attempted | The total number of point-after-touchdown (PAT) kicks attempted by the player during the game. | pat kick att |
| PAT Kicks Made | The total number of successful point-after-touchdown (PAT) kicks made by the player during the game. |  |
| PAT Pass Attempts | The total number of point-after-touchdown (PAT) pass attempts made by the player during the game. | pat pass att |
| PAT Passes Completed | The total number of successful point-after-touchdown (PAT) passes completed by the player during the game. | pat pass made |
| PAT Rush Attempts | The total number of point-after-touchdown (PAT) rush attempts made by the player during the game. | pat rush att |
| PAT Rushes | The total number of successful point-after-touchdown (PAT) rushes made by the player during the game. | pat rush made |
| Punt Returns | The total number of punts returned by the player during the game. |  |
| Longest Punt Return | The longest distance, in yards, the player returned a punt during the game. | longest pr |
| Punt Return Touchdowns | The total number of touchdowns scored by the player as a result of returning a punt during the game. | pr td |
| Punt Return Yards | The total number of yards gained by the player when returning a punt during the game. | pr yards, pr yds |
| Punts | The total number of punts executed by the player during the game. |  |
| Punts Over 50 Yards | The total number of punts kicked by the player that traveled over 50 yards during the game. | punt >50, punt>50yds |
| Punts Blocked | The total number of punts that were blocked by the opposing team during the game. | blocked punts |
| Punts Fair Caught | The total number of punts that were caught by the receiving team without attempting to advance the ball (fair catch) during the game. | punts fc |
| Punts Inside 20 Yards | The total number of punts that were downed inside the opponent's 20-yard line during the game. | punts inside 20 |
| Longest Punt | The longest distance, in yards, the player punted the ball during the game. | punt long |
| Punts Touchbacks | The total number of punts that resulted in the ball being downed in the end zone, resulting in a touchback during the game. | punts tb |
| Punting Yards | The total number of yards covered by all punts executed by the player during the game. | punting yds, punt yards, punt yds |
| Receptions | The total number of passes caught by the player during the game. | catches, receiving catches |
| Longest Reception | The longest distance, in yards, the player caught a pass during the game. | longest catch, receiving long |
| Reception Touchdowns | Also called receiving touchdowns. The total number of touchdowns scored by the player through caught passes during the game.  Also called "Receiving Touchdowns" | touchdown receptions |
| Reception Yards | Yards gained by a receiver on a play in which they successfully catch a pass, including the distance the ball was thrown and any additional yardage gained after the catch. Also called "Receiving Yards" | receiving yards, receiving yds, rec yds |
| Rushing Attempts | The total number of times the player carried the ball during the game. | rush att, rushing att |
| Longest Rush | The longest distance, in yards, the player advanced the ball on a rushing attempt during the game. | longest carry |
| Rushing Touchdowns | The total number of touchdowns scored by the player through rushing attempts during the game. | rush td, rushing td |
| Rushing Yards Gained | The total number of yards gained by the player through rushing attempts during the game. | rushing gain, rush gain |
| Rushing Yards Lost | The total number of yards lost by the player due to negative rushing plays during the game. | rushing loss, rush loss |
| Net Rushing Yards | Should be returned by default if the search is "Rushing Yards". The total number of yards gained by the player through rushing attempts, adjusted for any yards lost due to negative rushing plays during the game. | rushing yards, rush yards, rush yds, rushing yds |
| Assisted Sacks | The total number of sacks in which the player participated, sharing the responsibility with one or more teammates during the game. | assist sacks |
| Total Sacks | The total number of times the player successfully tackled the opposing quarterback behind the line of scrimmage, resulting in a loss of yards during the game. | sacks, defense sacks |
| Unassisted Sacks | The total number of sacks in which the player was solely responsible for tackling the opposing quarterback behind the line of scrimmage during the game. | solo sacks |
| Sack Yards | The total number of yards lost by the opposing team due to sacks made by the player during the game. | defense sack yards, sack yds, defense sack yds |
| Assisted Tackles | The total number of tackles in which the player participated, sharing the responsibility with one or more teammates during the game. | assist tackles |
| Assisted Tackles for Loss | The total number of tackles for loss in which the player participated, sharing the responsibility with one or more teammates during the game. | assisted tfl, assist tfl |
| Solo Tackles for Loss | The total number of tackles for loss in which the player was solely responsible for stopping the opposing player behind the line of scrimmage during the game. | unassisted tfl, solo tfl |
| Total Tackles for Loss | The total number of tackles for loss made by the player during the game, including both solo and assisted tackles. | tfl, tackles for loss |
| Solo Tackles | The total number of tackles in which the player was solely responsible for stopping the opposing player during the game. |  |
| Total Tackles | The total number of tackles made by the player during the game, including both solo and assisted tackles. | tackles |
| Tackles Yards | The total number of yards lost by the opposing team due to tackles made by the player during the game. | tfl yards, tackle for loss yards, tfl yds, tackle for loss yds |
| Touchdowns Scored | The total number of touchdowns scored by the player during the game, including rushing, receiving, and defensive touchdowns. | scoring touchdowns |
| Passing Yards Per Attempt | The average number of yards gained per passing attempt by the player. | pass yards per att |
| Pass Completion Percentage | The percentage of pass attempts completed by the player. | pass comp percent |
| Average Rushing Yards | The average number of net yards gained per rushing attempt by the player. | avg yards per carry, avg yds per carry, avg yds per rush, avg yards per rush |
| Average Yards per Reception | The average number of yards gained per reception by the player. | avg receiving yds, avg rec yds, avg reception yds |
| Takeaways | The number of times the player recovered a fumble or intercepted a pass. |  |
| Field Goal Percentage | The percentage of field goal attempts successfully made by the player. | fgm percent |
| Kickoffs Returned | The number of kickoffs returned by the player. | kickoff ret |
| Average Punt Return Yards | The average number of yards gained per punt return by the player. | punt return avg, punt ret avg |
| Net Kickoff Yards | The total net yards gained on kickoffs by the special teams unit. | kickoff yds, kickoff yards |
| Average Punt Yards | The average number of yards per punt made by the player. | avg punt yds, avg punt yards |
| Total Offensive Yards | The total number of yards gained by the player on offense. | total offense yds, total off yds |
| All-Purpose Yards | The total yards gained by the player from rushing, receiving, and returns. | all purp yds, all purpose yds |
| Turnovers Committed | The number of times the player turned the ball over, via fumble or interception. | turnovers |
| Longest field goal attempt | The longest field goal attempted during the game, regardless of whether it was successful. |  |
| Field Goal Blocked by | The number of field goals blocked by the team or player. |  |
| Longest fumble return | The longest distance returned by the team after recovering a fumble. |  |
| Total fumble returns | The total number of fumble returns by the team. |  |
| average yards per fumble return | The average yards gained on fumble returns. |  |
| Avg yards per interception return | The average yards gained after intercepting a pass. |  |
| Average gross yards from kickoff | The average gross yardage gained per kickoff. |  |
| Kickoff gross yards | The total gross yardage gained from all kickoffs. |  |
| Kick-off return average | The average yards gained per kickoff return. |  |
| Total kickoff returns | The total number of kickoff returns attempted. |  |
| All kicks blocked by | The number of any type of kicks (FG, PAT, punt) blocked by the team. |  |
| Pass Efficiency | A composite metric measuring a quarterback's overall passing effectiveness. |  |
| Avg yards per pass completion | The average number of yards gained per completed pass. |  |
| Percentage of passes resulting in TD | The percentage of completed passes that resulted in a touchdown. |  |
| PAT attempt | The total number of point-after-touchdown (PAT) attempts. |  |
| PAT kick blocked | The number of PAT kicks that were blocked. |  |
| PAT kick blocked by | The number of PAT kicks blocked by the team. |  |
| PAT Fumble return | The number of fumble returns that occurred during PAT attempts. |  |
| PAT kick return | The number of PAT kick returns after a failed attempt. |  |
| PAT kick made | The total number of successful PAT kicks made. |  |
| PAT receptions | The number of receptions made during a 2-point PAT attempt. |  |
| PAT 2pt conversion | The number of 2-point conversion attempts following a touchdown. |  |
| PAT 2pt made | The number of successful 2-point PAT conversions. |  |
| All purpose net yards | Total yards gained by a player including rushing, receiving, and returns. |  |
| Total plays | Total number of offensive plays executed. |  |
| Total points | Total number of points scored by the team. |  |
| Punts blocked by | The number of punts blocked by the team. |  |
| Average punt yards (net) | The average net distance of all punts. |  |
| Net punt yards | The total net yardage of all punts. |  |
| Redzone attempts passing plays | The number of pass plays attempted in the red zone. |  |
| Rush left | The number of rushing plays attempted to the left side. |  |
| Rush middle | The number of rushing plays attempted up the middle. |  |
| Rush right | The number of rushing plays attempted to the right side. |  |
| Safety 2 pt | The number of safeties (2-point defensive scores) recorded. |  |
| Caused turnovers | The number of times a team forced the opponent to lose possession. |  |
| Average yards per play | The average number of yards gained per offensive play. |  |
| Defensive Extra Points | The total number of points scored by the defense on conversion returns (blocked kicks or turnovers during extra point or two-point attempts) | defensive extra points, defensive extra point, extra points by defense, defense extra points |
| Goal Efficiency Percentage | The percentage of goal-to-go possessions that result in a touchdown. | goal efficiency percentage, goal efficiency %, goal-to-go efficiency, goal conversion percentage |
| Goal Efficiency Touchdowns | The number of touchdowns scored in goal-to-go situations. | goal efficiency touchdowns, goal-to-go touchdowns, touchdowns in goal-to-go, goal efficiency tds |
| Kicks Blocked | The total number of opponent kicks (field goals, PATs, or punts) blocked by the player. | kicks blocked, blocked kicks, kick blocks, blocked field goals, blocked punts, blocked PATs |
| Minutes Played | The total number of minutes played in the game. | minutes played, minutes, time played |
| Pass Attempts to Left | Number of pass attempts thrown to the left side of the field. | pass attempts left, throws to left, passes to left side, pass attempts to left, passes thrown to left, pass attempted to left |
| Pass Attempts to Middle | Number of pass attempts thrown to the middle of the field. | pass attempts middle, throws to middle, passes over middle, pass attempts to middle, passes to middle |
| Pass Attempts to Right | Number of pass attempts thrown to the right side of the field. | pass attempts right, throws to right, passes to right side |
| Negative Passing Plays | Completed passes that result in a loss of yardage. | negative passing plays, passes for loss, completed passes for loss, pass plays for loss |
| Defensive PAT Fumble Returns | Defensive two-point conversions scored by returning a fumble during a point-after-touchdown attempt. | defensive PAT fumble return |
| Defensive PAT Interception Returns | Defensive two-point conversions scored by returning an interception during a point-after-touchdown attempt. | pat interception return, pat int return, defensive PAT interception return |
| Defensive Blocked PAT Returns | Defensive two-point conversions scored by returning a blocked point-after-touchdown kick. | kick return pat, blocked PAT return |
| PAT Kick Percentage | The percentage of successful point-after-touchdown kick attempts. | pat percentage, pat kick percentage, extra point percentage |
| Negative Receiving Plays | Receptions that result in a loss of yardage. | negative receiving plays, receptions for loss |
| Receiving Yards After Catch | Total yards gained by the receiver after making a catch. | yards after catch, yac, receiving yac, receiving yards after catch, receiving yards gained after catch |
| Average Rushing Yards | Average yards gained per rushing attempt. | rushing average, rush avg, avg rush yards, average rushing yards, rushing yards average, rushing average yards |
| Kickoff Net Average | The average distance from the kickoff spot to the opponentâ€™s starting field position. | kickoff net average, net kickoff average |
| Defensive Touchdowns | Total touchdowns scored by the defense (interception or fumble return touchdowns). | defensive touchdowns, defensive touchdown, touchdowns by defense, defense touchdowns, interception return touchdowns, fumble return touchdowns, defensive scores |
| Points Responsible For | Total points scored or directly credited to the player (touchdowns, passing touchdowns, field goals, extra points, and two-point conversions). | points responsible for, points responsible, responsible for points |
| Field Goal Attempts Under 20 Yards | Total field goal attempts from distances less than 20 yards. | field goal attempts under 20 yards, field goal attempts below 20 yards, field goal attempts less than 20 yards, under 20 yard field goal attempts |
| Field Goal Attempts 20+ Yards | Total field goal attempts from distances of 20 yards or more. | field goal attempts above 20 yards, field goal attempts over 20 yards, 20+ yard field goal attempts |
| Field Goal Attempts 30+ Yards | Total field goal attempts from distances of 30 yards or more. | field goal attempts 30+ yards, field goal attempts above 30 yards, field goal attempts over 30 yards, 30+ yard field goal attempts |
| Field Goal Attempts 40+ Yards | Total field goal attempts from distances of 40 yards or more. | field goal attempts 40+ yards, field goal attempts above 40 yards, field goal attempts over 40 yards, 40+ yard field goal attempts |
| Field Goal Attempts 50+ Yards | Total field goal attempts from distances of 50 yards or more. | field goal attempts 50+ yards, field goal attempts above 50 yards, field goal attempts over 50 yards, 50+ yard field goal attempts, fga under 50 |
| Field Goal Attempts 60+ Yards | Total field goal attempts from distances of 60 yards or more. | field goal attempts 60+ yards, field goal attempts above 60 yards, field goal attempts over 60 yards, 60+ yard field goal attempts |
| Field Goal Attempts Under 20 Yards | Total field goal attempts from distances less than 20 yards. | field goal attempts under 20 yards, field goal attempts below 20 yards, field goal attempts less than 20 yards, under 20 yard field goal attempts |
| Field Goal Attempts Under 30 Yards | Total field goal attempts from distances less than 30 yards. | field goal attempts under 30 yards, field goal attempts below 30 yards, field goal attempts less than 30 yards, under 30 yard field goal attempts |
| Field Goal Attempts Under 40 Yards | Total field goal attempts from distances less than 40 yards. | field goal attempts under 40 yards, field goal attempts below 40 yards, field goal attempts less than 40 yards, under 40 yard field goal attempts |
| Field Goal Attempts Under 50 Yards | Total field goal attempts from distances less than 50 yards | field goal attempts under 50 yards, field goal attempts below 50 yards, field goal attempts less than 50 yards, under 50 yard field goal attempts |
| Field Goal Attempts Under 60 Yards | Total field goal attempts from distances less than 60 yards. | field goal attempts under 60 yards, field goal attempts below 60 yards, field goal attempts less than 60 yards, under 60 yard field goal attempts |
| Field Goals Made below 20 Yards | Total field goals made from distances less than 20 yards. | field goals made under 20 yards, field goals made below 20 yards, field goals made less than 20 yards, under 20 yard field goals made |
| Field Goals Made from 20+ Yards | Total field goals made from distances greater than or equal to 20 yards. | field goals made above 20 yards, field goals made over 20 yards, 20+ yard field goals made |
| Field Goals Made from 30+ Yards | Total field goals made from distances greater than or equal to 30 yards. | field goals made 30+ yards, field goals made above 30 yards, field goals made over 30 yards, 30+ yard field goals made |
| Field Goals Made from 40+ Yards | Total field goals made from distances greater than or equal to 40 yards. | field goals made 40+ yards, field goals made above 40 yards, field goals made over 40 yards, 40+ yard field goals made |
| Field Goals Made from 50+ Yards | Total field goals made from distances greater than or equal to 50 yards. | field goals made 50+ yards, field goals made above 50 yards, field goals made over 50 yards, 50+ yard field goals made |
| Field Goals Made from 60+ Yards | Total field goals made from distances greater than or equal to 60 yards. | field goals made 60+ yards, field goals made above 60 yards, field goals made over 60 yards, 60+ yard field goals made |
| Field Goals Made under 20 Yards | Total field goals made from distances less than 20 yards. | field goals made under 20 yards, field goals made below 20 yards, field goals made less than 20 yards, under 20 yard field goals made |
| Field Goals Made Under 30 Yards | Total field goals made from distances less than 30 yards. | field goals made under 30 yards, field goals made below 30 yards, field goals made less than 30 yards, under 30 yard field goals made |
| Field Goals Made under 40 Yards | Total field goals made from distances less than 40 yards. | field goals made under 40 yards, field goals made below 40 yards, field goals made less than 40 yards, under 40 yard field goals made |
| Field Goals Made under 50 Yards | Total field goals made from distances less than 50 yards. | field goals made under 50 yards, field goals made below 50 yards, field goals made less than 50 yards, under 50 yard field goals made |
| Field Goals Made under 60 Yards | Total field goals made from distances less than 60 yards. | field goals made under 60 yards, field goals made below 60 yards, field goals made less than 60 yards, under 60 yard field goals made |
| Punt Return 0+ Yards | Total punt returns greater than or equal to 0 yards. | punt returns greater than 0 yards, punt returns 0 or more yards |
| Punt Returns 10+ Yards | Total punt returns greater than or equal to 10 yards. | punt returns greater than 10 yards, punt returns 10 or more yards |
| Punt Returns 20+ Yards | Total punt returns greater than or equal to 20 yards. | punt returns greater than 20 yards, punt returns 20 or more yards, punt returns 20+ yards |
| Punt Returns 30+ Yards | Total punt returns greater than or equal to 30 yards. | punt returns greater than 30 yards, punt returns 30 or more yards |
| Punt Returns 40+ Yards | Total punt returns greater than or equal to 40 yards. | punt returns greater than 40 yards, punt returns 40 or more yards |
| Punt Returns 50+ Yards | Total punt returns greater than or equal to 50 yards. | punt returns greater than 50 yards, punt returns 50 or more yards |
| Punt Returns Under 10 Yards | Total punt returns less than 10 yards. | punt return under 10 yards, punt return less than 10 yards |
| Punt Returns Under 20 Yards | Total punt returns less than 20 yards. | punt return under 20 yards, punt return less than 20 yards |
| Punt Returns Under 30 Yards | Total punt returns less than 30 yards. | punt return under 30 yards, punt return less than 30 yards |
| Punt Returns Under 40 Yards | Total punt returns less than 40 yards. | punt return under 40 yards, punt return less than 40 yards |
| Punt Returns Under 50 Yards | Total punt returns less than 50 yards. | punt return under 50 yards, punt return less than 50 yards |
| Passes Completed 0+ Yards | Number of completed passes that gained 0 or more yards. | passes completed 0+ yards, 0+ yard completions, completed passes 0+ |
| Passes Completed 10+ Yards | Number of completed passes that gained 10 or more yards. | passes completed 10+ yards, 10+ yard completions, completed passes 10+ |
| Passes Completed 20+ Yards | Number of completed passes that gained 20 or more yards. | passes completed 20+ yards, 20+ yard completions, completed passes 20+ |
| Passes Completed 30+ Yards | Number of completed passes that gained 30 or more yards. | passes completed 30+ yards, 30+ yard completions, completed passes 30+ |
| Passes Completed 40+ Yards | Number of completed passes that gained 40 or more yards. | passes completed 40+ yards, 40+ yard completions, completed passes 40+ |
| Passes Completed 50+ Yards | Number of completed passes that gained 50 or more yards. | passes completed 50+ yards, 50+ yard completions, completed passes 50+ |
| Passes Completed Under 10 Yards | Number of completed passes that gained less than 10 yards. | passes completed under 10 yards, completions under 10 yards, completed passes less than 10 |
| Passes Completed Under 20 Yards | Number of completed passes that gained less than 20 yards. | passes completed under 20 yards, completions under 20 yards, completed passes less than 20 |
| Passes Completed Under 30 Yards | Number of completed passes that gained less than 30 yards. | passes completed under 30 yards, completions under 30 yards, completed passes less than 30 |
| Passes Completed Under 40 Yards | Number of completed passes that gained less than 40 yards. | passes completed under 40 yards, completions under 40 yards, completed passes less than 40 |
| Passes Completed Under 50 Yards | Number of completed passes that gained less than 50 yards. | passes completed under 50 yards, completions under 50 yards, completed passes less than 50 |
| Receptions 0+ Yards | Number of receptions that gained 0 or more yards. | receptions 0+ yards, receptions for 0+ yards, catches 0+ yards, receptions with 0+ yards, non-negative receptions |
| receptions Above 10 yards | Number of reception with receiving yards greater than or equal to 10 yards. | receptions above 10 yards, receiving yards over 10 |
| receptions Above 20 yards | Number of reception with receiving yards greater than or equal to 20 yards. | receptions above 20 yards, receiving yards over 20 |
| receptions Above 30 yards | Number of reception with receiving yards greater than or equal to 30 yards. | receptions above 30 yards, receiving yards over 30 |
| receptions Above 40 yards | Number of reception with receiving yards greater than or equal to 40 yards. | receptions above 40 yards, receiving yards over 40 |
| receptions Above 50 yards | Number of reception with receiving yards greater than or equal to 50 yards. | receptions above 50 yards, receiving yards over 50 |
| Receptions Under 10 Yards | Number of reception with receiving yards less than 10 yards. | receptions below 10 yards, receptions under 10 yards |
| Receptions Under 20 Yards | Number of reception with receiving yards less than 20 yards. | receptions below 20 yards, receptions under 20 yards |
| Receptions Under 30 Yards | Number of reception with receiving yards less than 30 yards. | receptions below 30 yards, receptions under 30 yards |
| Receptions Under 40 Yards | Number of reception with receiving yards less than 40 yards. | receptions below 40 yards, receptions under 40 yards |
| Receptions Under 50 Yards | Number of reception with receiving yards less than 50 yards. | receptions below 50 yards, receptions under 50 yards |
| Rush Attempts 0+ Yards | Number of rushing attempts that gained 0 or more yards. | rush attempts 0+ yards, rushing attempts 0+ yards, rushes for 0+ yards, rushes with 0+ yards, non-negative rush attempts, rush attempts no loss |
| Rushing Attempts 10+ Yards | number of rushes with rushing yards greater than or equal to 10 yards. | rushing attempts above 10 yards, rushing attempts over 10 yards, rushing attempts 10+ yards |
| Rushing Attempts 20+ Yards | number of rushes with rushing yards greater than or equal to 20 yards. | rushing attempts above 20 yards, rushing attempts over 20 yards, rushing attempts 20+ yards |
| Rushing Attempts 30+ Yards | number of rushes with rushing yards greater than or equal to 30 yards. | rushing attempts above 30 yards, rushing attempts over 30 yards |
| Rushing Attempts 40+ Yards | number of rushes with rushing yards greater than or equal to 40 yards. | rushing attempts above 40 yards, rushing attempts over 40 yards |
| Rushing Attempts 50+ Yards | number of rushes with rushing yards greater than or equal to 50 yards. | rushing attempts above 50 yards, rushing attempts over 50 yards |
| Rushing Attempts Below 10 Yards | number of rushes with rushing yards less than 10 yards. | rushing attempts below 10 yards, rushing attempts under 10 yards |
| Rushing Attempts Below 20 Yards | number of rushes with rushing yards less than 20 yards. | rushing attempts below 20 yards, rushing attempts under 20 yards |
| Rushing Attempts Below 30 Yards | number of rushes with rushing yards less than 30 yards. | rushing attempts below 30 yards, rushing attempts under 30 yards |
| Rushing Attempts Below 40 Yards | number of rushes with rushing yards less than 40 yards. | rushing attempts below 40 yards, rushing attempts under 40 yards |
| Rushing Attempts Below 50 Yards | number of rushes with rushing yards less than 50 yards. | rushing attempts below 50 yards, rushing attempts under 50 yards |

## MFB Teams Statistics

| Statistic Name | Description | Aliases |
| --- | --- | --- |
| Completed Passes | The total number of successful pass completions by the team. | pass comp |
| Passing Yards | The total number of yards gained by the team through completed passes. | pass yards, pass yds, passing yds |
| Longest Pass | The longest single pass completion by the team in the game. | longest pass |
| Passing Touchdowns | The total number of touchdowns scored by the team through passing plays. | pass td, passing td |
| Intercepted Passes | The number of passes thrown by the team that were intercepted by the opposing defense. | defense interception, interceptions caught |
| Pass Attempts | The total number of times the team attempted a forward pass. | pass att |
| Times Sacked | The number of times the team's quarterback was sacked while attempting to pass. | pass sacks |
| Sack Yards Lost | The total number of yards lost by the team due to sacks. | pass sack yards, passing sck yards, pass sack yds, passing sack yds |
| Receptions | The total number of completed catches made by the team's receivers. | catches, receiving catches |
| Receiving Yards | The total number of yards gained by the team through receptions. | receiving yards, receiving yds, rec yds |
| Longest Reception | The longest single reception made by a player on the team. | longest catch, receiving long |
| Receiving Touchdowns | The total number of touchdowns scored by the team via receptions. | touchdown receptions |
| Rushing Attempts | The total number of times the team attempted a rushing play. | rush att, rushing att |
| Net Rushing Yards | The total number of yards gained by the team on rushing plays, subtracting any yards lost. | rushing yards, rush yards, rush yds, rushing yds |
| Rushing Yards Gained | The total number of yards gained by the team on rushing plays before any losses. | rushing gain, rush gain |
| Longest Rush | The longest single rushing play executed by the team. | longest carry |
| Rushing Touchdowns | The total number of touchdowns scored by the team on rushing plays. | rush td, rushing td |
| Rushing Yards Lost | The total number of yards lost by the team on rushing plays. | rushing loss, rush loss |
| Total First Downs | The total number of first downs achieved by the team. |  |
| First Downs by Rushing | The number of first downs achieved by the team through rushing plays. |  |
| First Downs by Passing | The number of first downs achieved by the team through passing plays. |  |
| First Downs by Penalty | The number of first downs awarded to the team due to penalties committed by the opposing team. |  |
| Third Down Attempts | The total number of times the team attempted a play on third down. |  |
| Third Down Conversions | The total number of times the team successfully converted a third down attempt into a first down. |  |
| Fourth Down Attempts | The total number of times the team attempted a play on fourth down. |  |
| Fourth Down Conversions | The total number of times the team successfully converted a fourth down attempt into a first down. |  |
| Fumbles Lost | The total number of times the team fumbled the ball and lost possession. | lost fumble |
| Total Fumbles | The total number of fumbles committed by the team, regardless of whether possession was lost. |  |
| Total Penalties | The total number of penalties committed by the team. |  |
| Penalty Yards | The total number of yards lost due to penalties committed by the team. |  |
| Red Zone Attempts | The total number of times the team reached the opponent's red zone (inside the 20-yard line). |  |
| Red Zone Scores | The number of times the team successfully scored (touchdown or field goal) after entering the red zone. |  |
| Red Zone Points | The total number of points scored by the team from red zone possessions. |  |
| Red Zone Rushing Touchdowns | The number of touchdowns the team scored by rushing inside the red zone. |  |
| Red Zone Passing Touchdowns | The number of touchdowns the team scored by passing inside the red zone. |  |
| Red Zone Field Goals Made | The total number of field goals successfully made from red zone possessions. |  |
| Red Zone Field Goal Attempts | The total number of field goal attempts the team made from red zone possessions. |  |
| Red Zone Turnovers on Downs | The number of times the team failed to convert a fourth down in the red zone, losing possession. |  |
| Red Zone Interceptions | The number of times the team threw an interception inside the red zone. |  |
| Red Zone Fumbles Lost | The number of times the team fumbled and lost possession inside the red zone. |  |
| Red Zone End of Half | The number of times a red zone possession ended due to the end of the half. |  |
| Red Zone End of Game | The number of times a red zone possession ended due to the end of the game. |  |
| Miscellaneous Yards | The total number of yards gained or lost by the team in plays classified as miscellaneous. |  |
| Time of Possession | The total amount of time the team controlled the ball during the game. |  |
| Onside Kick Attempts | The total number of onside kick attempts made by the team. |  |
| Onside Kicks Recovered | The number of successful onside kicks recovered by the team. |  |
| Points off Turnovers | The total number of points scored by the team after forcing a turnover. |  |
| Assisted Tackles | The number of tackles where the defender contributed but did not make the solo tackle. | assist tackles |
| Solo Tackles | The number of tackles made solely by a defender without assistance. |  |
| Total Tackles | The total number of tackles made by the team, including solo and assisted tackles. | tackles |
| Interceptions | The number of passes intercepted by the team's defense. | interceptions thrown, pass had intercepted |
| Interception Return Yards | The total number of yards gained by the team after intercepting a pass. | ir yards |
| Pass Breakups | The number of times the team successfully defended a pass without intercepting it. | pbu |
| Unassisted Sacks | The number of times a single defender sacked the opposing quarterback. | solo sacks |
| Assisted Sacks | The number of times multiple defenders contributed to sacking the quarterback. | assist sacks |
| Total Sacks | The total number of quarterback sacks made by the team's defense. | sacks, defense sacks |
| Sack Yards | The total number of yards lost by the opposing team due to sacks made by the defense. | defense sack yards, sack yds, defense sack yds |
| Quarterback Hurries | The number of times the team's defense forced the quarterback to throw early due to pressure. | qbh |
| Forced Fumbles | The number of times the team forced the opposing player to fumble the ball. | forced fumble(s) |
| Fumbles Recovered | The number of fumbles recovered by the team, regardless of who forced them. | fumble recoveries |
| Fumble Return Yards | The total number of yards gained after recovering a fumble. |  |
| Fumble Return Touchdowns | The total number of touchdowns scored by the team after recovering a fumble. | fumble return td |
| Kicks Blocked By | The total number of kicks (field goals or extra points) blocked by the player during the game. | blocked kicks |
| Assisted Tackles for Loss | The number of tackles for loss where multiple defenders contributed. | assisted tfl, assist tfl |
| Solo Tackles for Loss | The number of tackles for loss made solely by a defender. | unassisted tfl, solo tfl |
| Total Tackles for Loss | The total number of tackles resulting in negative yardage for the opposing team. | tfl, tackles for loss |
| Tackle for Loss Yards | The total number of yards lost by the opposing team due to tackles for loss. | tfl yards, tackle for loss yards, tfl yds, tackle for loss yds |
| Interception Return Yards | The total number of yards gained by the team after intercepting a pass. | ir yards |
| Interception Return Touchdowns | The total number of touchdowns scored by the team after intercepting a pass. | ir td |
| Longest Interception Return | The longest single interception return made by the team. | longest int return |
| Interceptions Made | The total number of passes intercepted by the team's defense. | interceptions thrown, pass had intercepted |
| Field Goals Made | The total number of successful field goals made by the team. | fgm |
| Field Goals Attempted | The total number of field goal attempts made by the team. | fga |
| Longest Field Goal Made | The longest field goal successfully made by the team. | longest fgm |
| Blocked Field Goals | The total number of field goal attempts blocked by the opposing team. | blocked fg |
| PAT Kicks Attempted | The total number of extra point kicks attempted after touchdowns. | pat kick att |
| PAT Kicks Made | The total number of successful extra point kicks made after touchdowns. |  |
| PAT Pass Attempts | The total number of pass attempts on a two-point conversion play after a touchdown. | pat pass att |
| PAT Pass Completions | The number of successful pass attempts on a two-point conversion play. | pat pass made |
| PAT Rush Attempts | The total number of rushing attempts on a two-point conversion play. | pat rush att |
| PAT Rush Completions | The number of successful rushing attempts on a two-point conversion play. | pat rush made |
| Total Kickoffs | The total number of times the team kicked off to start a drive. | kcikoffs |
| Kickoff Yards | The total number of yards gained on all kickoffs. | kickoff yards |
| Kickoff Touchbacks | The number of kickoffs that resulted in a touchback. | kickoff tb |
| Kickoffs Out of Bounds | The number of kickoffs that went out of bounds, resulting in a penalty. | kickoff oob |
| Kick Returns | The total number of kickoffs returned by the team. | kick returns |
| Kick Return Yards | The total number of yards gained by the team on kickoff returns. | kr yards, kr yds |
| Kick Return Touchdowns | The total number of touchdowns scored on kickoff returns. | kr td |
| Longest Kick Return | The longest single kickoff return by the team. | longest kr |
| Total Punts | The total number of times the team punted the ball. |  |
| Punting Yards | The total number of yards gained on all punts. | punting yds, punt yards, punt yds |
| Punts of 50+ Yards | The number of punts that traveled at least 50 yards. | punt >50, punt>50yds |
| Punts Inside 20 | The number of punts that landed inside the opponent's 20-yard line. | punts inside 20 |
| Longest Punt | The longest single punt made by the team. | punt long |
| Punt Touchbacks | The number of punts that resulted in a touchback. | punts tb |
| Fair Catches on Punts | The number of punts where the receiving team called a fair catch. | punts fc |
| Blocked Punts | The number of punts that were blocked by the opposing team. | blocked punts |
| Punt Returns | The total number of punts returned by the team. |  |
| Punt Return Yards | The total number of yards gained by the team on punt returns. | pr yards, pr yds |
| Punt Return Touchdowns | The total number of touchdowns scored on punt returns. | pr td |
| Longest Punt Return | The longest single punt return made by the team. | longest pr |
| Total Touchdowns | The total number of touchdowns scored by the team across all types of plays. | scoring touchdowns |
| Total Field Goals Made | The total number of successful field goals made by the team. | fgm |
| Total PAT Kicks Made | The total number of successful extra point kicks made by the team. |  |
| Passing Yards Per Attempt | The average number of yards gained per passing attempt by the team. | pass yards per att |
| Pass Completion Percentage | The percentage of pass attempts completed by the team. | pass comp percent |
| Average Rushing Yards | The average number of net yards gained per rushing attempt by the team. | avg yards per carry, avg yds per carry, avg yds per rush, avg yards per rush |
| Average Yards per Reception | The average number of yards gained per reception by the team. | avg receiving yds, avg rec yds, avg reception yds |
| Takeaways | The number of times the team recovered a fumble or intercepted a pass. |  |
| Field Goal Percentage | The percentage of field goal attempts successfully made by the team. | fgm percent |
| Kickoffs Returned | The number of kickoffs returned by the team. | kickoff ret |
| Average Punt Return Yards | The average number of yards gained per punt return by the team. | punt return avg, punt ret avg |
| Net Kickoff Yards | The total net yards gained on kickoffs by the special teams unit. | kickoff yds, kickoff yards |
| Average Punt Yards | The average number of yards per punt made by the team. | avg punt yds, avg punt yards |
| Total Offensive Yards | The total number of yards gained by the team on offense. | total offense yds, total off yds |
| All-Purpose Yards | The total yards gained by the team from rushing, receiving, and returns. | all purp yds, all purpose yds |
| 1st Down Attempts | The total number of 1st down attempts. |  |
| 1st Down Conversions | The number of successful 1st down conversions. |  |
| 2nd Down Attempts | The total number of 2nd down attempts. |  |
| 2nd Down Conversions | The number of successful 2nd down conversions. |  |
| Biggest Lead of the game | The highest point margin by which the team led during the game. |  |
| Biggest scoring run | The highest number of consecutive points scored without interruption. |  |
| Longest field goal attempt | The longest field goal attempted during the game, regardless of whether it was successful. |  |
| Field Goal Blocked by | The number of field goals blocked by the team or player. |  |
| Longest fumble return | The longest distance returned by the team after recovering a fumble. |  |
| Total fumble returns | The total number of fumble returns by the team. |  |
| average yards per fumble return | The average yards gained on fumble returns. |  |
| Avg yards per interception return | The average yards gained after intercepting a pass. |  |
| Average gross yards from kickoff | The average gross yardage gained per kickoff. |  |
| Kickoff gross yards | The total gross yardage gained from all kickoffs. |  |
| Kick-off return average | The average yards gained per kickoff return. |  |
| Total kickoff returns | The total number of kickoff returns attempted. |  |
| All kicks blocked by | The number of any type of kicks (FG, PAT, punt) blocked by the team. |  |
| Avg yards per pass completion | The average number of yards gained per completed pass. |  |
| PAT attempt | The total number of point-after-touchdown (PAT) attempts. |  |
| PAT kick blocked | The number of PAT kicks that were blocked. |  |
| PAT kick blocked by | The number of PAT kicks blocked by the team. |  |
| PAT Fumble return | The number of fumble returns that occurred during PAT attempts. |  |
| PAT kick return | The number of PAT kick returns after a failed attempt. |  |
| PAT kick made | The total number of successful PAT kicks made. |  |
| PAT receptions | The number of receptions made during a 2-point PAT attempt. |  |
| PAT 2pt conversion | The number of 2-point conversion attempts following a touchdown. |  |
| PAT 2pt made | The number of successful 2-point PAT conversions. |  |
| All purpose net yards | Total yards gained by a player including rushing, receiving, and returns. |  |
| Total plays | Total number of offensive plays executed. |  |
| Total points | Total number of points scored by the team. |  |
| Punts blocked by | The number of punts blocked by the team. |  |
| Average punt yards (net) | The average net distance of all punts. |  |
| Net punt yards | The total net yardage of all punts. |  |
| Redzone Score | The number of times the team scored when in the red zone. |  |
| Redzone attempts passing plays | The number of pass plays attempted in the red zone. |  |
| Rush left | The number of rushing plays attempted to the left side. |  |
| Rush middle | The number of rushing plays attempted up the middle. |  |
| Rush right | The number of rushing plays attempted to the right side. |  |
| Safety 2 pt | The number of safeties (2-point defensive scores) recorded. |  |
| Times team lead | The total time the team was leading in the game. |  |
| Times score was tied | The number of times the score was tied during the game. |  |
| Turnovers | The total number of times the team gave up possession via fumble or interception. |  |
| Wins in overtime | The number of overtime games won. |  |
| Average yards per play | The average number of yards gained per offensive play. |  |
| Biggest lead score | The score margin representing the largest lead held by the team during the game. |  |
| Biggest scoring run score | The total number of points scored during the team's longest uninterrupted scoring run. |  |
| Goal efficiency attempts | The total number of attempts made in goal-to-go situations. |  |
| Goal efficiency field goals | The number of successful field goals scored in goal-to-go situations. |  |
| Field goal formation plays | The total number of plays run using a field goal formation. |  |
| Punt formation plays | The total number of plays executed from a punt formation. |  |
| Shotgun formation plays | The total number of offensive plays run from the shotgun formation. |  |
| Under center formation plays | The total number of offensive plays run with the quarterback under center. |  |
| Quarterback kneels | The total number of quarterback kneel-down plays. |  |
| Lead changes | The number of times the lead changed between teams during the game. |  |
| Huddle plays | The total number of offensive plays run using a traditional huddle. |  |
| No-huddle plays | The total number of offensive plays run without a huddle. |  |
| Quarterback scrambles | The number of times the quarterback scrambled and ran the ball. |  |
| Wins when leading at halftime | The number of games won when the team was leading at halftime. |  |
| Wins by 7 points or less | The number of games won by a margin of seven points or fewer. |  |
